// g++ -std=c++11 -Wall -g -o pb1.exe pb1.cpp

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

vector<unordered_map<int,int>> citeste_fisier(ifstream& f, vector<unordered_map<int, int> > v, int numar_muchii) {

    //ifstream f(fisier_input);

    for (int i = 0; i < numar_muchii; i++) {

        int x, y;
        f >> x >> y;
        v[x][y] = 1;
        v[y][x] = 1;
    }

    f.close();

    return v;
}

vector<int> colorare_graf(int nod_start, int numar_varfuri, vector<unordered_map<int,int>> lista_adiacenta, int& numar_culori) {

    numar_culori = 0;
    vector<int> culori_varfuri(numar_varfuri);
    fill(culori_varfuri.begin(), culori_varfuri.end(), -1);

    culori_varfuri[nod_start] = 0;

    numar_culori++;

    for (int i = 0; i < numar_varfuri; i++) {

        if (i != nod_start) {

            int culoare_curenta = 0;

            unordered_map<int, int> culori_adiacente;

            for (int j = 0; j < numar_varfuri; j++) {

                if (lista_adiacenta[i][j] == 1) {

                    culori_adiacente[culori_varfuri[j]] = 1;
                }
            }

            while (culoare_curenta < numar_culori && culori_adiacente[culoare_curenta] != 0) {

                culoare_curenta++;
            }

            if (culoare_curenta == numar_culori) {

                culori_varfuri[i] = culoare_curenta;
                numar_culori++;
            }
            else

                culori_varfuri[i] = culoare_curenta;
        }

    }

    return culori_varfuri;

}

int main(int argc, char** argv) {

    ifstream f(argv[1]);

    //ifstream f("fisier_input.in");

    if (!f.is_open())

        return 2;

    int numar_varfuri = 0, numar_muchii = 0;

    f >> numar_varfuri >> numar_muchii;

    vector<unordered_map<int, int> > v(numar_varfuri + 1);

    v = citeste_fisier(f, v, numar_muchii);
    //globals.numar_culori = 0;

    //int numar_culori;

    vector<int> rezultat_final;

    int numar_minim_culori = numar_varfuri + 1;

    f.close();

    for (int i = 0; i < numar_varfuri; i++) {

        int numar_culori = 0;

        vector<int> rez = colorare_graf(i, numar_varfuri, v, numar_culori);

        if (numar_culori < numar_minim_culori) {

            numar_minim_culori = numar_culori;
            rezultat_final = rez;
        }

    }

    ofstream g(argv[2]);

    g << numar_minim_culori << "\n";

    for (auto c : rezultat_final)

        g << c << " ";

    return 0;
}

/*

9 17
0 1
0 3
0 4
0 5
1 5
1 6
1 7
2 5
2 6
3 7
4 5
4 8
5 6
5 8
6 7
6 8
7 8

*/