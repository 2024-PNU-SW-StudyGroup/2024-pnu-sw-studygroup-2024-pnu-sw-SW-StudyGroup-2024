#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
int N;
vector<pair<int, pair<int, int>>> tree[11];
int parent[11], child[11];

ll gcd(ll a, ll b) {
    ll c;
    while (b != 0) {
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}

ll lcm(ll a, ll b) {
    return a * b / gcd(a, b);
}

void cocktail(int a) {
    for (auto t: tree[a]) {
        auto [b, pq] = t;
        auto [p, q] = pq;

        if (parent[b] == 0) {
            parent[b] = parent[a] * p;
            child[b] = child[a] * q;

            // 이 부분 떄문에 처음에 틀림
            ll g = gcd(parent[b], child[b]);
            parent[b] /= g;
            child[b] /= g;
            cocktail(b);
        }
    }
}

ll makeIntPercent() {
    ll num = parent[0];
    for (int i=1; i<N; i++) {
        num = lcm(num, parent[i]);
    }
    return num;
}

void getAnswer() {
    parent[0] = 1;
    child[0] = 1;
    cocktail(0);
    ll num = makeIntPercent();
    for (int i=0; i<N; i++) {
        cout << (num / parent[i]) * child[i] << " ";
    }
}

void getInput() {
    int a, b, p, q;
    cin >> N;
    for (int i=0; i<N-1; i++) {
        cin >> a >> b >> p >> q;
        for (int j=2; j<=9; j++) {
            if (p % j == 0 && q % j == 0) {
                p /= j;
                q /= j;
            }
        }
        tree[a].push_back({b, {p, q}});
        tree[b].push_back({a, {q, p}});
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // 1시간 정도 걸림, 반례 하나 보고 푼
    // 4
    // 3 2 1 2
    // 2 1 1 1
    // 1 0 4 1
    // 답: 1 4 4 2

    getInput();
    getAnswer();

    return 0;
}

