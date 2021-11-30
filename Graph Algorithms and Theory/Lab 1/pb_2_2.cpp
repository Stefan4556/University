#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

ifstream f("pb2.txt");

int main(){

    int n,x;
    //vector< vector<int> > a;
    int a[101][101];
    f>>n;
    cout<<n;
    for(int i = 0; i < n; i++)
        for(int j = 0; j  < n; j++){

            f>>x;
            a[i][j] = x;
        }

    for(int k = 0 ; k < n ; ++k)
        for(int i = 0 ; i < n ; ++i)
            for(int j = 0 ; j < n ; ++j)
                if(a[i][j] == 0)
                    a[i][j] = a[i][k] * a[k][j];

    for(int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++)
            cout<<a[i][j]<<" ";
            cout<<'\n';
    }

    return 0;
}