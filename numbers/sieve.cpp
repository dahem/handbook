// Sieve of Eratosthenes O(n)
const int N = 10000000;
int lp[N + 1];
vector<int> pr;

void linearSieve()
{
  memset(lp, 0, (N+1) * sizeof(int));
  for (int i = 2; i <= N; ++i)
  {
    if (lp[i] == 0)
    {
      lp[i] = i;
      pr.push_back(i);
    }
    for (int j = 0; j < (int)pr.size() && pr[j] <= lp[i] && i * pr[j] <= N; ++j)
      lp[i * pr[j]] = pr[j];
  }
}

void findPrimefactors(int n)
{
  while (n != 1)
  {
    int ok = 1, pf = spf[n], cnt = 0;
    while (n > 1 && n % pf == 0)
    {
      ok *= pf;
      n /= pf;
      ++cnt;
    }
    v.push_back({cnt * k, pf});
  }
}
