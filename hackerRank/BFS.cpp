#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#define N 1010
#define oo (1 << 30)
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define pii pair<int, int>
#define FASTIO std::ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);

using namespace std;

class Graph {
    private: 
        bool visited[N];
        int distance[N];
        vector<pii> adyList[N];
        int n;
    public:
        Graph(int _n) : n(_n) {
        }

        void init() {
            for(int i = 0; i < n+1; i++) {
                distance[i] = oo;
                visited[i] = 0;
            }
        }
    
        void add_edge(int u, int v) {
            adyList[u].PB(MP(6, v));
            adyList[v].PB(MP(6, u));
        }
    
        vector<int> shortest_reach(int start) {
            int adjacent, cost, current;
            init();
            priority_queue<pii, vector<pii>, greater<pii> > Q;
            distance[start] = 0;
            Q.push(MP(distance[start], start));
            while (!Q.empty())
            {
                current = Q.top().S;
                Q.pop();

                if (visited[current]) continue;
                visited[current] = 1;
                
                for (int i = 0; i < adyList[current].size(); i++) {
                    adjacent = adyList[current][i].S;
                    cost = adyList[current][i].F;
                    if (visited[adjacent]) continue;
                    if (distance[current] + cost < distance[adjacent]) {
                        distance[adjacent] = distance[current] + cost;
                        Q.push(MP(distance[adjacent], adjacent));
                    }
                }
            }
            vector<int> result; 
            for(int i = 0; i < n + 1; i++) {
                if (distance[i] != oo) {
                    result.PB(distance[i]);
                }
                else {
                    result.PB(-1);
                }
            }
            return result;
        }
    
};

int main() {
    FASTIO;
    int queries;
    cin >> queries;
        
    for (int t = 0; t < queries; t++) {
      
		int n, m;
        cin >> n;
        // Create a graph of size n where each edge weight is 6: 
        Graph graph(n);
        cin >> m;
        // read and set edges
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            // u--, v--;
            // add each edge to the graph
            graph.add_edge(u, v);
        }
		int startId;
        cin >> startId;
        // startId--;
        // Find shortest reach from node s
        vector<int> distances = graph.shortest_reach(startId);

        for (int i = 1; i < n + 1; i++) {
            if (i != startId) {
                cout << distances[i] << " ";
            }
        }
        cout << endl;
    }
    
    return 0;
}

