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

int n, m;
int a, b;
int dp[N];
vector<pii> v;

int run(int val) {
    if (val == 0) return 0;
    if (val < 0) return -oo; 
    if (dp[val] != -1) return dp[val];

    int maxi = -oo;
    int ind = -1;
    f(i, n) {
        int nexVal = v[i].S + run(val - v[i].F);
        if(maxi < nexVal) {
            maxi = nexVal; 
            ind = i;
        }
    }

    // if(ind > -1) {
    //     cout<<v[ind].F<<" "<<v[ind].S<<endl;
    // } else {
    //     cout<<"negative"<<endl;
    // }
    return dp[val] = maxi;
}

int main()
{
    FASTIO;
    int ind = 0;
    while(cin>>n>>m) {
        ind++;
        memset(dp, -1, sizeof(dp));
        v.clear();
        f(i,n) {
            cin >> a >> b;
            v.PB(MP(a,b));
        } 
        cout<<run(m)<<endl;

    }
    return 0;
}
