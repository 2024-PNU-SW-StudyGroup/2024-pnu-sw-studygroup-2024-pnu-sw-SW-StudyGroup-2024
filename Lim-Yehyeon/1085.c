#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int x, y, w, h;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	
	int output1, output2;
	
	if(x > abs(w-x)) output1 = abs(w-x);
	else output1 = x;
	
	if(y > abs(y-h)) output2 = abs(y-h);
	else output2 = y;
	
	if(output1 > output2) printf("%d", output2);
	else printf("%d", output1);
	
	return 0;
}
