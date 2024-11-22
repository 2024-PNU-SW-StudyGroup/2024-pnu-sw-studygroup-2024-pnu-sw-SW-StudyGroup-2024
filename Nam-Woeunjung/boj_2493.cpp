#include <bits/stdc++.h>

using namespace std;

int n;
int arr[500001];

void getAnswer() {
    vector<pair<int, int>> q;
    for (int i=0; i<n; i++) {
        while (!q.empty() && q.back().first <= arr[i]) {
            q.pop_back();
        }
        if (q.empty()) cout << 0 << " ";
        else cout << q.back().second+1 << " ";

        q.push_back({arr[i], i});
    }
}

void getInput() {
    cin >> n;
    for (int i=0; i<n; i++) {
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
