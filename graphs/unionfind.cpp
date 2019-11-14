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
#define N 100005
using namespace std;


int padre[N];
int rango[N];
int root[N];
int numVertices[N];
int numComponentes;
void MakeSet( int n ){
    for( int i = 0 ; i < n ; ++i ){
        padre[ i ] = i;
        rango[ i ] = 0;
    }
}

int Find( int x ){
    if( x == padre[ x ] ){ 
        return x;
    }
    else return padre[ x ] = Find( padre[ x ] );
}

void Union( int x , int y ){
    int xRoot = Find( x );
    int yRoot = Find( y ); 
    padre[ xRoot ] = yRoot;
}

void UnionbyRank( int x , int y ){
    int xRoot = Find( x ); 
    int yRoot = Find( y );
    if( rango[ xRoot ] > rango[ yRoot ] ){ 
       padre[ yRoot ] = xRoot;
    }
    else{ 
        padre[ xRoot ] = yRoot; 
        if( rango[ xRoot ] == rango[ yRoot ] ){ 
            rango[ yRoot ]++; 
        }
    }
}

int getNumberConnectedComponents( int n ){
    numComponentes = 0;
    for( int i = 0 ; i < n ; ++i ){
        if( padre[ i ] == i ){ 
            root[ numComponentes++ ] = i;
        }
    }
    return numComponentes;
}

void getNumberNodes( int n ){
    memset( numVertices , 0 , sizeof( numVertices ) );
    for( int i = 0 ; i < n ; ++i ){
        numVertices[ Find( i ) ]++;
    }
    for( int i = 0 ; i < numComponentes ; ++i ){
        printf("Componente %d: Raiz = %d , Nro nodos = %d.\n" , i + 1 , root[ i ] , numVertices[ root[ i ] ] );
    }
}

bool sameComponent( int x , int y ){
    if( Find( x ) == Find( y ) ) return true; 
    return false;
}

int n,m,q;
int u,v;
int qu,qv;
int main()
{
  FASTIO;
  int wasPrint = false;
  while(cin>>n>>m>>q) {
      if (wasPrint) cout<<endl;
      wasPrint = true;
      MakeSet(n);
      f(i,m) {
          cin>>u>>v;
          Union(u-1,v-1);
      }
      f(i,q){
          cin>>qu>>qv;
          if (sameComponent(qu-1, qv-1)) cout<<"S"<<endl;
          else cout<<"N"<<endl;
      }
  }
  return 0;
}