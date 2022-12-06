#include <bits/stdc++.h>
using namespace std;

class StartMarker {
private:
    queue<char> packet;
    unordered_map<char, int> charFreqs; // Frequence of each char in the packet
    int length;
public:
    StartMarker(int length);
    void recieveChar(char c);
    bool isStart();
};

StartMarker::StartMarker(int length) {
    this->length = length;
}

void StartMarker::recieveChar(char c) {
    if (packet.size() == length) {
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
    if (packet.size() != length) {
        return false;
    }
    for (auto &charFreq : charFreqs) {
        if (charFreq.second > 1) {
            return false;
        }
    }
    return true;
}

int findStartMarker(string &datastreamBuffer, StartMarker &marker) {
    for (int start = 0; start < datastreamBuffer.length(); ++start) {
        if (marker.isStart()) {
            return start;
        }
        marker.recieveChar(datastreamBuffer[start]);
    }
    throw invalid_argument("No start marker was found");
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    string datastreamBuffer;

    StartMarker packetStart(4);
    int startOfPacket;
    
    StartMarker messageStart(14);
    int startOfMessage;

    input.open("input.txt", ios::in);

    input >> datastreamBuffer;

    startOfPacket = findStartMarker(datastreamBuffer, packetStart);
    startOfMessage = findStartMarker(datastreamBuffer, messageStart);

    cout << "Start of the Packet Marker: " << startOfPacket << "\n";
    cout << "Start of the Message Marker: " << startOfMessage << "\n";

    input.close();
    return 0;
}
