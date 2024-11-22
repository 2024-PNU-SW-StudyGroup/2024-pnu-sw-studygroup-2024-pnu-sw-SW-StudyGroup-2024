#include <stdio.h>

int main(void)
{
	int n, k, output;
	int count = 0;
	scanf("%d %d", &n, &k);
	
	for(int i = 1; i <= n; i++)
	{
		if(n % i == 0) count++;
		
		if(count == k)
		{
			output = i;
			break;
		}
	}
	
	if(count == 0) printf("0");
	else printf("%d", output);
	
	return 0;
}
