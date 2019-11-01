#define MOD 1000000007
int add(int a, int b)
{
	if (a + b >= MOD)
	{
		return a + b - MOD;
	}
	return a + b;
}

int sub(int a, int b)
{
	if (a - b < 0)
	{
		return a - b + MOD;
	}
	return a - b;
}

int mul(int a, int b)
{
	return 1ll * a * b % MOD;
}

ll binpow(ll a, ll b)
{
	a %= MOD;
	ll res = 1;
	while (b > 0)
	{
		if (b & 1)
			res = res * a % MOD;
		a = a * a % MOD;
		b >>= 1;
	}
	return res;
}

int gcd(int a, int b)
{
	while (b)
	{
		a %= b;
		swap(a, b);
	}
	return a;
}

int lcm(int a, int b)
{
	return a / gcd(a, b) * b;
}

ll binpow(ll a, ll b, ll mod)
{
  a %= mod;
  ll res = 1;
  while (b > 0)
  {
    if (b & 1)
      res = res * a % mod;
    a = a * a % mod;
    b >>= 1;
  }
  return res;
}