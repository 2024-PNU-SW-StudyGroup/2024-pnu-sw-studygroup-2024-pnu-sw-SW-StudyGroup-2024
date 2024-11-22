#include <bits/stdc++.h>

using namespace std;

int N;
string initString, targetString;

char changeString(char c) {
    return c == '0' ? '1' : '0';
}

int getZeroPush(string tmp) {
    int zeroPush = 0;
    for (int i=0; i<N; i++) {
        if (tmp[i] != targetString[i]) {
            if (i < N-1) {
                tmp[i] = changeString(tmp[i]);
                tmp[i+1] = changeString(tmp[i+1]);
            }
            if (i < N-2) tmp[i+2] = changeString(tmp[i+2]);
            zeroPush++;
        }
    }
    if (tmp != targetString) return 1e9;
    return zeroPush;
}
void getAnswer() {
    // 00111010101
    // 11000001001
    int answer = getZeroPush(initString);
    initString[0] = changeString(initString[0]);
    initString[1] = changeString(initString[1]);
    answer = min(answer, getZeroPush(initString) + 1);
    if (answer == 1e9) cout << -1;
    else cout << answer;
}

void getInput() {
    cin >> N;
    cin >> initString >> targetString;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    getAnswer();

    return 0;
}
