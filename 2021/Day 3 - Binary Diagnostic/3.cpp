#include <bits/stdc++.h>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fstream input;
    input.open("input.txt", ios::in);

    string data;
    vector<string> diagnostic;
    vector<int> gamma;
    int gammaRate = 0;
    int epsilonRate;
    int len;
    int shift;

    while (input >> data){
        diagnostic.emplace_back(data);
    }

    len = (int) data.length();
    gamma.resize(len);

    for (auto s : diagnostic){
        for (int i = 0; i < len; ++i){
            switch (s[i]){
            case '0':
                --gamma[i];
                break;
            case '1':
                ++gamma[i];
                break;
            }
        }
    }
    int pow = 1;
    for (int i = len - 1; i >= 0; --i){
        if (gamma[i] > 0){
            gammaRate += pow;
        }
        pow *= 2;
    }
    epsilonRate = ~gammaRate;
    shift = 8*sizeof(epsilonRate) - len;
    epsilonRate = epsilonRate << shift;
    epsilonRate = epsilonRate >> shift;

    cout << "Part 1: " << gammaRate*epsilonRate << "\n";
    cout << "Part 2: " << "" << "\n";
    return 0;
}
