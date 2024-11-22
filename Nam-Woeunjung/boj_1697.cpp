#include <bits/stdc++.h>

using namespace std;

int N, K;
int answer = 1e9;

void getAnswer(int start, int end, int cnt) {
    answer = min(answer, cnt+abs(start-end));
    if (start == end) return;
    if (start <= 1) return;

    if (start%2) {
        int a = (start+1)/2, b = (start-1)/2;
        getAnswer(a, end, cnt+2);
        getAnswer(b, end, cnt+2);
    }
    else getAnswer(start/2, end, cnt+1);

}
// 2 1 0
// 100 0 = 100
void getInput() {
    cin >> N >> K;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    //0 100
    //
    if (K == 0) answer = N;
    else if (N != K) getAnswer(K, N, 0);
    else answer = 0;

    cout << answer;

    return 0;
}
