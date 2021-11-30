#include <stdio.h>

int conversie_string(int v[]);

int main()
{
    int v[101];
    
    conversie_string(v);
    
    for(int i=1;i<=v[0];i++)
        printf("%d ",v[i]);
    
    return 0;
}