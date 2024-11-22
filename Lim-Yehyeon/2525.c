#include <stdio.h>

int main(void)
{
	int a, b, c;
	scanf("%d %d", &a, &b);
	scanf("%d", &c);
	
	if(b+c < 60){
		printf("%d %d", a, b+c);
	}
	else{
		int ph = (b+c)/60;
		int pm = (b+c)%60;
		if(a+ph < 24){
			printf("%d %d", a+ph, pm);
		}
		else
			printf("%d %d", a+ph-24, pm);
	}
	
	return 0;
}
