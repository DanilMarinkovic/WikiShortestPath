#pragma once
#include <string>

class Parser{
    public:
        int findPage(const std::string& target);
    private:
        std::string PATH = "../data/simplewiki-latest-pages-articles-multistream.xml";
};
