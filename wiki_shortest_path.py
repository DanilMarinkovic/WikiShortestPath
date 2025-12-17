import wikipediaapi
from collections import deque

MAX_DEPTH = 3

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="WikiShortestPathBot/1.0 (https://github.com/DanilMarinkovic/WikiShortestPath)"
)

def should_skip_page(title):
    skip_prefixes = [
        "Category:", "File:", "Template:", "Wikipedia:",
        "Help:", "Portal:", "Talk:", "User:", "Special:",
        "Media:", "MediaWiki:", "Module:", "Draft:",
    ]
    
    for prefix in skip_prefixes:
        if title.startswith(prefix):
            return True
    
    if "(disambiguation)" in title:
        return True
    
    return False

def bidirectional_bfs(source_title, target_title, max_depth=None):
    if max_depth is None:
        max_depth = MAX_DEPTH
    
    source_page = wiki.page(source_title)
    target_page = wiki.page(target_title)
    
    if not source_page.exists():
        print(f"Source page '{source_title}' does not exist.")
        return None
    
    if not target_page.exists():
        print(f"Target page '{target_title}' does not exist.")
        return None
    
    print(f"Searching from '{source_page.title}' to '{target_page.title}' (max depth: {max_depth})")
    
    if source_page.title == target_page.title:
        return [source_page.title]
    
    forward_queue = deque([(source_page.title, 0)])
    forward_visited = {source_page.title: [source_page.title]}

    backward_queue = deque([(target_page.title, 0)])
    backward_visited = {target_page.title: [target_page.title]}
    
    nodes_explored = 0
    
    while forward_queue or backward_queue:
        if forward_queue and (not backward_queue or len(forward_queue) <= len(backward_queue)):
            result = explore_level(
                forward_queue, forward_visited, backward_visited,
                max_depth, nodes_explored,"forward")
        else:
            result = explore_level(
                backward_queue, backward_visited, forward_visited,
                max_depth, nodes_explored,"backward")
        
    if result is not None:
        if isinstance(result, tuple):
            path, nodes_explored = result
            print(f"Path found! Explored {nodes_explored} pages.\n")
            return path
        else:
            nodes_explored = result
    
    print(f"No path found within {max_depth} links. Explored {nodes_explored} pages.\n")
    return None

def explore_level(queue, visited, other_visited, max_depth, nodes_explored, direction):
    if not queue:
        return None
    
    level_size = len(queue)
    
    for _ in range(level_size):
        current_title, depth = queue.popleft()
        nodes_explored += 1
        
        if nodes_explored % 100 == 0:
            print(f"[{direction}] Explored {nodes_explored}, depth: {depth}, queue: {len(queue)}\n")
        
        if depth >= max_depth:
            continue
        current_page = wiki.page(current_title)
        link_titles = list(current_page.links.keys())
        
        for link_title in link_titles:
            if link_title in other_visited:
                path = reconstruct_path(
                    visited[current_title], link_title, other_visited[link_title], direction
                )
                return (path, nodes_explored)
            if should_skip_page(link_title):
                continue
            
            if link_title not in visited:
                visited[link_title] = visited[current_title] + [link_title]
                queue.append((link_title, depth + 1))
    
    return nodes_explored

def reconstruct_path(forward_path, meeting_point, backward_path, direction):
    if direction == "forward":
        if forward_path[-1] != meeting_point:
            forward_path = forward_path + [meeting_point]
        return forward_path + backward_path[-2::-1]
    else:
        if backward_path[-1] != meeting_point:
            backward_path = backward_path + [meeting_point]
        return forward_path + backward_path[-2::-1]

if __name__ == "__main__":
    source = "Monty Python"
    target = "Comedy"
    
    path = bidirectional_bfs(source, target, max_depth=MAX_DEPTH)
    if path:
        print("Shortest path:")
        for i, page in enumerate(path):
            print(f"  {i}. {page}")
        print(f"Path length: {len(path) - 1} link(s)\n")
    else:
        print(f"No path found from '{source}' to '{target}'\n")