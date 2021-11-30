#include <stdio.h>
#include <string.h>

char concatenare(char rez[],char s1[], char s2[],int lungime);

int main()
{
    char s1[101];
    char s2[101];
    char rez[202];
    scanf("%s",s1);
    scanf("%s",s2);
    int lungime = strlen(s1);
    concatenare(rez,s1,s2,lungime);
    printf("Rezultatul primei concatenari este: ");
    for(int i=0;i<lungime*2;i++)
        printf("%c",rez[i]);
    printf("\n");
    printf("Rezultatul celei de a doua concatenari este: ");
    for(int i=0;i<lungime*2;i++)
        printf("%c",rez[i+lungime*2]);
    return 0;
}
