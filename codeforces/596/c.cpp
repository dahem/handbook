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
#define N 200010
const int INF = 0x3f3f3f3f;

using namespace std;
int arr[N];
map<int, int> mapNum;

int main()
{
  FASTIO;
  int t, n, k, d;
  cin >> t;

  f(s, t)
  {
    // watch(s);
    cin >> n >> k >> d;
    int sol;
    mapNum.clear();
    f(i, n)
    {
      cin >> arr[i];
    }

    fx(i, 0, d)
    {
      if (mapNum.count(arr[i]))
      {
        mapNum[arr[i]]++;
      }
      else
      {
        mapNum[arr[i]] = 1;
      }
    }

    // for (map<int, int>::iterator it = mapNum.begin(); it != mapNum.end(); ++it)
    //   cout << it->first << " => " << it->second << '\n';
    sol = (int)mapNum.size();
    // watch(sol);
    int start = 0;
    fx(i, d, n)
    {
      if (mapNum[arr[start]] > 1)
      {
        mapNum[arr[start]]--;
      }
      else
      {
        mapNum.erase(arr[start]);
      }
      if (mapNum.count(arr[i]))
      {
        mapNum[arr[i]]++;
      }
      else
      {
        mapNum[arr[i]] = 1;
      }
      // if (sol > mapNum.size())
      // {

      //   cout << "size" << mapNum.size() << endl;
      //   cout << start + 1 << " " << i << endl;
      //   for (map<int, int>::iterator it = mapNum.begin(); it != mapNum.end(); ++it)
      //     cout << it->first << " => " << it->second << '\n';
      // }
      sol = min(sol, (int)mapNum.size());

      start++;
    }
    cout << sol << endl;
  }
  return 0;
}