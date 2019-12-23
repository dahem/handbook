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
int vis[N];
int previous[N];
int n, m;

void init() {
    f(i, n+1) {
        dis[i] = oo;
        vis[i] = 0;
        previous[i] = -1;
    }
}

void printPath(int target) {
    if (previous[target] != -1) 
        printPath(previous[target]);
    cout<<target<<" ";
}

void dijkstra(int source)
{
    int adjacent, cost, current;
    init();
    priority_queue<pii, vector<pii>, greater<pii> > pq;
    dis[source] = 0;
    pq.push(MP(dis[source], source));

    while (!pq.empty())
    {
        current = pq.top().S;
        pq.pop();

        if (vis[current]) continue;
        vis[current] = 1;
        
        f(i, graph[current].size()) {
            adjacent = graph[current][i].S;
            cost = graph[current][i].F;
            if (vis[adjacent]) continue;
            if (dis[current] + cost < dis[adjacent]) {
                dis[adjacent] = dis[current] + cost;
                previous[adjacent] = current;
                pq.push(MP(dis[adjacent], adjacent));
            }
        }
    }
}

int main()
{
    FASTIO;
    cin >> n >> m;
    int u, v, source;
    int cost;
    f(i, m)
    {
        cin >> u >> v >> cost;
        graph[u].PB(MP(cost, v));
        graph[v].PB(MP(cost, u));
    }
    cin >> source;
    dijkstra(source);
    fx(i, 1, n+1) cout<<dis[i]<<" ";
    cout<<endl;
    printPath(5);
    return 0;
}
