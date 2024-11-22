#include <stdio.h>
#include <string.h>

int main(void)
{
	int max, result = 0, len;
	char word[1000000];
	int alpha[26] = {0};
	int select = 0;
	
	scanf("%s", &word);
	len = strlen(word);
	
	for(int i = 97; i <= 122; i++)
	{
		for(int j = 0; j < len; j++)
		{
			if(i == word[j]) alpha[i - 97]++;
		}
	}
	for(int i = 65; i <= 90; i++)
	{
		for(int j = 0; j < len; j++)
		{
			if(i == word[j]) alpha[i - 65]++;
		}
	}
	
	max = alpha[0];
	for(int i = 1; i < 26; i++)
	{
		if(max < alpha[i])
		{
			max = alpha[i];
			select = i;
		}
	}
	
	for(int i = 0; i < 26; i++)
	{
		if(max == alpha[i]) result++;
	}
	if(result > 1) printf("?");
	else printf("%c", select + 65);
	
	return 0;
}
