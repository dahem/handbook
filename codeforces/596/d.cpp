//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll unsigned long long int
#define ld long double
#define endl '\n'
#define F first
#define S second
#define pb push_back
#define mp make_pair
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

const ll INF = 1e10;
const int N = 1e5 + 5;
using namespace std;

int mpf[N + 1]; // minimum prime factor
vector<int> primes;
int n, k;
int a[N]; //data
int h[N]; //histogram
ll ans = 0;
vector<pii> pFactors;
ll ipowk;

void linearSieve()
{
  memset(mpf, 0, (N) * sizeof(int));
  fx(i, 2, N)
  {
    if (mpf[i] == 0)
    {
      mpf[i] = i;
      primes.push_back(i);
    }
    for (int j = 0; j < (int)primes.size() && primes[j] <= mpf[i] && i * primes[j] <= N; ++j)
      mpf[i * primes[j]] = primes[j];
  }
}

ll sumDivisors(ll i, ll j)
{
  if (i > 1e5 || j > 1e5)
    return 0ll;
  if (i == j)
    return h[i] * (h[i] - 1ll) / 2ll;

  if (i < j)
    return h[i] * h[j];
  return 0;
}

void findPrimefactors(ll num)
{
  while (num != 1)
  {
    ll primeFactor = mpf[num];
    ll cnt = 0;
    while (num > 1 && num % primeFactor == 0)
    {
      num /= primeFactor;
      ++cnt;
    }
    pFactors.pb(mp(primeFactor, cnt * k));
  }
}

void findDivisors(int indFactor, ll lastDivisor) {
  f(i, pFactors[indFactor].S + 1) {
    if (indFactor + 1 < pFactors.size()) {
      findDivisors(indFactor + 1, lastDivisor);
      lastDivisor *= pFactors[indFactor].F;
    } else {
      if (i > 0) lastDivisor *= pFactors[indFactor].F;
      if (lastDivisor * lastDivisor > ipowk) return;     
      ans += sumDivisors(lastDivisor, ipowk / lastDivisor);
    }
  }
}

int main()
{
  FASTIO;
  linearSieve();
  cin >> n >> k;

  f(i, n)
  {
    cin >> a[i];
    h[a[i]]++;
  }
  int exp = 0;
  ll x, y;
  ans = sumDivisors(1ll, 1ll);
  fx(i, 2, N)
  {
    ipowk = 1ll;
    exp = 0;
    while (exp < k && ipowk < INF)
    {
      ipowk *= i;
      exp++;
    }
    if (exp < k)
      break;
    pFactors.clear();
    findPrimefactors(i);
    findDivisors(0, 1);
  }
  cout << ans << endl;
  return 0;
}