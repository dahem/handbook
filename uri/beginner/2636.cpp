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

using namespace std;
int base[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};

ll gcd(ll a, ll b)
{
	while (b) { a %= b; swap(a, b);}
	return a;
}
// Multiply caring overflow
ll mulmod(ll a, ll b, ll m=MOD) {
  ll r=0;
  for (a %= m; b; b>>=1, a=(a*2)%m) if (b&1) r=(r+a)%m;
  return r;
}

// Fast exponential
ll fexp(ll a, ll b, ll m=MOD) {
  ll r = 1;
  for (a %= m; b; b>>=1, a=(a*a)%m) if (b&1) r=(r*a)%m;
  return r;
}

// Miller-Rabin - Primarily Test
bool miller(ll n, ll a) {
    if (!(n & 1)) return 0;
    ll d = n - 1;
    ll s = 0; 
    while (!(d & 1) && d) d >>= 1, s++;
    ll x = fexp(a, d, n);

    if (x == 1 || x == n-1) return 1;
    f(r,s) {
        x = mulmod(x,x,n);
        if (x == 1) return 0;
        if (x == n-1) return 1;
    }
    return 0;
}

bool isprime(ll n) {
    if (n == 1 || n == 4) return 0;
    if (n == 2 || n == 3) return 1;
    f(i,12) if (n > base[i] && !miller(n, base[i])) return 0;
    return 1;
}

ll pollard(ll n) {
    ll x, y, d, c = -1;
    if (!(n&1)) return 2;
    while(1) {
        y = x = 2;
        while(1) {
            x = mulmod(x, x, n); x = (x - c) %n;
            y = mulmod(y, y, n); y = (y - c) %n;
            y = mulmod(y, y, n); y = (y - c) %n; 
            d = gcd(abs(n+ y - x), n);
            if (d == n) break;
            if (d > 1) return d;
        }
        c--;
    }
}

ll n;
vector<ll> sol;

void run(ll n) {
    if(isprime(n)) {
        sol.PB(n);
        return ;
    }
    ll factor = pollard(n);
    run(factor);
    run(n / factor);
}

int main()
{
  FASTIO;
  while (cin>>n && n) {
      sol.clear();
      run(n);
      assert(sol.size() == 3);
      sort(sol.begin(), sol.end());
      cout<<n<<" = "<<sol[0]<<" x "<<sol[1]<<" x "<<sol[2]<<endl;
  }
  return 0;
}