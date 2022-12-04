#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    char del;
    int min1st, max1st;
    int min2nd, max2nd;

    int overlapsFully = 0;
    int overlapsAtAll = 0;

    input.open("input.txt", ios::in);

    while (input >> min1st >> del >> max1st >> del >> min2nd >> del >> max2nd) {
        if (    (min1st <= min2nd && max2nd <= max1st)
             || (min2nd <= min1st && max1st <= max2nd)) {
            ++overlapsFully;
        }
        if  (min2nd <= max1st && min1st <= max2nd) {
            ++overlapsAtAll;
        }
    }

    cout << "Overlaps fully: " << overlapsFully << "\n";
    cout << "Overlaps at all: " << overlapsAtAll << "\n";

    input.close();
    return 0;
}
