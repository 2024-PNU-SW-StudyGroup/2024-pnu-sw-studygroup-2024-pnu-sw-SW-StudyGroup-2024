#include <bits/stdc++.h>

using namespace std;

int N, K;
int arr[202];

bool isNoRobot(int target, vector<int> &robots) {
    for (auto r: robots) {
        if (r == target) return false;
    }
    return true;
}

void getAnswer() {
    int zero = 0, index = 0, cnt = 0;
    vector<int> robots;

    while (zero < K) {
        index--;
        cnt++;

        if (index < 0) index += 2*N;
        int outIndex = (index <= N) ? index+N-1 : index-N-1;

        int i=0;
        while (i<robots.size()) {
            int robot = robots[i];
            if (robot == outIndex) {
                robots.erase(robots.begin()+i);
                continue;
            }
            int nextIndex = (robot+1)%(2*N);
            if (isNoRobot(nextIndex, robots) && arr[nextIndex] > 0) {
                robots[i] = nextIndex;
                if (nextIndex == outIndex) {
                    robots.erase(robots.begin()+i);
                    i--;
                }
                arr[nextIndex]--;
                if (arr[nextIndex] == 0) zero++;
            }
            i++;
        }
        if (arr[index] > 0) {
            robots.push_back(index);
            arr[index]--;
            if (arr[index] == 0) zero++;
        }
    }
    cout << cnt;
}

void getInput() {
    cin >> N >> K;
    for (int i=0; i<2*N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    getAnswer();

    return 0;
}
