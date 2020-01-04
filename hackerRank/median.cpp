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
const int N = 2010;
using namespace std;


int main()
{
    
    FASTIO;
    priority_queue<double> left;
    priority_queue<double, vector<double>, greater<double> > right;
    int n;
    double num;
    cin>>n;
    double median = 0.0;
    f(i, n) {
        cin>>num;
        if(i == 0) {
            median = num;
            right.push(num);
            printf("%.1lf\n", median);
            continue;
        }
        
        if (left.size() > right.size()) {
            if (num > median) {
                right.push(num);
            } else {
                right.push(left.top());
                left.pop();
                left.push(num);
            }
            median = (left.top() + right.top()) / 2.0;
        }
        else if (left.size() < right.size()) {
            if (num < median) {
                left.push(num);
            } else {
                left.push(right.top());
                right.pop();
                right.push(num);
            }
            median = (left.top() + right.top()) / 2.0;
        }
        else {
            if (num < median) {
                left.push(num);
                median = left.top();
            } else {
                right.push(num);
                median = right.top();
            }
        }
        
        printf("%.1lf\n", median);
    }
    return 0;
}
