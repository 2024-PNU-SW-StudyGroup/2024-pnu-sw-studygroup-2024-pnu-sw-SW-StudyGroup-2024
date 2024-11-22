#include <bits/stdc++.h>

using namespace std;

int M, N;
int start_x, start_y, start_direction;
int end_x, end_y, end_direction;
int arr[101][101];
int visited[5][101][101];


bool isValid(int y, int x) {
    return y >= 1 && x >= 1 && y <= M && x <= N;
}

void getAnswer() {
    queue<pair<pair<int, int>, pair<int, int>>> q;
    visited[start_direction][start_y][start_x] = 1;
    q.push({{start_y, start_x}, {start_direction, 0}});

    while (!q.empty()) {
        auto [pos, num] = q.front();
        auto [y, x] = pos;
        auto [dir, cnt] = num;
        q.pop();

        //cout << y << " " << x << " " << dir  << " " << cnt << endl;
        if (y == end_y && x == end_x && dir == end_direction) {
            cout << cnt;
            break;
        }
        // 이동
        for (int i=1; i<=3; i++) {
            int ty = y, tx = x;
            bool flag = false;

            if (dir == 1) {
                for (int j=1; j<=i; j++) {
                    tx++;
                    if (arr[ty][tx]) flag = true;
                }
            }
            if (dir == 2) {
                for (int j=1; j<=i; j++) {
                    tx--;
                    if (arr[ty][tx]) flag = true;
                }
            }
            if (dir == 3) {
                for (int j=1; j<=i; j++) {
                    ty++;
                    if (arr[ty][tx]) flag = true;
                }
            }
            if (dir == 4) {
                for (int j=1; j<=i; j++) {
                    ty--;
                    if (arr[ty][tx]) flag = true;
                }
            }
            if (flag) continue;

            if (isValid(ty, tx) && !arr[ty][tx] && !visited[dir][ty][tx]) {
                visited[dir][ty][tx] = 1;
                q.push({{ty, tx}, {dir, cnt+1}});
            }
        }

        // 회전
        // 왼쪽 이동: 1 -> 4, 2 -> 3, 3 -> 1, 4 -> 2
        int left;
        if (dir == 1) left = 4;
        if (dir == 2) left = 3;
        if (dir == 3) left = 1;
        if (dir == 4) left = 2;

        if (!visited[left][y][x]) {
            visited[left][y][x] = 1;
            q.push({{y, x}, {left, cnt+1}});
        }

        // 오른쪽 이동: 1 -> 3, 2 -> 4, 3 -> 2, 4 -> 1
        int right;
        if (dir == 1) right = 3;
        if (dir == 2) right = 4;
        if (dir == 3) right = 2;
        if (dir == 4) right = 1;

        if (!visited[right][y][x]) {
            visited[right][y][x] = 1;
            q.push({{y, x}, {right, cnt+1}});
        }
    }
}

void getInput() {
    cin >> M >> N;
    for (int i=1; i<=M; i++) {
        for (int j=1; j<=N; j++) {
            cin >> arr[i][j];
        }
    }
    cin >> start_y >> start_x  >> start_direction;
    cin >> end_y >> end_x >> end_direction;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    getAnswer();

    return 0;
}

