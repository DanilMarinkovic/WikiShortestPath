import wikipediaapi
from collections import deque

def bfs_shortest_path(source_title, target_title, max_depth=3):
    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="WikiShortestPathBot/1.0 (https://github.com/DanilMarinkovic/WikiShortestPath)"
    )

    source_page = wiki.page(source_title)
    target_page = wiki.page(target_title)

    if not source_page.exists() or not target_page.exists():
        print("Source or Target page does not exist.")
        return None
    queue = deque([(source_page.title, 0)])
    visited = {source_page.title: None}
    
    nodes_explored = 0

    print(f"Searching from '{source_page.title}' to '{target_page.title}'")

    while queue:
        current_title, depth = queue.popleft()
        nodes_explored += 1

        if current_title == target_page.title:
            print(f"Found target! Explored {nodes_explored} pages.\n")
            return reconstruct_path(visited, current_title)

        if depth >= max_depth:
            continue
        if nodes_explored % 100 == 0:
            print(f"Explored {nodes_explored}, Current Depth: {depth}, Queue Size: {len(queue)}")

        current_page = wiki.page(current_title)
        try:
            links = list(current_page.links.keys())
        except Exception as e:
            print(f"Error fetching links for {current_title}: {e}")
            continue

        for link_title in links:
            if link_title not in visited and not should_skip_page(link_title):
                visited[link_title] = current_title
                queue.append((link_title, depth + 1))
                if link_title == target_page.title:
                    print(f"Found target! Explored {nodes_explored} pages.\n")
                    return reconstruct_path(visited, link_title)

    print("Target not found within depth limit.")
    return None

def reconstruct_path(visited, current_title):
    path = []
    while current_title is not None:
        path.append(current_title)
        current_title = visited[current_title]
    return path[::-1] 

def should_skip_page(title):
    if "(disambiguation)" in title: return True
    if ":" in title:
        skip_prefixes = ["Category:", "File:", "Template:", "Wikipedia:", "Help:", "Portal:"]
        if any(title.startswith(p) for p in skip_prefixes):
            return True
    return False

if __name__ == "__main__":
    path = bfs_shortest_path("Bukayo Saka", "Python (programming language)")
    if path:
        print("Path found:\n")
        for i, step in enumerate(path):
            print(f"{i}. {step}")