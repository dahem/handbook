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
