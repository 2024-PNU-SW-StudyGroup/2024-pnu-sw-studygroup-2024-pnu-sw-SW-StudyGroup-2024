#include <bits/stdc++.h>

using namespace std;

int N;
int arr[100001];

void getAnswer() {
    int start = 0, end = N-1;
    int answer = 1e9*2, answer_start, answer_end;
    while (start < end) {
        int num = arr[start] + arr[end];
        if (abs(answer) > abs(num)) {
            answer = num;
            answer_start = arr[start];
            answer_end = arr[end];
            if (num == 0) break;
        }
        if (abs(arr[start]) > abs(arr[end])) {
            start++;
        }
        else end--;
    }
    cout << answer_start << " " << answer_end;
}

void getInput() {
    cin >> N;
    for (int i=0; i<N; i++) {
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
