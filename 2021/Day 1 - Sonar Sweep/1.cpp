#include <bits/stdc++.h>
using namespace std;

int increasesOfDepth(const vector<int> &depthMeasurements){
    int increases = 0;
    for (int i = 1; i < depthMeasurements.size(); ++i){
        if (depthMeasurements[i-1] < depthMeasurements[i]){
            ++increases;
        }
    }
    return increases;
}


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fstream input;
    vector<int> depthMeasurements;
    int depth;
    input.open("input.txt", ios::in);
    while (input >> depth){
        depthMeasurements.emplace_back(depth);
    }
    cout << increasesOfDepth(depthMeasurements) << "\n";
    return 0;
}
