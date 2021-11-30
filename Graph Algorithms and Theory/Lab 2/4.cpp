#include <fstream>

using namespace std;

ifstream f("4.in");
ofstream g("4.out");

int graf[101][101];

int exista_nod_nevizitat(int v[101], int n){

    for(int i = 1; i <= n; i++)
        if(v[i] == 0)
            return i;
    
    return 0;
}

void DFS(int v[101][101], int n, int nod_start){

    comp++;

}

int main(){

    int n,x,y,nod_start;
    f>>n;
    while(f>>x>>y){

        graf[x][y] = 1;
        graf[y][x] = 1;

    }

    f>>nod_start;

    g<<"Pornim de la nodul "<<nod_start<<'\n';

    return 0;
}