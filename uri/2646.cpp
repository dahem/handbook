//   ／l、
// （ﾟ､ ｡ ７
// 　l、 ~ヽ
// 　じしf_,)ノ

#include <bits/stdc++.h>
#define MOD 1000000007
#define ll long long
#define ld long double
#define oo (1 << 30)
#define OO (1ll << 60)
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
const int N = 27;
using namespace std;
int n, m;
char a, b;
string cad1, cad2;
vi graph[N];
int vis[N]; 
void dfs(int u) {
    vis[u] = 1;
    f(i, graph[u].size()) {
        if(!vis[graph[u][i]]) {
            dfs(graph[u][i]);
        }
    } 
}

int main()
{
    FASTIO;
    cin>>m>>n;
    f(i,m) {
        cin>>a>>b;
        graph[a-'a'].PB(b-'a');
    }
    
    f(i,n) {
        cin>>cad1>>cad2;
        bool flag = cad1.length() == cad2.length();
        if(flag) {
            f(j,cad1.length()) {
                memset(vis, 0, sizeof(vis));
                dfs(cad1[j]-'a');
                if(!vis[cad2[j]-'a']) {
                    flag = false;
                    break;
                }
            }
        }
        if(flag) cout<<"yes"<<endl;
        else cout<<"no"<<endl;
    }
    return 0;
}
