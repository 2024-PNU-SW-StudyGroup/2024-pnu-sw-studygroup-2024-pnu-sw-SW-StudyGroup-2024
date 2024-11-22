#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
	char input[1000000];
	int b;
	int output = 0;
	
	scanf("%s %d", &input, &b);
	
	for(int i = 0; i < strlen(input); i++)
	{
		int digit;
		if(input[i] >= 48 && input[i] <= 57) digit = input[i] - 48;
		else if(input[i] >= 65 && input[i] <= 90) digit = input[i] - 65 + 10;
		output += digit * pow(b, strlen(input) - 1 -i);
	}
	
	printf("%d", output);
	
	return 0;
}
