#include "Matrice.h"

#include <exception>
#include <iostream>
using namespace std;


Matrice::Matrice(int m, int n) {
	/* de adaugat */
	if (m <= 0 || n <= 0)
		throw;//throw 1;
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
Matrice::~Matrice() {
	//  de adaugat 
	delete [] Linie;
	delete [] Coloana;
	delete [] Valoare;
}
*/

int Matrice::nrLinii() const{
	/* de adaugat */
	return nrLin;
}


int Matrice::nrColoane() const{
	/* de adaugat */
	return nrCol;
}


TElem Matrice::element(int i, int j) const{
	/* de adaugat */
	if ((i < 0 || i > nrLin - 1) || (j < 0 || j > nrCol - 1))	// cazul in care indicii sunt invalizi

		throw exception();//throw 1;

	if (Linie[i + 1] - Linie[i] == 0) // inseamna ca nu exista elemente pe linia respectiva

		return 0;

	for (int ii = Linie[i]; ii < Linie[i + 1]; ii++)	// mai mic sau egal

		if (Coloana[ii-1] == j)	// inseamna ca l-am gasit

			return Valoare[ii-1];

	return 0;
}


void alocaMemorie(TElem* &l, int capacitate, int nr_elem) {

	int capacitate_noua = 2 * capacitate;

	TElem* l_nou = new TElem [capacitate_noua];

	for (int i = 0; i < nr_elem; i++)

		l_nou[i] = l[i];

	delete [] l;

	l = l_nou;
}


TElem Matrice::modifica(int i, int j, TElem e) {
	/* de adaugat */
	if ((i < 0 || i > nrLin - 1) || (j < 0 || j > nrCol - 1))	// cazul in care indicii sunt invalizi

		throw exception();//throw 1;

	// Daca nu s a aruncat exceptie sunt 3 cazuri:
	//	1) Daca elem pe care vrem sa-l modificam e egal cu valoarea 0, trebuie sa modificam cei 3 vectori + ai grija daca e este 0
	//	2) Daca elem pe care vrem sa-l modificam e diferit de 0 si e este dif de 0, atunci trebuie doar sa modificam valoare - tratat
	//	3) Daca elem pe care vrem sa-l modificam e diferit de 0, dar e = 0, atunci trebuie sa actualizam toti cei 3 vectori - tratat

	int elem = element(i, j);
	int val_precedenta = 0;

	if (elem != 0 && e != 0) {	// cazul in care trebuie doar sa actualizam valoarea

		for (int ii = Linie[i]; ii < Linie[i + 1]; ii++)	// mai mic sau egal

			if (Coloana[ii-1] == j) {

				val_precedenta = Valoare[ii-1];
				Valoare[ii-1] = e;
				/*
				cout << '\n' << '\n' << "Linie: ";
				for (i = 0; i <= nrLinii(); i++)
					cout << Linie[i] << ", ";
				cout << '\n';
				for (i = 0; i < nrElem; i++)
					cout << Coloana[i] << " " << Valoare[i] << " | ";

				cout << '\n';
				*/
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
		/*
		cout << '\n' << '\n' << "Linie: ";
		for (i = 0; i <= nrLinii(); i++)
			cout << Linie[i] << ", ";
		cout << '\n';
		for (i = 0; i < nrElem; i++)
			cout << Coloana[i] << " " << Valoare[i] << " | ";

		cout << '\n';
		*/
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
		//cout << '\n' << "Pasi: " << pasi<<" Diferenta: "<<dif;
		while (indice >= pasi) {	// in loc de pasi era 0 indice = dif

			Coloana[indice] = Coloana[indice - 1];
			Valoare[indice] = Valoare[indice - 1];
			indice--;
			dif--;
		}
		
		for (int ii = i + 1; ii < nrLinii() + 1; ii++)	// marcam in vectorul Linie ca adaugam un element

			Linie[ii]++;

		Coloana[pasi-1] = j;
		Valoare[pasi-1] = e;
		/*
		cout << '\n' << '\n' << "Linie: ";
		for (i = 0; i <= nrLinii(); i++)
			cout << Linie[i] << ", ";
		cout << '\n';
		for (i = 0; i < nrElem; i++)
			cout << Coloana[i] << " " << Valoare[i] << " | ";

		cout << '\n';
		*/
		
		return 0;	// val ce se afla pe pozitia precedenta
	}
	else // cazul in care elem = 0 si e = 0 

		return 0;
}


