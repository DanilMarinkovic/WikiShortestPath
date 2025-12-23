#include "parser.hpp"
#include <libxml/xmlreader.h>
#include <iostream>
#include <cstring>

std::string Parser::findPage(const std::string& target) {
    xmlTextReaderPtr reader = xmlReaderForFile(PATH.c_str(), nullptr, 0);
    if (!reader) {
        std::cerr << "Failed to open XML file: " << PATH << "\n";
        return "";
    }

    std::string currentTitle;
    std::string pageText;
    int ret;

    while ((ret = xmlTextReaderRead(reader)) == 1) {
        int nodeType = xmlTextReaderNodeType(reader);
        const xmlChar* nodeName = xmlTextReaderConstName(reader);

        if (nodeType == XML_READER_TYPE_ELEMENT && nodeName) {
            std::string tag = reinterpret_cast<const char*>(nodeName);

            if (tag == "title") {
                xmlChar* content = xmlTextReaderReadString(reader);
                if (content) {
                    currentTitle = reinterpret_cast<const char*>(content);
                    xmlFree(content);
                }
            }

            if (tag == "text" && currentTitle == target) {
                xmlChar* content = xmlTextReaderReadString(reader);
                if (content) {
                    pageText = reinterpret_cast<const char*>(content);
                    xmlFree(content);
                    break;
                }
            }
        }

    }

    xmlFreeTextReader(reader);

    if (pageText.empty()) {
        std::cout << "Article not found: " << target << std::endl;
    }

    return pageText;
}
    std::vector<std::string> Parser::getLinks(const std::string& text){
        std::vector<std::string> links;
        size_t pos = 0;
        while((pos = text.find("[[",pos))!=std::string::npos){
            size_t end;
            if((end = text.find("]]",pos))==std::string::npos){
                break;
            }
            std::string link = text.substr(pos + 2, end - pos - 2);
            pos = end + 2;
            links.push_back(link);
        }
    return links;
}
      
