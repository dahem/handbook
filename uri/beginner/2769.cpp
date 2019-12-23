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
const int N = 1010;
using namespace std;
int n;

int arr[N][2];
int dp[N][2];
int pass[N][2];
int main()
{
    FASTIO;
    
    while(cin>>n) {
        cin>>arr[0][0]>>arr[0][1];
        dp[0][0] = arr[0][0];
        dp[0][1] = arr[0][1];
        fx(i,1,n+1) {
            cin>>arr[i][0];
        }
        fx(i,1,n+1) {
            cin>>arr[i][1];
        }
        pass[0][0] = oo;
        pass[0][1] = oo;
        fx(i,1, n) {
            cin>>pass[i][0];
        }
        fx(i,1, n) {
            cin>>pass[i][1];
        }
        
        cin>>arr[n+1][0]>>arr[n+1][1];
        
        pass[n][0] = oo;
        pass[n][1] = oo;
        int cost = 0;
        fx(i, 1, n+2) {
            dp[i][0] = min(dp[i-1][0], dp[i-1][1] + pass[i-1][1]) + arr[i][0];
            dp[i][1] = min(dp[i-1][1], dp[i-1][0] + pass[i-1][0]) + arr[i][1];
        }
        cout<<min(dp[n+1][0], dp[n+1][1])<<endl;
    }
    return 0;
}
