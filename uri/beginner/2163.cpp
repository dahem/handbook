//  ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ld long double
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
int n, m;
int mat[N][N];
int X[] = {1, 1, 0, -1, -1, -1, 0, 1};
int Y[] = {0, 1, 1, 1, 0, -1, -1, -1};
bool imposible;
int main()
{
    FASTIO;
    cin>>n>>m;
    f(i,n)f(j,m) cin>>mat[i][j];
    fx(i,1,n-1) fx(j,1,m-1) {
        if (mat[i][j] != 42) continue;
        imposible = false;
        f(k,8) {
            if (mat[i + X[k]][j + Y[k]] != 7) {
                imposible = true;
                break;
            }
        }
        if (imposible) continue;
        cout<<i+1<<" "<<j+1<<endl;
        return 0;
    }
    cout<<"0 0"<<endl;
    return 0;
}