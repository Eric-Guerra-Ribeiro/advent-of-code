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
    int sumPrioritiesWrongItem = 0;
    int comparmentSize;

    unordered_set<char> rucksack;
    unordered_set<char> badgeCandidates;
    int groupCounter = 0;
    int sumPrioritiesBadges = 0;

    input.open("input.txt", ios::in);

    while (input >> rucksackContent) {
        // Part 1
        firstCompartmentContent.clear();
        comparmentSize = rucksackContent.length()/2;
        for (auto c : rucksackContent.substr(0, comparmentSize)) {
            firstCompartmentContent.emplace(c);
        }
        for (auto c : rucksackContent.substr(comparmentSize)) {
            if (firstCompartmentContent.count(c) != 0) {
                sumPrioritiesWrongItem += calculatePriority(c);
                break;
            }
        }
        // Part 2

        switch (groupCounter) {
        case 0:
            rucksack.clear();
            for (auto c : rucksackContent) {
                rucksack.emplace(c);
            }
            break;
        case 1:
            badgeCandidates.clear();
            for (auto c : rucksackContent) {
                if (rucksack.count(c) != 0) {
                    badgeCandidates.emplace(c);
                }
            }
            break;
        case 2:
            for (auto c : rucksackContent) {
                if (badgeCandidates.count(c) != 0) {
                    sumPrioritiesBadges += calculatePriority(c);
                    break;
                }
            }
            break;
        }
        groupCounter = (groupCounter + 1)%3;
    }

    cout << "Part 1: " << sumPrioritiesWrongItem << "\n";
    cout << "Part 2: " << sumPrioritiesBadges << "\n";

    input.close();
    return 0;
}
