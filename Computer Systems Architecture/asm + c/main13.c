#include <stdio.h>
#include <string.h>

int minim(int a, int b)
{
    if(a < b)
        return a;
    return b;

}

char rasturnare(char s[])
{
    int i,l=strlen(s);
    char aux;
    for(i=0;i<l/2;i++)
    {
        aux = s[i];
        s[i] = s[l-i-1];
        s[l-i-1] = aux;
    }
    //return s;
}

char cautaresufix(char rezultat[],char s1[],char s2[],int lungime_minima,int ls1,int ls2);

int main()
{
    char s1[101] = "dab";
    char s2[101] = "cab";
    char s3[101] = "aab";
    int lungime_minima;
    char rezultat[101];
    //scanf("%s",s1);
    int ls1 = strlen(s1);
    //scanf("%s",s2);
    int ls2 = strlen(s2);
    //scanf("%s",s3);
    int ls3 = strlen(s3);
    
    // Ne ocupam de s1 cu s2
    lungime_minima = minim(ls1,ls2);
    cautaresufix(rezultat,s1,s2,lungime_minima,ls1-1,ls2-1);
    rezultat[strlen(rezultat)] = NULL;
    rasturnare(rezultat);
    printf("Sufixul maxim comun sirului 1 si 2 este %s \n",rezultat);
    
    // Ne ocupam de s1 cu s3
    lungime_minima = minim(ls1,ls3);
    cautaresufix(rezultat,s1,s3,lungime_minima,ls1-1,ls3-1);
    rezultat[strlen(rezultat)] = NULL;
    rasturnare(rezultat);
    printf("Sufixul maxim comun sirului 1 si 3 este %s \n",rezultat);
    
    // Ne ocupam de s2 cu s3
    lungime_minima = minim(ls2,ls3);
    cautaresufix(rezultat,s2,s3,lungime_minima,ls2-1,ls3-1);
    rezultat[strlen(rezultat)] = NULL;
    rasturnare(rezultat);
    printf("Sufixul maxim comun sirului 2 si 3 este %s",rezultat);
    
    return 0;
}