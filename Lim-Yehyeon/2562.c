#include <stdio.h>

int main(void)
{
	int arr[9];
	for(int i = 0; i < 9; i++)
	{
		scanf("%d", &arr[i]);
	}
	int max, index;
	max = arr[0];
	index = 1;
	for(int i = 1; i < 9; i++)
	{
		if(max < arr[i]){
			max = arr[i];
			index = i + 1;
		}
	}
	printf("%d\n%d", max, index);
}
