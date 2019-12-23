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
int n;
int lenMax;

string printNumber(int n) {
  string sol = to_string(n);
  while(sol.length() < lenMax){
    sol = ' ' + sol;
  }
  return sol;
}
int main()
{
  FASTIO;

  while(cin>>n && n) {
      int maxNum = pow(2,(n - 1)*2);
      lenMax = to_string(maxNum).length();
      f(i,n) {
          f(j,n) {
              if (j>0) cout<<" ";
              int val = pow(2,i+j);
              cout<<printNumber(val);
          }
          cout<<endl;
      }
      cout<<endl;
  }
  return 0;
}