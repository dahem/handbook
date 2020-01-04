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
#define clear(arr, val) memset(arr, val, sizeof arr)
#define watch(x) cerr << (#x) << "= " << (x) << endl;
#define watcharr(a)                        \
    cerr << (#a) << "(" << sz(a) << ")= "; \
    rep(i, sz(a)) cerr << a[i] << ",";     \
    cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
const int INF = 0x3f3f3f3f;
const int N = 610;
using namespace std;

int mat[N][N];
int dp[N][N];
pii dims[N][N];
bool check[N][N][N]

// check sub arr from j - len   to j in row i 
bool checkRow(int i, int j, int len) {
    int last = mat[i][j-len + 1];
    fx(k, j-len + 1, j+1) {
        if (last >= mat[i][k]) {
            last = mat[i][k];
        } else {
            return false;
        }
    }
    return true;
}

int main()
{
    FASTIO;
    while(cin>>n>>m) {
        if (n == 0) break; 
        f(i, n) f(j, m) {
            cin>>mat[i][j];
        }
        dp[0][0] = 1;
        dims[0][0] = MP(1, 1);
        fx,(j, 1, m) {
            if (mat[0][j] <= mat[0][j-1]) {
                dp[0][j] = dp[0][j-1] + 1;
                dims[0][j] = MP(1, dims[0][j-1].S + 1);
            } else {
                dp[0][j] = 1;
                dims[0][j] = MP(1, 1);
            }
        }
        fx,(i, 1, n) {
            if (mat[i][0] <= mat[i-1][0]) {
                dp[i][0] = dp[i-1][0] + 1;
                dims[i][0] = MP(dims[i-1][0].F + 1, 1);
            } else {
                dp[i][0] = 1;
                dims[i][0] = MP(1, 1);
            }
        }
        
        fx(i,1,n) fx(j,1,m) {
            // try best box
            int maxlen = dims[i-1][j].S;
            while(maxlen) {
                if (checkRow(i,j, maxlen) && mat[i][j-]) {
                    break;
                }
                maxlen--;
            }
            
        }
    }
    return 0;
}
