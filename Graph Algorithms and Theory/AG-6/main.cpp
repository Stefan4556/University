// g++ -std=c++11 -Wall -g -o pb1.exe pb1.cpp

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

typedef struct var_globale{

    int numar_varfuri;
    int numar_muchii;
    vector<unordered_map<int,int>> lista_adiacenta;
    //int numar_culori;
};

void citeste_fisier(ifstream& f, vector<unordered_map<int,int>> v, int numar_muchii){

    //ifstream f(fisier_input);

    for(int i = 0 ; i < numar_muchii; i++){

        int x,y;
        f >> x >> y;
        v[x][y] = 1;
        v[y][x] = 1;
    }

    f.close();
}

vector<int> colorare_graf(var_globale globals, int &numar_culori){

    numar_culori = 0;
    vector<int> culori_varfuri(globals.numar_varfuri);
    fill(culori_varfuri.begin(), culori_varfuri.end(), -1);

    culori_varfuri[0] = 0;

    numar_culori++;

    for(int i = 1; i < globals.numar_varfuri; i++){

        int culoare_curenta = 0;

        unordered_map<int,int> culori_adiacente;

        for(int j = 0 ; j < globals.numar_varfuri; j++){

                if(globals.lista_adiacenta[i][j] == 1){

                    culori_adiacente[culori_varfuri[j]] = 1;
                }
        }

        while(culoare_curenta < numar_culori && culori_adiacente[culoare_curenta] != 0) {

                culoare_curenta++;
        }

        if(culoare_curenta == numar_culori){

            culori_varfuri[i] = culoare_curenta;
            numar_culori++;
        }
        else

            culori_varfuri[i] = culoare_curenta;

    }

    return culori_varfuri;

}

int main(int argc, char** argv) {

    //ifstream f(argv[1]);

    ifstream f("./AG-6/fisier_input.in");

    if(!f.is_open())

        return 2;

    int numar_varfuri = 0, numar_muchii = 0;

    f >> numar_varfuri >> numar_muchii;

    vector<unordered_map<int,int>> v(numar_varfuri + 1);

    citeste_fisier(f, v, numar_muchii);

    var_globale globals;

    globals.numar_muchii = numar_muchii;
    globals.numar_varfuri = numar_varfuri;
    globals.lista_adiacenta = v;
    //globals.numar_culori = 0;

    int numar_culori;

    f.close();

    vector<int> rez = colorare_graf(globals, numar_culori);

    cout << numar_culori << "\n";

    return 0;
}
