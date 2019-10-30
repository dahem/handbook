//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define ll long long
#define endl '\n'
#define f(i, y) for (int i = 0; i < y; i++)
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

using namespace std;

ll binpow(ll a, ll b, ll mod)
{
  a %= mod;
  ll res = 1;
  while (b > 0)
  {
    if (b & 1)
      res = res * a % mod;
    a = a * a % mod;
    b >>= 1;
  }
  return res;
}

int main()
{
  FASTIO;
  int cases,x,y;
  cin>>cases;
  f(i, cases)
  {
    cin>>x>>y;
    cout << binpow(x, y, 10) << endl;
  }
  return 0;
}