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
#define watcharr(a)                        \
    cerr << (#a) << "(" << sz(a) << ")= "; \
    rep(i, sz(a)) cerr << a[i] << ",";     \
    cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
const int INF = 0x3f3f3f3f;
const int N = 10010;
using namespace std;
ll cases, n, item, m;
ll sets[N];
ll num;
int main()
{
    FASTIO;

    cin >> cases;
    f(cas, cases)
    {
        cin >> n;
        f(i, n)
        {
            cin >> m;
            num = 0ll;
            f(j, m)
            {
                cin >> item;
                num |= 1ll << (item - 1ll);
            }
            sets[i] = num;
            // cout<<"dd"<<num<<endl;
        }
        // f(i,n){
        //     cout<<sets[i]<<endl;
        //     cout<<__builtin_popcountll(sets[i])<<endl;
        // }
        int q;
        int op;
        int a, b;
        cin >> q;
        f(i, q)
        {
            cin >> op >> a >> b;
            if (op == 1)
            {
                cout << __builtin_popcountll(sets[a - 1] & sets[b - 1]) << endl;
            }
            else
            {
                cout << __builtin_popcountll(sets[a - 1] | sets[b - 1]) << endl;
            }
        }
    }
}