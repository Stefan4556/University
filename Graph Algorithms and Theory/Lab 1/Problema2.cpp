#include <fstream>

using namespace std;

ifstream f("graf2.in");
ofstream g("graf2.out");

int graf[101][101];

int matricea_distantelor[101][101];

int main()
{
    int i,j,n,x,y,caz_noduri_izolate=0,ok,k,INF = 99999;
    f>>n;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            graf[i][j] = 0;

    while(f>>x>>y)
    {
        graf[x-1][y-1] = 1;
        graf[y-1][x-1] = 1;
    }

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(i==j)
                matricea_distantelor[i][j] = 0;
            else if(graf[i][j] == 0)
                    matricea_distantelor[i][j] = INF;
                else
                    matricea_distantelor[i][j] = graf[i][j];

    // cerinta a - noduri izolate
    
    g<<"a) Nodurile izolate din graful nostru sunt: ";
    for(i=0;i<n;i++)
    {
        ok = 0;
        for(j=0;j<n;j++)
            if(graf[i][j]==1)
                ok = 1;
        if(ok == 0)
            {
                g<<i+1<<" ";
                caz_noduri_izolate = 1;
            }
    }
    if(caz_noduri_izolate == 0)
    g<<"nu exista";

    // cerinta b - graf regular - fiecare varf are acelasi numar de vecini

    g<<"\nb) Este sau nu este graf regular: ";
    int grad_precedent=0,grad_curent=0;

    for(j=0;j<n;j++)
        if(graf[0][j]!=0)
            grad_precedent++;
    
    ok = 0;
    for(i=1;i<n;i++)
    {
        grad_curent = 0;
        for(j=0;j<n;j++)
            if(graf[i][j]==1)
                grad_curent++;
        if(grad_curent!=grad_precedent)
            {
                ok = 1;
                break;
            }
    }
    if(ok==1)
        g<<"nu este un graf regular\n";
    else 
        g<<"este un graf regular\n";

    // cerinta c - matricea distantelor 

    g<<"c) Matricea distantelor este:\n";
    for(k=0;k<n;k++)
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                if(matricea_distantelor[i][k] != INF && matricea_distantelor[k][j] != INF)
                    if(matricea_distantelor[i][k] + matricea_distantelor[k][j] < matricea_distantelor[i][j])
                        matricea_distantelor[i][j] = matricea_distantelor[i][k] + matricea_distantelor[k][j];
    
    for(i=0;i<n;i++)
    {
        g<<"   ";
        for(j=0;j<n;j++)
            if(matricea_distantelor[i][j] == INF)
                g<<"INF"<<" ";
            else 
                g<<"  "<<matricea_distantelor[i][j]<<" ";
        g<<"\n";
    }

    // cerinta d - este graful conex? - cel mai usor se face cu ceva parcurgere ori in adancime ori in latime

    g<<"d) Este sau nu graful nostru conex? ";

    ok = 0;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(matricea_distantelor[i][j]==INF)
                ok = 1;
    
    if(ok==1)
        g<<"Nu este conex";
    else
        g<<"Este conex";

    return 0;
}