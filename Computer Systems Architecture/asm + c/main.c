#include<stdio.h>
void Transformare(char[10]);
int main()
{int numar,i,sir2[10];
char sir[10][10]={"10100111b","01100011b","00000110b","00101011b"};
numar=4;
for(i=0;i<numar;i++)
    Transformare(sir[i]);
printf("%x ",sir2);
    
return 0;}