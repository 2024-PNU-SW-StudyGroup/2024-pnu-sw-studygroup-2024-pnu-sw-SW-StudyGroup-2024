#include <stdio.h>

int main(void)
{
	int m, n;
	int sum = 0;
	int min = 0;
	scanf("%d", &m);
	scanf("%d", &n);
	
	for(int i = m; i <= n; i++)
	{
		int count = 0;
		if(i == 1) continue;
		for(int j = 2; j < i; j++)
		{
			if(i % j == 0)
			{
				count = 1;
				break;
			}
		}
		if(count == 0)
		{
			if(min == 0) min = i;
			sum += i;
		}
	}
	if(sum != 0) printf("%d\n%d", sum, min);
	else printf("-1");
	
	return 0;
}
