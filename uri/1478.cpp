// def pp(arr):
//     sol = []
//     for x in arr:
//         if x < 10:
//             sol.append("  "+str(x))
//             continue
//         if x < 99:
//             sol.append(" "+str(x))
//             continue
//         if x == 100:
//             sol.append(str(x))
//     return sol

// while(True):
//     n = int(input())
//     if n == 0:
//         break
//     mat = [[0 for y in range(n)] for x in range(n)]
//     for x in range(n):
//         for y in range(n):
//             mat[x][y] = max(x,y) - min(x,y) + 1

//     for x in mat:
//         print(" ".join(pp(x)))
    
//     print("")
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
int main()
{
  FASTIO;

  while(cin>>n && n) {
      f(i,n) {
          f(j,n) {
              if (j>0) printf(" ");
              int val = max(i,j) - min(i,j) + 1;
              printf("%3hd", val);
          }
          printf("\n");
      }
      printf("\n");
  }
  return 0;
}