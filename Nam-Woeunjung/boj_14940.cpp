#include <bits/stdc++.h>

using namespace std;

int n, m;
int target_x, target_y;
int arr[1001][1001];
int dist[1001][1001];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};

bool isValid(int x, int y) {
    return x >= 0 && y >= 0 && x < n && x < m;
}

void getAnswer() {
    queue<pair<int, int>> q;
    q.push({target_x, target_y});
    dist[target_x][target_y] = 1;

    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        for (int i=0; i<4; i++) {
            int tx = x+dx[i], ty = y+dy[i];
            if (isValid(tx, ty)&& dist[tx][ty] == 0 && arr[tx][ty] == 1) {
                dist[tx][ty] = dist[x][y] + 1;
                q.push({tx, ty});
            }
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (arr[i][j] == 0) cout << 0 << " ";
            else if (dist[i][j] == 0) cout << -1 << " ";
            else cout << dist[i][j]-1 << " ";
        }
        cout << endl;
    }
}

void getInput() {
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 2) {
                target_x = i, target_y = j;
            }
        }
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
