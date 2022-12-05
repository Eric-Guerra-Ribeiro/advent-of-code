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
    // Remove it from the lines and it's blank space
    line = *lines.rbegin();
    line.pop_back();
    lines.pop_back();
    stringstream str(line);
    string num;
    // Find the last number in that line
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

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;

    vector<stack<char>> crateStacks;

    string del;
    int qnty, origin, destination;

    input.open("input.txt", ios::in);

    constructCrateStacks(input, crateStacks);

    while (input >> del >> qnty >> del >> origin >> del >> destination) {
        useCrateMover9000(qnty, --origin, --destination, crateStacks);
    }

    cout << "With CrateMover 9000: " << topCratesContent(crateStacks) << "\n";

    input.close();
    return 0;
}
