#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

ifstream file;
string line;
regex reg("seeds:");


int main() {
    file.open("input_1.txt");

    if (file.is_open()) {
        while (getline(file, line)) {
            
            if (regex_search(line, reg))
                printf("MATCH");
        }
    }

    return 0;
}