#include <exception>
#include <iostream>
#include "../Proiect C++/LI.h"
#include "../Proiect C++/IteratorLI.h"

using namespace std;

Nod::Nod(TElem e, PNod previous, PNod urmator) {

	this->e = e;
	this->prev = previous;
	this->next = urmator;
}

TElem Nod::element() {

	return e;
}

PNod Nod::urmator() {

	return next;
}

PNod Nod::precedent() {

	return prev;
}

LI::LI() {
	/* de adaugat */
	prim = nullptr;
	ultim = nullptr;
	lungime = 0;
}

int LI::dim() const {
 	/* de adaugat */
	return lungime;
	//return 0;
}


bool LI::vida() const {
	/* de adaugat */
	if(prim == NULL && ultim == NULL)

		return true;

	return false;
}

TElem LI::element(int i) const {
	/* de adaugat */
	if (i < 0)
		throw exception();

	PNod p = prim;

	for (int j = 0; j < dim(); j++) {

		if (j == i) {	// daca ne aflam pe pozitia respectiva inseamna ca trebuie sa returnam valoarea acestuia

			return p->element();
		}

		p = p->next;

	}

	return -1; // cazul in care nu este gasit elementul - nu sunt sigur ca trebuie
}

TElem LI::modifica(int i, TElem e) {
	/* de adaugat */
	if (i < 0)
		throw exception();

	PNod p = prim;

	int val_precedenta;

	for (int j = 0; j < dim(); j++) {

		if (j == i) {	// daca ne aflam pe pozitia respectiva inseamna ca trebuie sa actualizam si sa returnam valoarea precedenta a acestuia

			val_precedenta = p->element();
			p->e = e;
			return val_precedenta;
		}

		p = p->next;

	}

	return -1;
}

void LI::adaugaSfarsit(TElem e) { // posibil sa fie nev sa tratezi cazul cand e vida
	/* de adaugat */
	if (prim == nullptr) {	// inseamna ca adaugam pe prima pozitie

		PNod q = new Nod(e, nullptr, ultim);
		prim = q;
		ultim = q;	// nu sunt sigur ca e bine
		lungime++;
	}/*
	else if (ultim == nullptr) {	// inseamna ca in lista e un singur element

		PNod q = new Nod(e, prim, nullptr);
		ultim = q;
		lungime++;
	}
	*/
	else{

		PNod q = new Nod(e, ultim, nullptr);	// creem noul nod ce urmeaza sa fie plasat pe ultima pozitie
		ultim->next = q;
		ultim = q;
		lungime ++;
	}
}

void LI::adauga(int i, TElem e) {
	/* de adaugat */
	if (i < 0)
		throw exception();

	PNod nou = new Nod(e, nullptr, nullptr);
	lungime++;
	if (i == 0) {	// inseamna ca adaugam pe prima pozitie
		nou->next = prim;
		prim->prev = nou;
		prim = nou;
	}
	else {	// trebuie inserat pe o anume pozitie
		PNod p = prim;
		for (int j = 0; j <= i; j++)	// ajungem pe pozitia i in lista noastra
			p = p->next;
		PNod inainte = p->prev;
		inainte->next = nou;
		nou->prev = inainte;
		nou->next = p;
		p->prev = nou;
	}
}

TElem LI::sterge(int i) {	// posibil sa fie nevoie sa eliberezi pointerul dupa ce l stergi
	/* de adaugat */
	if (i < 0)
		throw exception();
	if (i == 0) { // inseamna ca trebuie sa stergem primul element

		PNod p = prim;
		prim = p->next;
		prim->prev = nullptr;
		lungime--;
		return p->e;
	}
	else if (i == lungime - 1) {	// inseamna ca trebuie sa stergem ultimul element

		PNod p = ultim;
		ultim = p->prev;
		ultim->next = nullptr;
		lungime--;
		return p->e;
	}
	else {	// suntem pe o pozitie i oarecare in lista

		PNod p = prim;
		for (int j = 0; j <= i; j++)	// ne deplasam pe pozitia i

			p = p->next;

		PNod inainte = p->prev;
		PNod dupa = p->next;
		inainte->next = dupa;
		dupa->prev = inainte;
		lungime--;
		return p->e;
	}
	//return -1;
}

int LI::cauta(TElem e) const{
	/* de adaugat */
	PNod p = prim;
	for (int i = 0; i < lungime; i++) {

		if (p -> e == e)

			return i;

		p = p -> next;
	}

	return -1;
}

IteratorLI LI::iterator() const {
	return  IteratorLI(*this);
}

LI::~LI() {
	/* de adaugat */
	for (int i = 0; i < lungime; i++) {

		PNod p = prim;
		prim = prim->next;
		delete p;
	}
}
