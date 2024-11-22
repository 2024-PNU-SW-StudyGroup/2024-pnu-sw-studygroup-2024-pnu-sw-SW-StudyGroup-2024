#include <stdio.h>

int main(void)
{
	int x, n;
	scanf("%d", &x);
	scanf("%d", &n);
	
	int sum = 0;
	for(int i = 1; i<=n; i++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		sum += a*b;
	}
	
	if(x == sum){
		printf("Yes");
	}
	else printf("No");
}
