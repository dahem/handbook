//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ld long double
#define oo (1 << 30)
#define OO (1ll << 60)
#define endl '\n'
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define vi vector<int>
#define f(i, y) for (int i = 0; i < y; i++)
#define fx(i, x, y) for (int i = x; i < y; i++)
#define fd(i, y) for (int i = y - 1; i >= 0; i--)
#define fdx(i, x, y) for (int i = y; i >= x; i--)
#define FOR(it, A) for (typeof A.begin() it = A.begin(); it != A.end(); it++)
#define pii pair<int, int>
#define pil pair<int, long long>
#define sz(v) (int)v.size()
#define watch(x) cerr << (#x) << "= " << (x) << endl;
#define watcharr(a)                        \
    cerr << (#a) << "(" << sz(a) << ")= "; \
    rep(i, sz(a)) cerr << a[i] << ",";     \
    cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
const int INF = 0x3f3f3f3f;
const int N = 2010;
using namespace std;

string isBalanced(string s) {
    stack<char> brackers_stack;
    map<char, char> brackers_map;
    brackers_map[']'] = '[';
    brackers_map[')'] = '(';
    brackers_map['}'] = '{';
    for(int i = 0; i < s.length(); i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            brackers_stack.push(s[i]);
        }
        else {
            if (brackers_stack.empty()) return "NO";
            int top = brackers_stack.top();
            if (brackers_map[s[i]] == top) {
                brackers_stack.pop();
            }
            else {
                return "NO";
            }
        }
    }
    if (brackers_stack.size() > 0) return "NO";
    return "YES";
}

int main()
{
    FASTIO;
    int n;
    cin>>n;
    f(i,n) {
        string s;
        cin>>s;
        cout<<isBalanced(s)<<endl;
    }
    return 0;
}
