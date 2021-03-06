//   ／l、
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
#define watcharr(a)                      \
  cerr << (#a) << "(" << sz(a) << ")= "; \
  rep(i, sz(a)) cerr << a[i] << ",";     \
  cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
const int INF = 0x3f3f3f3f;
const int N = 1000010;
using namespace std;
ll A[N];
int S[N];
int main()
{
    FASTIO;
    int n;
    cin>>n;
    memset(A, 0, n);
    memset(S, 0, n);
    f(i,n){
        cin>>A[i];
    }
    int i = 0;
    while(i >= 0 && i < n) {
        S[i] = 1;
        if (A[i]%2 == 1) {
            if(A[i]>0) {
                A[i]--;
            }
            i++;
        } else {
            if(A[i]>0) {
                A[i]--;
            }
            i--;
        }
    }
    int stars = 0;
    ll acum = 0;
    f(i,n) {
        stars += S[i];
        acum += A[i]; 
    }
    cout<<stars<<" "<<acum<<endl;
  return 0;
}