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
#define OO 1000000000000000000
const int INF = 0x3f3f3f3f;
const int N = 1000010;

using namespace std;
ll A[N];
int n, k;
int main()
{
  FASTIO;
  cin >> n >> k;

  ll fk = 0ll;
  ll b = 0ll;
  ll c = 0ll;
  f(i, n)
  {
    cin >> A[i];
  }

  sort(A, A + n);
  f(i, n){
    b += 2 * (fk - A[i]);
    c += (fk - A[i]) * (fk - A[i]);
    fk += k;
  }
  watch(b);
  watch(c);
  if (n == 1)
  {
    cout << 0 << endl;
  } else {
    ll mini = OO;
    int ind = 0;
    fx(i, 0, 1000000) {
      ll x = n * i * i + b * i + c;
      if (abs(x) < mini){
        mini = abs(x);
        ind = i;
      }
    }

    watch(ind);

    watch(mini);
    ll sol = 0ll;

    f(i, n) {
      sol += abs(ind - A[i]);
      ind += k;
    }

    cout << sol << endl;
  }
  return 0;
}