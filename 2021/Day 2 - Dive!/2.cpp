#include <bits/stdc++.h>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fstream input;
    input.open("input.txt", ios::in);

    int depth = 0;
    int horizontalPosition = 0;
    string direction;
    int X;
    while (input >> direction >> X){
        if (direction == "forward"){
            horizontalPosition += X;
        }
        else if (direction == "up"){
            depth -= X;
        }
        else if (direction == "down"){
            depth += X;
        }
    }
    cout << depth*horizontalPosition << "\n";
    return 0;
}
