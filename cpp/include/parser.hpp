#pragma once
#include <string>
#include <vector>
#include <unordered_map>

class Parser{
    public:
        std::vector <std::string> getLinks(const std::string& text);
    private:
        std::string findPage(const std::string& target);
        const std::string PATH = "../data/simplewiki-latest-pages-articles-multistream.xml";
        std::unordered_map<std::string, std::vector<std::string>> linkCache;
};
