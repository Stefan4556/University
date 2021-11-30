#include <fstream>
using namespace std;
int graf[101][101];
int adiacenta[101][101];
int incidenta[101][101];
ifstream f("graf.in");
ofstream g("graf.out");
int main()
{
    int n,x,y,i,j,k,nr_muchii=0;
    f>>n;
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            graf[i][j]=0;
    
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            adiacenta[i][j]=0;
    
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            incidenta[i][j]=0;
    
    while(f>>x>>y)
    {
        graf[x-1][y-1]=1;
        graf[y-1][x-1]=1;
        nr_muchii++;
    }

    // Matricea de adiacenta - de la muchii
    g<<"Matricea de adiacenta este: \n";
    for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                g<<graf[i][j]<<" ";
            g<<"\n";
        }

    // Lista adiacenta - venim de la matricea de adiacenta
    g<<"\nLista de adiacenta este: \n";
    for(i=0;i<n;i++)
    {   
        k = 0;
        for(j=0;j<n;j++)
            if(graf[i][j]==1)
                {
                    adiacenta[i][k] = j+1;  
                    k++;
                }
    }

    for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                g<<adiacenta[i][j]<<" ";
            g<<"\n";
        }

    // matricea de incidenta - venim de la lista de adiacenta
    g<<"\nMatricea de incidenta este: \n";
    int coloana_curenta = 0;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            if(adiacenta[i][j]!=0 && i<adiacenta[i][j])
                {
                    incidenta[i][coloana_curenta]=1;
                    incidenta[adiacenta[i][j]-1][coloana_curenta]=1;
                    coloana_curenta++;
                }
    }

    for(i=0;i<n;i++)
    {
        for(j=0;j<nr_muchii;j++)
            g<<incidenta[i][j]<<" ";
        g<<'\n';
    }

    // lista adiacenta - venim de la matricea de incidenta
    g<<"\nLista de adiacenta este: \n";

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            adiacenta[i][j]=0;
    
    for(j=0;j<nr_muchii;j++)
    {   
        int x=0,y=0;
        for(i=0;i<n;i++)
            if(incidenta[i][j] == 1 && x==0)
                x = i;
            else if(incidenta[i][j] == 1 && y==0)
                y = i;
        
        for(int jj=0;jj<n;jj++)
            if(adiacenta[x][jj]==0)
            {
                adiacenta[x][jj] = y+1;
                break;
            }

        for(int jj=0;jj<n;jj++)
            if(adiacenta[y][jj] == 0)
            {
                adiacenta[y][jj] = x+1;
                break;
            }
    }

    for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                g<<adiacenta[i][j]<<" ";
            g<<"\n";
        }

    // matricea de adiacenta - venim de la lista adiacenta
    g<<"\nMatricea de adiacenta este: \n";

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            graf[i][j]=0;
    
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(adiacenta[i][j]!=0)
                graf[i][adiacenta[i][j]-1] = 1;
    
    for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
                g<<graf[i][j]<<" ";
            g<<"\n";
        }

    // matricea de incidenta - venim din matricea de adiacenta
    g<<"\nMatricea de incidenta este: \n";

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            incidenta[i][j]=0;
    
    coloana_curenta = 0;

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(i<j && graf[i][j]==1)
            {
                incidenta[i][coloana_curenta] = 1;
                incidenta[j][coloana_curenta] = 1;
                coloana_curenta++;
            }
    
    for(i=0;i<n;i++)
    {
        for(j=0;j<nr_muchii;j++)
            g<<incidenta[i][j]<<" ";
        g<<'\n';
    }

    return 0;
}