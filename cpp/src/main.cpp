#include <iostream>
#include <string>
#include "parser.hpp"

int main(int argc, char* argv[]) {
    if (argc != 2){
        std::cout << "Usage: " << argv[0] << " \"target\"" << std::endl;
        return 1;
    }
    std::string target = argv[1];
    Parser target_parser;
    auto text = target_parser.findPage(target);
    auto links = target_parser.getLinks(text);
    for(auto i = 0uz; i!=links.size(); i++){
        std::cout << "Link number " << i << " is "<<links[i] << std::endl;
    }
    return 0;
}
