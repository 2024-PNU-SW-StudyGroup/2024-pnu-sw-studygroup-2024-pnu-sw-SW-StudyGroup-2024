#include <bits/stdc++.h>

using namespace std;

int N, M;
char arr[100][100];
int start_x, start_y;
vector<pair<int, int>> end_vec;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, 1, -1, 0};
int visited[200][100][100];


bool isInValid(int x, int y) {
    return !(x >= 0 && x < N && y >= 0 && y < M);
}

int isKeyNotExist(int k, int b) {
    return k & (1 << b);
}

int addKey(int k, int b) {
    return k | (1 << b);
}

void getAnswer() {
    queue<pair<pair<int, int>,int>> q;
    vector<int> keys;
    visited[0][start_x][start_y] = 1;
    q.push({{start_x, start_y}, 0});

    while (!q.empty()) {
        auto [pos, k] = q.front();
        auto [x, y] = pos;
        q.pop();

        if (arr[x][y] == '1') {
            cout << visited[k][x][y] -1;
            return;
        }

        for (int i=0; i<4; i++) {
            int tx = x + dx[i], ty = y + dy[i];
            if (isInValid(tx, ty)) continue;
            if (arr[tx][ty] == '#') continue;
            if (visited[k][tx][ty]) continue;

            if (arr[tx][ty] >= 'A' && arr[tx][ty] <= 'Z'
                && !isKeyNotExist(k, arr[tx][ty] - 'A')) {
                continue;
            }
            if (arr[tx][ty] >= 'a' && arr[tx][ty] <= 'z') {
                int kk = addKey(k, arr[tx][ty] - 'a');
                if (!visited[kk][tx][ty]) {
                    visited[kk][tx][ty] = visited[k][x][y]+1;
                    q.push({{tx, ty}, kk});
                }
            }
            else {
                visited[k][tx][ty] = visited[k][x][y]+1;
                q.push({{tx, ty}, k});
            }
        }
    }
    cout << -1;
}

void getInput() {
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == '0') {
                start_x = i, start_y = j;
            }

        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // 10:50 - 12:40
    // visited 3차원, bfs 까지는 알았는데
    // 비트 마스킹;; 선넘네
    getInput();
    getAnswer();

    return 0;
}

