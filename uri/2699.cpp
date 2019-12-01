//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ld long double
#define oo 1 << 30
#define OO 1ll << 60
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
const int N = 1010;

using namespace std;

int dp[N][N];
int n;
string cad;
string sol;
int len;
int mod;

int solve(int idx, int val) {
    if (idx == len) return val == 0;
    if (dp[idx][val] != -1) return dp[idx][val];
    if (cad[idx] != '?') return solve(idx + 1, (val * 10 + cad[idx] - '0') % mod);
    int i = 0;
    if (idx == 0) i++;
    for (; i <= 9; i++) {
        if (solve(idx + 1, (val * 10 + i) % mod)) {
            sol[idx] = i + '0';
            return dp[idx][val] = 1;
        }
    }
    return dp[idx][val] = 0;
}

int main()
{
    FASTIO;
    cin>>cad>>mod;
    sol = cad;
    len = cad.length();
    memset(dp, -1, sizeof(dp));
    if (solve(0,0)) {
        cout<<sol<<endl;
    } else {
        cout<<'*'<<endl;
    }
    return 0;
}
