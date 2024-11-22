#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<pair<int, int>> mymap[50001];

void getAnswer() {
    vector<int> dist(N+1, 1e9);
    queue<int> q;

    dist[1] = 0;
    q.push(1);

    while (!q.empty()) {
        int pq = q.front();
        q.pop();

        for (auto m: mymap[pq]) {
            auto [b, w] = m;
            if (dist[b] > dist[pq]+w) {
                dist[b] = dist[pq]+w;
                q.push(b);
            }
        }
    }
    cout << dist[N];
}

void getInput() {
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        mymap[a].push_back({b,c});
        mymap[b].push_back({a,c});
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
