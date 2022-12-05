#include <bits/stdc++.h>
using namespace std;


string topCratesContent(vector<stack<char>> &crateStacks) {
    string content = "";
    for (auto &crateStack : crateStacks) {
        content.push_back(crateStack.top());
    }
    return content;
}


void constructCrateStacks (fstream &input, vector<stack<char>> &crateStacks) {
    vector<string> lines;
    string line;
    char crate;
    int numStacks;
    // Read until blank line
    while (getline(input, line, '\n')) {
        if (line == "") {
            break;
        }
        lines.emplace_back(line);
    }
    // Last line has the numbers, ending with a blank space
    line = *lines.rbegin();
    // Remove it's blank space
    line.pop_back();
    // Remove it from the lines with the crates
    lines.pop_back();

    // Find the last number in that line
    stringstream str(line);
    string num;
    while (getline(str, num, ' ')) {}
    numStacks = stoi(num);

    // Populate the crate stacks
    crateStacks.clear();
    crateStacks.resize(numStacks, stack<char>());
    for (auto it = lines.rbegin(); it != lines.rend(); ++it) {
        for (int i = 0; i < numStacks; ++i) {
            crate = (*it)[4*i + 1];
            if (crate != ' ') {
                crateStacks[i].emplace(crate);
            }
        }
    }
}


void useCrateMover9000(int qnty, int origin, int destination, vector<stack<char>> &crateStacks) {
    for (int i = 0; i < qnty; ++i) {
        crateStacks[destination].emplace(crateStacks[origin].top());
        crateStacks[origin].pop();
    }
}


void useCrateMover9001(int qnty, int origin, int destination, vector<stack<char>> &crateStacks) {
    stack<char> pile;
    for (int i = 0; i < qnty; ++i) {
        pile.emplace(crateStacks[origin].top());
        crateStacks[origin].pop();
    }
    while (!pile.empty()) {
        crateStacks[destination].emplace(pile.top());
        pile.pop();
    }
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;

    vector<stack<char>> crateStacks1;

    string del;
    int qnty, origin, destination;

    input.open("input.txt", ios::in);

    constructCrateStacks(input, crateStacks1);
    auto crateStacks2 = crateStacks1;

    while (input >> del >> qnty >> del >> origin >> del >> destination) {
        --origin;
        --destination;
        useCrateMover9000(qnty, origin, destination, crateStacks1);
        useCrateMover9001(qnty, origin, destination, crateStacks2);
    }

    cout << "With CrateMover 9000: " << topCratesContent(crateStacks1) << "\n";
    cout << "With CrateMover 9001: " << topCratesContent(crateStacks2) << "\n";

    input.close();
    return 0;
}
