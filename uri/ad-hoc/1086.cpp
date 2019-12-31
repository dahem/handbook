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
#define clr(arr, val) memset(arr, val, sizeof arr)
#define watch(x) cerr << (#x) << "= " << (x) << endl;
#define watcharr(a)                        \
    cerr << (#a) << "(" << sz(a) << ")= "; \
    rep(i, sz(a)) cerr << a[i] << ",";     \
    cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
const int INF = 0x3f3f3f3f;
const int N = 10010;
using namespace std;
int n,m;
int l;
int k;
int arrX[N];
int arrY[N];
set<int> placks;
set<int>::reverse_iterator it;

int check(bool flag) {
    it = placks.rbegin();
    int spaces = flag ? (n*100)/l : (m*100)/l;
    int ans = 0;
    int num, restPlack;
    while(spaces>0 && it != placks.rend()) {
        num = *it;
        // watch(num);
        restPlack = (flag ? m : n) - num;
        if (flag) {
            if (restPlack < 0 || arrX[num] <= 0 || (restPlack == num ? arrX[restPlack] <= 1 : arrX[restPlack] <= 0)) {
                it++;
                continue;
            }    
        } else {
            if (restPlack < 0 || arrY[num] <= 0 || (restPlack == num ? arrY[restPlack] <= 1 : arrY[restPlack] <= 0)) {
                it++;
                continue;
            } 
        }
        
        if (flag) {        
            arrX[num]--;
            arrX[restPlack]--;
        } else {
            arrY[num]--;
            arrY[restPlack]--;
        }
        ans += restPlack > 0 ? 2 : 1;
        spaces--;
    }
    // watch(spaces);
    if (spaces>0) return oo;
    return ans;
}

int main()
{
    FASTIO;
    while(cin>>n>>m) {
        if (n == 0 || m == 0) break;
        cin>>l;
        cin>>k;
        clr(arrX, 0);
        clr(arrY, 0);
        arrX[0] = oo;
        arrY[0] = oo;
        placks.clear();
        int num;
        f(i,k) {
            cin>>num;
            placks.insert(num);
            arrX[num]++;
            arrY[num]++;
        }
        int ans = oo;
        if ((n*100)% l == 0) {
            ans = min(ans, check(1));
        }
        
        if ((m*100)% l == 0) {
            ans = min(ans, check(0));
        }
        
        if (ans >= oo || ans < 0) cout<<"impossivel"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
