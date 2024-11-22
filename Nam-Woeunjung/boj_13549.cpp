#include <bits/stdc++.h>

using namespace std;

int N, K;
int visited[100002];

void getAnswer() {
    for (int i=0; i<=100000; i++) visited[i] = 1e9;
    queue<int> q;
    q.push(N);
    visited[N] = 0;

    while (!q.empty()) {
        int x = q.front();
        q.pop();

        int right = x+1, left = x-1, twice = x*2;
        if (right <= 100000 && visited[right] > visited[x]) {
            visited[right] = visited[x] + 1;
            q.push(right);
        }
        if (left >= 0 && visited[left] > visited[x]) {
            visited[left] = visited[x] + 1;
            q.push(left);
        }
        if (twice <= 100000 && visited[twice] > visited[x]) {
            visited[twice] = visited[x];
            q.push(twice);
        }
    }
    cout << visited[K];
}

void getInput() {
    cin >> N >> K;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    if (N == K) cout << 0;
    else if (N < K) getAnswer();
    else cout << N-K;

    return 0;
}
