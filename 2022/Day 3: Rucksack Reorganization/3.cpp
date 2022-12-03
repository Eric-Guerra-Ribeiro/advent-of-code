#include <bits/stdc++.h>
using namespace std;


int calculatePriority(char c) {
    if ('a' <= c && c <= 'z') {
        return c - 'a' + 1;
    }
    if ('A' <= c && c <= 'Z') {
        return c - 'A' + 27;
    }
    throw invalid_argument("Invalid char");
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    string rucksackContent;
    unordered_set<char> firstCompartmentContent;
    int sumPriorities = 0;
    int comparmentSize;

    input.open("input.txt", ios::in);

    while (input >> rucksackContent) {
        firstCompartmentContent.clear();
        comparmentSize = rucksackContent.length()/2;
        for (auto c : rucksackContent.substr(0, comparmentSize)) {
            firstCompartmentContent.emplace(c);
        }
        for (auto c : rucksackContent.substr(comparmentSize)) {
            if (firstCompartmentContent.count(c) != 0) {
                sumPriorities += calculatePriority(c);
                break;
            }
        }
    }

    cout << sumPriorities << "\n";

    input.close();
    return 0;
}
