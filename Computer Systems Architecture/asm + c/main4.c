#include <stdio.h>

int hexa(int a);
int binar(int b,int v[]);

int main()
{
    // declaram variabilele
    int sir[101] = {10,20,30,2,4,6,8};
	printf("Sir in baza 16 : ");
	for(int i=0;i<7;i++)
	{
		hexa(sir[i]);
	}
	
	printf("\n");
	printf("Sir in baza 2 : ");
	
	for(int i=0;i<7;i++)
	{
		int v[101];
		binar(sir[i],v);
		int j=0;
		while(v[j]!=2)
			j++;
		j--;
		for (j;j>=0;j--)
			printf("%d", v[j]);
		printf("b ");
	}
 
    return 0;
}