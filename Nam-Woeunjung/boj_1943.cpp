#include <bits/stdc++.h>

using namespace std;

int isPossible(int N, pair<int, int> money[100001], int target) {
    int dp[100001] = {0, };
    dp[0] = 1;

    for (int i=0; i<N; i++) {
        auto [price, cnt] = money[i];
        if (dp[target]) return 1;
        for (int j=50000; j>=0; j--) {
            if (j - price >= 0 && dp[j - price]) {
                for (int k=0; k<cnt; k++) {
                    if (j + price * k <= 50000) {
                        dp[j + price * k] = 1;
                    }
                }
            }
        }
    }
    return dp[target];
}

void solve() {
    int N;
    pair<int, int> money[100001];
    cin >> N;
    int total = 0;
    for (int i=0; i<N; i++) {
        int x, y;
        cin >> x >> y;
        money[i] = {x, y};
        total += x * y;
    }
    if (total % 2) cout << 0 << endl;
    else cout << isPossible(N, money, total/2) << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // 10:09
    solve();
    solve();
    solve();

    return 0;
}
