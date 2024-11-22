#include <bits/stdc++.h>

using namespace std;

string s;

int getB() {
    int b = 0;
    for (auto ss: s) {
        if (ss == 'b') {
            b++;
        }
    }
    return b;
}
// 8 7
void getAnswer() {
    int answer = 1e9;
    int b = getB();
    string ss = s + s;
    for (int i=0; i<s.size(); i++) {
        int cnt = 0;
        for (int j=0; j<b; j++) {
            int tmp = i+j;
            if (ss[tmp] == 'a') cnt++;
        }
        answer = min(answer, cnt);
    }
    if (answer == 1e9) cout << 0;
    else cout << answer;
}

void getInput() {
    cin >> s;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    getAnswer();

    return 0;
}
