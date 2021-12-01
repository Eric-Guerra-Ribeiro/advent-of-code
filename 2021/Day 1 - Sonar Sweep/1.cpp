#include <bits/stdc++.h>
using namespace std;

int movingIncreasesOfDepth(const vector<int> &depthMeasurements, int numberOfDepths){
    if (numberOfDepths > depthMeasurements.size()){
        exit(1);
    }
    int increases = 0;
    for (int i = numberOfDepths; i < depthMeasurements.size(); ++i){
        if (depthMeasurements[i-numberOfDepths] < depthMeasurements[i]){
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
    cout << movingIncreasesOfDepth(depthMeasurements, 1) << "\n";
    cout << movingIncreasesOfDepth(depthMeasurements, 3) << "\n";
    return 0;
}
