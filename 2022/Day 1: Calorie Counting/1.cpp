#include <bits/stdc++.h>
using namespace std;


struct TopThree {
    int top1;
    int top2;
    int top3;

    TopThree() {
        top1 = top2 = top3 = -1;
    }

    void newChallenger(int val) {
        if (val > top1) {
            swap(top1, val);
        }
        if (val > top2) {
            swap(top2, val);
        }
        if (val > top3) {
            swap(top3, val);
        }
    }

    int sum() {
        return top1 + top2 + top3;
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    TopThree maxCalories = TopThree();
    int currentCalories;
    string line;

    input.open("input.txt", ios::in);

    int i = 0;
    do {
        getline(input, line);
        if (line == "") {
            maxCalories.newChallenger(currentCalories);
            currentCalories = 0;
        }
        else {
            currentCalories += stoi(line);
        }
    } while (!input.eof());
    cout << "1st: " << maxCalories.top1 << "\n";
    cout << "2nd: " << maxCalories.top2 << "\n";
    cout << "3rd: " << maxCalories.top3 << "\n";
    cout << "All three: " << maxCalories.sum() << "\n";
    input.close();
    return 0;
}
