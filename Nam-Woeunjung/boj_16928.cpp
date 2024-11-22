#include <bits/stdc++.h>

using namespace std;

int N, M;
int vec[101];
int visited[101] = {0, };

void getAnswer() {
    queue<pair<int, int>> q;
    q.push({1, 0});
    visited[1] = 1;

    while (!q.empty()) {
        auto [game, cnt] = q.front();
        q.pop();

        for (int i=1; i<=6; i++) {
            int nx = game + i;
            while (vec[nx] != 0) {
                nx = vec[nx];
            }
            if (nx == 100) {
                cout << cnt + 1;
                return;
            }
            if (nx > 100) continue;
            if (visited[nx] == 0) {
                visited[nx] = 1;
                q.push({nx, cnt+1});
            }
        }
    }
}

void getInput() {
    int x, y;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> x >> y;
        vec[x] = y;
    }
    for (int i=0; i<M; i++) {
        cin >> x >> y;
        vec[x] = y;
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
