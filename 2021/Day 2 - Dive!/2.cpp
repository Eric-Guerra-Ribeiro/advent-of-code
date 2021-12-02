#include <bits/stdc++.h>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fstream input;
    input.open("input.txt", ios::in);

    int depth = 0;
    int horizontalPosition = 0;
    int aim = 0;
    string direction;
    int X;
    while (input >> direction >> X){
        if (direction == "forward"){
            horizontalPosition += X;
            depth += aim*X;
        }
        else if (direction == "up"){
            aim -= X;
        }
        else if (direction == "down"){
            aim += X;
        }
    }
    cout << "Part 1: " << aim*horizontalPosition << "\n";
    cout << "Part 2: " << depth*horizontalPosition << "\n";
    return 0;
}
