// print("A = %.1f, B = %.1f" % (a, b))
// print("C = %.1f, D = %.1f" % (c, d))

// print("A = %.2f, B = %.2f" % (a, b))
// print("C = %.2f, D = %.2f" % (c, d))

// print("A = %.3f, B = %.3f" % (a, b))
// print("C = %.3f, D = %.3f" % (c, d))

// print("A = %.3E, B = %.3E" % (a, b))
// print("C = %.3E, D = %.3E" % (c, d))

// print("A = %.0f, B = %.0f" % (a, b))
// print("C = %.0f, D = %.0f" % (c, d))

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

int main()
{
    FASTIO;
    float a,b;
    double c,d;
    cin>>a>>b;
    cin>>c>>d;
    printf("A = %.6f, B = %.6f\n", a, b); 
    printf("C = %.6f, D = %.6f\n", c, d); 
    printf("A = %.1f, B = %.1f\n", a, b); 
    printf("C = %.1f, D = %.1f\n", c, d); 
    printf("A = %.2f, B = %.2f\n", a, b); 
    printf("C = %.2f, D = %.2f\n", c, d); 
    printf("A = %.3f, B = %.3f\n", a, b); 
    printf("C = %.3f, D = %.3f\n", c, d); 
    printf("A = %.3E, B = %.3E\n", a, b); 
    printf("C = %.3E, D = %.3E\n", c, d); 
    printf("A = %.0f, B = %.0f\n", a, b); 
    printf("C = %.0f, D = %.0f\n", c, d); 
    return 0;
}
