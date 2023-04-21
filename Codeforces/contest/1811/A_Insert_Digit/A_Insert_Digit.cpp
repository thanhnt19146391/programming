#include <bits/stdc++.h>

using namespace std;

void solve(int n, int d, string s) {
    // Search suitable position of digit
    int p = 0;
    for (int i = 0; i < n; i++) {
        int cur_digit = s[i] - '0';
        if (cur_digit > d) {
                p = i + 1;
        }
        else {
            break;
        }
    }
    string pre_str = s.substr(0, p);
    char digit_str = (char)(d + '0');
    string suf_str = s.substr(p, n - p);
    string res = pre_str + digit_str + suf_str;

//    cout << p << '\n' ;
    cout << res << '\n';
//    cout << "----" << '\n';

}

int main()
{
    int T;
    cin >> T;
    while (T--) {
        int n, d;
        string s;
        cin >> n >> d >> s;
        solve(n, d, s);
    }

    return 0;
}

8281271277321
8281127127732
