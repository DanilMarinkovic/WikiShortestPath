#pragma once
#include <string>
#include <vector>

class Parser{
    public:
        std::string findPage(const std::string& target);
        std::vector <std::string> getLinks(const std::string& text);
    private:
        std::string PATH = "../data/simplewiki-latest-pages-articles-multistream.xml";
};
