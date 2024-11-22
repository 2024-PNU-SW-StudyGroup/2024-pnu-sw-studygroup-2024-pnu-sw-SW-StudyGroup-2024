#include <stdio.h>
#include <string.h>

int main(void)
{
	int n, group, count = 0;
	char word[100];
	
	scanf("%d", &n);
	
	for(int i = 0; i < n; i++)
	{
		scanf("%s", &word);
		group = 1;
		for(int j = 0; j < strlen(word); j++)
		{
			for(int k = 0; k < j - 1; k++)
			{
				if(word[j] == word[k] && word[j] != word[j-1])
				{
					group = 0;
					break;
				}
			}
			if(group == 0) break;
		}
		if(group == 1) count++;
	}
	printf("%d", count);
	
	return 0;
}
