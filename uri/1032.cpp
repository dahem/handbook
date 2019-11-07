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
#define watcharr(a)                        \
    cerr << (#a) << "(" << sz(a) << ")= "; \
    rep(i, sz(a)) cerr << a[i] << ",";     \
    cerr << '\n';
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

const ll INF = 1e10;
const int N = 1e5 + 5;
using namespace std;

int mpf[N + 1]; // minimum prime factor
vector<int> primes;

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

int run(int n, int ind)
{
    if (n == 1)
        return 0;
    int k = primes[ind];
    return (run(n - 1, ind + 1) + k) % n;
}

int main()
{
    FASTIO;
    linearSieve();
    int n;
    while (cin >> n && n)
    {
        cout << run(n, 0) + 1 << endl;
    }
    return 0;
}