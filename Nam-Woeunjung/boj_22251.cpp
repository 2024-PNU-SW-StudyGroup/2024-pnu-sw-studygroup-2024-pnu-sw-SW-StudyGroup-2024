#include <bits/stdc++.h>

using namespace std;

int N, K, P, X;
string str_x;

int nums[10][7] = {
    {1, 1, 1, 0, 1, 1, 1},
    {0, 0, 1, 0, 0, 1, 0},
    {1, 0, 1, 1, 1, 0, 1},
    {1, 0, 1, 1, 0, 1, 1},
    {0, 1, 1, 1, 0, 1, 0},
    {1, 1, 0, 1, 0, 1, 1},
    {1, 1, 0, 1, 1, 1, 1},
    {1, 0, 1, 0, 0, 1, 0},
    {1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 0, 1, 1}
};
int answer = 0;
int diffs[11][11];

void getAnswer(int index, int cur_x, string s) {
    if (index == s.size()) {
        if (stoi(s) >= 1 && stoi(s) != X && stoi(s) <= N) answer++;
        return;
    }

    // 반전 없음
    getAnswer(index+1, cur_x, s);

    // 반전 있음
    // 1 이상 N층 이하인지, cur_x가 남아도는지
    string tmp = s;
    int charIndex = tmp[index] - '0';
    for (int i=0; i<10; i++) {
        if (i == charIndex) continue;
        string changed = s;
        changed[index] = '0' + i;
        int myx = diffs[charIndex][i];
        if (cur_x - myx >= 0) {
            getAnswer(index+1, cur_x-myx, changed);
        }
    }

}

void getInput() {
    cin >> N >> K >> P >> X;
    int tmp = X, cnt = 0;
    while(tmp > 0) {
        tmp /= 10;
        cnt++;
    }
    str_x = to_string(X);
    for (int i=0; i<K-cnt; i++) {
        str_x = '0' + str_x;
    }
    for (int i=0; i<10; i++) {
        for (int j=0; j<10; j++) {
            int num = 0;
            for (int k=0; k<7; k++) {
                if (nums[i][k] != nums[j][k]) {
                    num++;
                }
            }
            diffs[i][j] = num;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    getAnswer(0, P, str_x);
    cout << answer;
    return 0;
}
