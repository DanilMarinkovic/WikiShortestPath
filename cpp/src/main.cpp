#include <iostream>
#include <string>
#include <fstream>

int main() {
    std::ifstream wiki("../data/simplewiki-latest-pages-articles-multistream.xml");
    std::string test;

    if(!wiki.is_open()){
        std::cerr << "Could not open file" << std::endl;
        return 1;
    }
    int count = 0;
    while(std::getline(wiki, test) && count < 10){
        std::cout << test << std::endl;
        count++;
    }
    wiki.close();
    return 0;
}

