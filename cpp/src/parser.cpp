#include "parser.hpp"
#include <libxml/xmlreader.h>
#include <iostream>
#include <cstring>

int Parser::findPage(const std::string& target) {
    xmlTextReaderPtr reader = xmlReaderForFile(PATH.c_str(), nullptr, 0);
    if (!reader) {
        std::cerr << "Failed to open XML file: " << PATH << "\n";
        return false;
    }

    std::string currentTitle;
    bool found = false;

    int ret = xmlTextReaderRead(reader);
    while (ret == 1 && !found) {
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
                    std::cout << content << std::endl;
                    xmlFree(content);
                }
                found = true;
                break;
            }
        }

        ret = xmlTextReaderRead(reader);
    }

    xmlFreeTextReader(reader);

    if (!found) {
        std::cout << "Article not found: " << target << std::endl;
        return 1;
    }

    return 0;
}

