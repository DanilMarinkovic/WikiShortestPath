#include "parser.hpp"
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

int main(int argc, char* argv[]) {
    if (argc != 3){
        std::cout << "Usage: " << argv[0] << "<source> <target>" << std::endl;
        return 1;
    }
    std::string source = argv[1];
    std::string target = argv[2];

    Parser parser;

    std::queue<std::string> q;
    std::unordered_set<std::string> visited;
    std::unordered_map<std::string, std::string> parent;

    q.push(source);
    visited.insert(source);
    parent[source] = "";
    bool found = false;
    while(!q.empty()){
        std::string curr = q.front();
        q.pop();
        if(curr == target){
            found = true;
            break;
        }
        std::vector<std::string> links = parser.getLinks(curr);
        for(const std::string& link : links) {
            if(visited.find(link) == visited.end()){
                visited.insert(link);
                parent[link] = curr;
                q.push(link);
            }
        }
    }
    if(found){
        std::vector<std::string> path;
        std::string curr = target;
    while(!curr.empty()) {
        path.push_back(curr);
        curr = parent[curr];
    }
    std::reverse(path.begin(), path.end());
    std::cout << "Shortest path found" << std::endl;
    for(size_t i = 0; i<path.size(); i++){
        std::cout << path[i];
        if (i < path.size() - 1) {
            std::cout << " -> ";
        }
    }
    std::cout << std::endl;
    } else {
        std::cout << "No path found" << std::endl;
    }
    return 0;
}
