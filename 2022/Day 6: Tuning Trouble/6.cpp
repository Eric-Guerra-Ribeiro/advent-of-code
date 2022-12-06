#include <bits/stdc++.h>
using namespace std;

class StartMarker {
private:
    queue<char> packet;
    unordered_map<char, int> charFreqs; // Frequence of each char in the packet
public:
    void recieveChar(char c);
    bool isStart();
};

void StartMarker::recieveChar(char c) {
    if (packet.size() == 4) {
        auto charFreq = charFreqs.find(packet.front());
        if (charFreq->second == 1) {
            charFreqs.erase(charFreq);
        }
        else {
            --charFreq->second;
        }
        packet.pop();
    }
    auto charFreq = charFreqs.find(c);
    if (charFreq == charFreqs.end()) {
        charFreqs.emplace(c, 1);
    }
    else {
        ++charFreq->second;
    }
    packet.emplace(c);
}

bool StartMarker::isStart() {
    if (packet.size() != 4) {
        return false;
    }
    for (auto &charFreq : charFreqs) {
        if (charFreq.second > 1) {
            return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    string datastreamBuffer;

    StartMarker packetStart;
    int startOfPacket;

    input.open("input.txt", ios::in);

    input >> datastreamBuffer;

    for (startOfPacket = 0; startOfPacket < datastreamBuffer.length(); ++startOfPacket) {
        if (packetStart.isStart()) {
            break;
        }
        packetStart.recieveChar(datastreamBuffer[startOfPacket]);
    }

    cout << "Start of the Packet Marker: " << startOfPacket << "\n";

    input.close();
    return 0;
}
