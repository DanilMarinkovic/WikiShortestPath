import wikipediaapi
from collections import deque

MAX_DEPTH = 2

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="WikiShortestPathBot/1.0 (https://github.com/DanilMarinkovic/WikiShortestPath)"
)

def bfs_shortest_path(source_title, target_title, max_depth=None):
    if max_depth is None:
        max_depth = MAX_DEPTH
    source_page = wiki.page(source_title)
    if not source_page.exists():
        print(f"source page '{source_title}' does not exist.")
        return

    queue = deque([(source_page, [source_page.title])])
    visited = set([source_page.title])

    while queue:
        current_page, path = queue.popleft()

        if current_page.title == target_title:
            return path

        if len(path) - 1 > max_depth:
            continue

        for link_title, linked_page in current_page.links.items():
            if link_title not in visited:
                visited.add(link_title)
                print(f"Link {link_title} added \n")
                queue.append((linked_page, path + [link_title]))

    return None 

source = "Monty Python"
target = "Comedy"

path = bfs_shortest_path(source, target, max_depth=MAX_DEPTH)
if path:
    print("Shortest path:", " -> ".join(path))
else:
    print(f"No path found from {source} to {target} within {MAX_DEPTH} links.")
