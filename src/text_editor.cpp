#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

bool fileExists(const string& filename) {
    ifstream file(filename);
    return file.good();
}

void createFile(const string& filename, const string& content) {
    ofstream file(filename);
    if (file) {
        file << content;
        cout << "File '" << filename << "' created successfully!" << endl;
    } else {
        cout << "Error creating file!" << endl;
    }
    file.close();
}

void readFile(const string& filename) {
    if (fileExists(filename)) {
        ifstream file(filename);
        string line;
        while (getline(file, line)) {
            cout << line << endl;
        }
        file.close();
    } else {
        cout << "File '" << filename << "' does not exist!" << endl;
    }
}

void updateFile(const string& filename, const string& content) {
    if (fileExists(filename)) {
        ofstream file(filename, ios::app);
        file << content;
        cout << "File '" << filename << "' updated successfully!" << endl;
        file.close();
    } else {
        cout << "File '" << filename << "' does not exist!" << endl;
    }
}

void deleteFile(const string& filename) {
    if (fileExists(filename)) {
        if (remove(filename.c_str()) == 0) {
            cout << "File '" << filename << "' deleted successfully!" << endl;
        } else {
            cout << "Error deleting file!" << endl;
        }
    } else {
        cout << "File '" << filename << "' does not exist!" << endl;
    }
}

void searchWord(const string& filename, const string& word) {
    if (fileExists(filename)) {
        ifstream file(filename);
        string line;
        int lineNumber = 0;
        bool found = false;
        while (getline(file, line)) {
            lineNumber++;
            if (line.find(word) != string::npos) {
                cout << "Found '" << word << "' in line " << lineNumber << ": " << line << endl;
                found = true;
            }
        }
        if (!found) {
            cout << "Word '" << word << "' not found in the file." << endl;
        }
        file.close();
    } else {
        cout << "File '" << filename << "' does not exist!" << endl;
    }
}

void fileStatistics(const string& filename) {
    if (fileExists(filename)) {
        ifstream file(filename);
        string line;
        int lineCount = 0;
        int wordCount = 0;
        int charCount = 0;

        while (getline(file, line)) {
            lineCount++;
            charCount += line.length();
            stringstream ss(line);
            string word;
            while (ss >> word) {
                wordCount++;
            }
        }

        cout << "File Statistics for '" << filename << "':" << endl;
        cout << "Number of lines: " << lineCount << endl;
        cout << "Number of words: " << wordCount << endl;
        cout << "Number of characters: " << charCount << endl;

        file.close();
    } else {
        cout << "File '" << filename << "' does not exist!" << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        cout << "Usage: <operation> <filename> [content]" << endl;
        return 1;
    }

    string operation = argv[1];
    string filename = argv[2];
    string content = (argc > 3) ? argv[3] : "";

    if (operation == "create") {
        createFile(filename, content);
    } else if (operation == "read") {
        readFile(filename);
    } else if (operation == "update") {
        updateFile(filename, content);
    } else if (operation == "delete") {
        deleteFile(filename);
    } else if (operation == "search") {
        if (argc > 3) {
            searchWord(filename, content);
        } else {
            cout << "Search word not provided!" << endl;
        }
    } else if (operation == "stats") {
        fileStatistics(filename);
    } else {
        cout << "Invalid operation!" << endl;
    }

    return 0;
}
