#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
	int n, b;
	char output[101];
	scanf("%d %d", &n, &b);
	int i = 0;
	
	while(n > 0)
	{
		int cal = n % b;
		if(cal >= 10) output[i] = cal + 55;
		else output[i] = cal + 48;
		i++;
		n /= b;
	}
	
	for(int j = i - 1; j >= 0; j--) printf("%c", output[j]);
		
	return 0;
}
