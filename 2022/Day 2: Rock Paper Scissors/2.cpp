#include <bits/stdc++.h>
using namespace std;

enum class MatchResult {
    WIN, LOSE, DRAW
};

enum class PlayChoice {
    ROCK, PAPER, SCISSOR
};

PlayChoice transformToPlay(char choice) {
    switch (choice) {
    case 'A':
    case 'X':
        return PlayChoice::ROCK;
    case 'B':
    case 'Y':
        return PlayChoice::PAPER;
    case 'C':
    case 'Z':
        return PlayChoice::SCISSOR;
    default:
        throw invalid_argument("No such choice exits.");
    }
}

MatchResult transformToResult(char choice) {
    switch (choice) {
    case 'X':
        return MatchResult::LOSE;
    case 'Y':
        return MatchResult::DRAW;
    case 'Z':
        return MatchResult::WIN;
    default:
        throw invalid_argument("No such choice exits.");
    }
}

MatchResult getMatchResult(PlayChoice opponentChoice, PlayChoice playerChoice) {
    if (opponentChoice == playerChoice) {
        return MatchResult::DRAW;
    }
    if (playerChoice == PlayChoice::ROCK) {
        switch (opponentChoice) {
        case PlayChoice::PAPER:
            return MatchResult::LOSE;
        case PlayChoice::SCISSOR:
            return MatchResult::WIN;
        }
    }
    if (playerChoice == PlayChoice::PAPER) {
        switch (opponentChoice) {
        case PlayChoice::SCISSOR:
            return MatchResult::LOSE;
        case PlayChoice::ROCK:
            return MatchResult::WIN;
        }
    }
    if (playerChoice == PlayChoice::SCISSOR) {
        switch (opponentChoice) {
        case PlayChoice::ROCK:
            return MatchResult::LOSE;
        case PlayChoice::PAPER:
            return MatchResult::WIN;
        }
    }
    throw invalid_argument("Impossible match");
}

int choicePoints(PlayChoice choice) {
    switch (choice) {
    case PlayChoice::ROCK:
        return 1;
    case PlayChoice::PAPER:
        return 2;
    case PlayChoice::SCISSOR:
        return 3;
    default:
        throw invalid_argument("No such choice exits.");
    }
}

int resultPoints(MatchResult result) {
    switch (result) {
    case MatchResult::WIN:
        return 6;
    case MatchResult::DRAW:
        return 3;
    case MatchResult::LOSE:
        return 0;
    default:
        throw invalid_argument("Impossible match");
    }
}

int matchPointsByPlay(PlayChoice opponent, PlayChoice player) {
    return choicePoints(player) + resultPoints(getMatchResult(opponent, player));
}

int matchPointsPart2(PlayChoice opponent, MatchResult result) {
    PlayChoice player;
    for (auto choice : {PlayChoice::ROCK, PlayChoice::PAPER, PlayChoice::SCISSOR}) {
        if (result == getMatchResult(opponent, choice)) {
            player = choice;
            break;
        }
    }
    return matchPointsByPlay(opponent, player);
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    fstream input;
    char opponent;
    char player;
    MatchResult opponentChoice;
    MatchResult playerChoice;
    int totalPointsPart1;
    int totalPointsPart2;

    input.open("input.txt", ios::in);

    while (input >> opponent >> player) {
        totalPointsPart1 += matchPointsByPlay(transformToPlay(opponent), transformToPlay(player));
        totalPointsPart2 += matchPointsPart2(transformToPlay(opponent), transformToResult(player));
    }

    cout << "Points part 1: " << totalPointsPart1 << "\n";
    cout << "Points part 2: " << totalPointsPart2 << "\n";

    input.close();
    return 0;
}
