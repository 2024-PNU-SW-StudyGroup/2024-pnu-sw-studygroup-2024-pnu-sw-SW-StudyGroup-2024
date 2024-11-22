#include <stdio.h>

int main(void)
{
	int n;
	int sum = 0;
	while(1)
	{
		scanf("%d", &n);
		if(n == -1) break;
		
		for(int i = 1; i < n; i++) if(n % i == 0) sum += i;
		
		if(sum == n)
		{
			printf("%d = ", sum);
			for(int i = 1; i < n; i++) if(n % i == 0) printf(i != n-i ? "%d + " : "%d", i);
			printf("\n");
		}
		else printf("%d is NOT perfect.\n", n);
		
		sum = 0;
	}
	
	return 0;
}
