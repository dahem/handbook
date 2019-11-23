//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ld long double
#define oo 1 << 30
#define OO 1ll << 60
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

vector<pii> graph[N];
int dis[N];
int n, m;

void Dijkstra(int source)
{
    int v, uv, u, du;
    priority_queue<pii, vector<pii>, greater<pii> > pq;
    fx(i,1, n+1) dis[i] = oo;

    dis[source] = 0;
    pq.push(MP(source, 0));

    while (pq.size())
    {
        u = pq.top().F;
        du = pq.top().S;
        pq.pop();

        if (du != dis[u]) continue;

        f(i,graph[u].size()) {
            v = graph[u][i].F;
            uv = graph[u][i].S;
            if (dis[v] > dis[u] + uv) {
                dis[v] = dis[u] + uv;
                pq.push(MP(v, dis[v]));
            }
        }
    }
}

int main()
{
    FASTIO;
    cin >> n >> m;
    int u, v, source;
    ll cost;
    f(i, m)
    {
        cin >> u >> v >> cost;
        graph[u].PB(MP(v, cost));
        graph[v].PB(MP(u, cost));
    }
    cin >> source;
    Dijkstra(source);
    int mini = oo;
    int maxi = 0;
    fx(i, 1, n+1)
    {
        if (i != source)
        {
            mini = min(mini, dis[i]);
            maxi = max(maxi, dis[i]);
        }
    }
    cout << maxi - mini << endl;
    return 0;
}
