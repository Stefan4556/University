/*
 *  g++ -std=c++11 -Wall -g -o pb1.exe pb1.cpp
 *  ./pb1.exe ./test_p1/9-in.txt output1.txt
 *      Codare_prufer(F){
 *
 *          k = vid
 *          cat timp t contine si alte varfuri decat radacina repeta
 *
 *                  fie v frunza minima din t
 *                  k - predecesor v
 *                  t = t \ { v }
 *          return k
 *      }
 */
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

#define MAX 100000

int arbore[MAX + 1], nrVarfuri;

int cautaCeaMaiMicaFrunza(){

    int i;

    vector<bool> frunze;

    for(i = 0; i < nrVarfuri; ++i)  // initializam totul ca fiind false
        frunze.push_back(false);

    for(i = 0; i < nrVarfuri; ++i){

        if (arbore[i] == -5)    // vedem daca s-a eliminat sau nu nodul respectiv
            frunze[i] = true;

        else if(arbore[i] >= 0) // marcam parintii
            frunze[arbore[i]] = true;
    }

    for(i = 0; i < nrVarfuri; ++i)

        if (frunze[i] == false)

            break;

    return i;
}

vector<int> CodarePrufer(){

    int ind_frunza = cautaCeaMaiMicaFrunza();
    vector<int> k;

    while(arbore[ind_frunza] != -1){

        k.push_back(arbore[ind_frunza]);

        arbore[ind_frunza] = -5; // marcam faptul ca am eliminat frunza respectiva

        ind_frunza = cautaCeaMaiMicaFrunza();
    }

    return k;
}

int main(int argc, char** argv) {

    ifstream in(argv[1]);
    ofstream out(argv[2]);

    in >> nrVarfuri;

    for(int i = 0; i < nrVarfuri; i++)

        in >> arbore[i];

    vector<int> codare_prufer = CodarePrufer();

    out << codare_prufer.size() << '\n';

    for (auto& varf : codare_prufer)

        out << varf << " ";

    in.close();
    out.close();

    return 0;
}
