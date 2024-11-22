#include <bits/stdc++.h>

using namespace std;



void getAnswer(string s, int k) {
    vector<int> vec[30];
    int min_val = 1e9, max_val = 0;
    for (int i=0; i<s.size(); i++) {
        vec[s[i]-'a'].push_back(i);
    }
    for (char a='a'; a<='z'; a++) {
        int index = a - 'a';
        int sz = vec[index].size()-k+1;

        for (int i=0; i<sz; i++) {
            int left = vec[index][i], right = vec[index][i+k-1];
            int len = right - left + 1;
            min_val = min(min_val ,len);
            max_val = max(max_val, len);
        }
    }
    if (max_val == 0) cout << -1 << endl;
    else cout << min_val << " " << max_val << endl;
}

void getInput() {
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        int k;
        cin >> k;

        getAnswer(s, k);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    getInput();
    return 0;
}
