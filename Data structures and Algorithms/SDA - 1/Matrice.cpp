#include "Matrice.h"

#include <exception>
#include <iostream>
using namespace std;

/*
 *    Complexitatea de timp pentru functia ce initializeaza o matrice si vectorii aferenti acesteia:
 *
 *       - In cazul in care datele de intrare nu sunt valide complexitatea de timp este Teta(1), algoritmul aruncand o exceptie
 *       - In cazul in care datele de intrare sunt valide, BC = WC = AC = OC = Teta(nr_Lin), constanta 2 de la for-ul cu capacitate fiind ignorata
 */
Matrice::Matrice(int m, int n) {

    if (m <= 0 || n <= 0)
        throw exception();
    nrLin = m;
    nrCol = n;
    nrElem = 0;
    capacitate = 2;
    Linie = new TElem[nrLin+1];
    for (int i = 0; i < nrLin+1; i++)
        Linie[i] = 1;
    Coloana = new TElem[capacitate];
    Valoare = new TElem[capacitate];
    for (int i = 0; i < capacitate; i++) {

        Coloana[i] = -1;
        Valoare[i] = -1;
    }
}
/*
 *      Complexitatea de spatiu pentru aceasta functie de dezalocare este de teta(1), aceasta fiind definita in plus deoarece am crezut ca a fost omisa in .cpp, dar definita in .h
 */
/*
Matrice::~Matrice() {
	//  de adaugat
	delete [] Linie;
	delete [] Coloana;
	delete [] Valoare;
}
*/

/*
 *      Complexitatea de spatiu pentru functia ce returneaza numarul de linii al unei matrici este:
 *
 *      - BC = WC = AC = OC = Teta(1) pentru ca aceasta functie doar returneaza numarul de linii
 */
int Matrice::nrLinii() const{

    return nrLin;
}

/*
 *      Complexitatea de spatiu pentru functia ce returneaza numarul de coloane al unei matrici este:
 *
 *          - BC = WC = AC = OC = Teta(1) pentru ca aceasta functie doar returneaza numarul de coloane
 */
int Matrice::nrColoane() const{

    return nrCol;
}

/*
 *      Complexitatea de spatiu pentru functia ce returneaza un element al matricii situat pe linia i si coloana j este:
 *
 *          - BC = Teta(1) - in cazul in care i si j nu sunt valide sau nu exista niciun element pe linia i
 *          - WC = Teta(nr_coloane) - in cazul in care elementul este situat pe ultima coloana de pe linia i
 *          - AC = Suma(0,n-1) poz * prob = 0 * 1/n + 1 * 1/n + ... + (n-1)* 1/n = (1 + 2 + ... + (n-1)) / n = n(n-1) / (2 * n) = (n - 1) / 2 => Teta(n), unde n este numarul de coloane
 *          - OC = O(nr_coloane) - aceasta cuprinde toate cazurile mentionate anterior
 */
TElem Matrice::element(int i, int j) const{

    if ((i < 0 || i > nrLin - 1) || (j < 0 || j > nrCol - 1))	// cazul in care indicii sunt invalizi

        throw exception();

    if (Linie[i + 1] - Linie[i] == 0) // inseamna ca nu exista elemente pe linia respectiva

        return 0;

    for (int ii = Linie[i]; ii < Linie[i + 1]; ii++)	// mai mic sau egal

        if (Coloana[ii-1] == j)	// inseamna ca l-am gasit

            return Valoare[ii-1];

    return 0;
}

/*
 *      Complexitatea de timp pentru functia ce se ocupa cu alocarea spatiului nou pentru un vector este:
 *
 *          - BC = WC = AC = OC = Teta(n) - unde n este numarul de elemente
 */
void alocaMemorie(TElem* &l, int capacitate, int nr_elem) {

    int capacitate_noua = 2 * capacitate;

    TElem* l_nou = new TElem [capacitate_noua];

    for (int i = 0; i < nr_elem; i++)

        l_nou[i] = l[i];

    delete [] l;

    l = l_nou;
}

/*
 *      Complexitatea de timp pentru functia ce se ocupa cu modificarea unui element este:
 *
 *         - OC = O(m*(n+1)) - aceasta functie cuprinzand toate celelalte cazuri
 *         - e - nr total elemente nenule
 *         - n - nr linii
 *         - m - nr coloane
 */
TElem Matrice::modifica(int i, int j, TElem e) {

    if ((i < 0 || i > nrLin - 1) || (j < 0 || j > nrCol - 1))	// cazul in care indicii sunt invalizi

        throw exception();

    // Daca nu s a aruncat exceptie sunt 3 cazuri:
    //	1) Daca elem pe care vrem sa-l modificam e egal cu valoarea 0, trebuie sa modificam cei 3 vectori + ai grija daca e este 0
    //	2) Daca elem pe care vrem sa-l modificam e diferit de 0 si e este dif de 0, atunci trebuie doar sa modificam valoare
    //	3) Daca elem pe care vrem sa-l modificam e diferit de 0, dar e = 0, atunci trebuie sa actualizam toti cei 3 vectori

    int elem = element(i, j);
    int val_precedenta = 0;

    if (elem != 0 && e != 0) {	// cazul in care trebuie doar sa actualizam valoarea

        for (int ii = Linie[i]; ii < Linie[i + 1]; ii++)	// mai mic sau egal

            if (Coloana[ii-1] == j) {

                val_precedenta = Valoare[ii-1];
                Valoare[ii-1] = e;
                return val_precedenta;

            }
    }
    else if (elem != 0 && e == 0) {	// cazul in care trebuie sa stergem o pozitie

        for (int ii = Linie[i]; ii < Linie[i + 1]; ii++)	// mai mic sau egal

            if (Coloana[ii-1] == j) {	// am ajuns pe pozitia lui

                val_precedenta = Valoare[ii-1];

                for (int jj = ii-1; jj < nrElem-1; jj++) {

                    Coloana[jj] = Coloana[jj + 1];
                    Valoare[jj] = Valoare[jj + 1];
                }
                break;
            }

        for (int ii = i + 1; ii < nrLinii() + 1; ii++)

            Linie[ii]--;

        nrElem--;
        return val_precedenta;
    }
    else if (elem == 0 && e != 0) {	// cazul in care trebuie sa adaugam o pozitie

        nrElem++;
        if (nrElem >= capacitate){ // functia ce aloca memorie daca e nevoie

            alocaMemorie(Coloana, capacitate, nrElem);
            alocaMemorie(Valoare, capacitate, nrElem);
            capacitate *= 2;
        }

        int indice = nrElem-1;
        int dif = Linie[i + 1] - Linie[i];
        int pasi = Linie[i]-1;
        while (Coloana[pasi] < j && pasi < Linie[i + 1]-1) {	// cautam pozitia unde trebuie inserat elementul nou

            pasi++;
        }
        pasi++;

        while (indice >= pasi) {	// deplasam totul spre dreapta

            Coloana[indice] = Coloana[indice - 1];
            Valoare[indice] = Valoare[indice - 1];
            indice--;
            dif--;
        }

        for (int ii = i + 1; ii < nrLinii() + 1; ii++)	// marcam in vectorul Linie ca adaugam un element

            Linie[ii]++;

        Coloana[pasi-1] = j;
        Valoare[pasi-1] = e;

        return 0;	// val ce se afla pe pozitia precedenta
    }
    else // cazul in care elem = 0 si e = 0

        return 0;
}


