#include <iostream>
#include <string>
#include <fstream>
#include "parser.hpp"

int main() {
    const std::string target = "Bukayo Saka";
    Parser parser;
    parser.findPage(target);
    return 0;
}
