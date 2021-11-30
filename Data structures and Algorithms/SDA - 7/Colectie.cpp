#include "Colectie.h"
#include "IteratorColectie.h"
#include <iostream>

using namespace std;

// Complexitate Theta(1)
Nod::Nod(TElem e, PNod st, PNod dr){

	this->e = e;
	this->frecv = 1;
	this->st = st;
	this->dr = dr;
}

// Complexitate Theta(1)
TElem Nod::element() {

	return this->e;
}

// Complexitate Theta(1)
int Nod::frecventa() {

	return this->frecv;
}

// Complexitate Theta(1)
PNod Nod::stanga() {

	return this->st;
}

// Complexitate Theta(1)
PNod Nod::dreapta() {

	return this->dr;
}

// Complexitate Theta(1)
bool rel(TElem e1, TElem e2) {
	
	if (e1 <= e2)

		return true;

	return false;
}
/*
PNod Colectie::adauga_rec(PNod p, TElem e) {	// de facut iterativ

	if (p == nullptr) {

		p = new Nod(e, nullptr, nullptr);
	}
	else {

		if (e == p->element())

			p->frecv++;

		else {

			if (rel(e, p->element()) == true)

				p->st = adauga_rec(p->st, e);

			else

				p->dr = adauga_rec(p->dr, e);
		}
	}
}*/

// Complexitate Theta(n), unde n sunt elementele situate pe partea stanga si dreapta a arborelui ce are ca radacina nodul p
void Colectie::distruge_rec(PNod p) {

	if (p != nullptr) {

		distruge_rec(p->stanga());
		distruge_rec(p->dreapta());
		delete p;
	}
}

// Complexitate Theta(1)
Colectie::Colectie() {
	
	this->rad = nullptr;
	this->dimensiune = 0;
}

// Complexitate O(h), unde h este inaltimea arborelui
void Colectie::adauga(TElem e) {
	
	//this->rad = adauga_rec(this->rad, e);

	PNod p = this->rad;

	PNod prec = nullptr;

	this->dimensiune++;

	if(p == nullptr)

		this->rad = new Nod(e, nullptr, nullptr);

	else {

		while (p != nullptr) {

			if (p -> element() == e) {

				p->frecv++;
				return;
			}

			if (rel(e, p->element()) == true) {// mergem in stanga

				prec = p;
				p = p->st;
			}
			else {

				prec = p;
				p = p->dr;
			}
		}

		if (p == nullptr) {

			p = new Nod(e, nullptr, nullptr);

			if (rel(e, prec->e) == true)	// trb pus in stanga

				prec->st = p;

			else

				prec->dr = p;
		}
	}
}

// Complexitate O(h), unde h este inaltimea arborelui
PNod Colectie::minim(PNod p) {

	while (p->st != nullptr) {

		p = p->st;
	}

	return p;
}

// Complexitate O(h), unde h este inaltimea arborelui
PNod Colectie::sterge_rec(PNod p, TElem e, bool& ok) {

	if (p == nullptr)

		return nullptr;

	else {

		if (e < p->e) {

			p->st = sterge_rec(p->st, e, ok);
			return p;
		}
		else if (e > p->e) {

			p->dr = sterge_rec(p->dr, e, ok);
			return p;
		}
		else {

			if (ok == false)

				this->dimensiune--;

			if (p->frecv - 1 != 0 && ok == false) {

				p->frecv--;
				ok = true;
				return p;
			}

			ok = true;

			if (p->st != nullptr && p->dr != nullptr) {

				PNod temp = minim(p->dr);
				p->e = temp->e;
				p->frecv = temp->frecv;
				bool ok2 = true;
				p->dr = sterge_rec(p->dr, p->e, ok2);
				return p;
			}
			else {

				PNod temp = p;

				PNod repl = nullptr;

				if (p->st == nullptr)

					repl = p->dr;

				else

					repl = p->st;

				delete p;

				return repl;
			}
		}
	}
}

// Complexitate O(h), unde h este inaltimea arborelui
bool Colectie::sterge(TElem e) {
	
	bool ok = false;

	this->rad = sterge_rec(this->rad, e, ok);

	return ok;

	//return false;
}

// Complexitate O(h), unde h este inaltimea arborelui
bool Colectie::cauta(TElem elem) const {
	
	PNod p = this->rad;

	while (p != nullptr) {

		if (p->element() == elem)

			return true;

		else {

			if (rel(elem, p->element()) == true)	// inseamna ca e mai mic sau egal deci mergem in stanga

				p = p->stanga();

			else

				p = p->dreapta();
		}
	}

	return false;
}

// Complexitate O(h), unde h este inaltimea arborelui
int Colectie::nrAparitii(TElem elem) const {
	
	PNod p = this->rad;

	while (p != nullptr) {

		if (p->element() == elem)

			return p->frecventa();

		else {

			if (rel(elem, p->element()) == true)	// inseamna ca e mai mic sau egal deci mergem in stanga

				p = p->stanga();

			else

				p = p->dreapta();
		}
	}

	return 0;
}

// Complexitate Theta(1)
int Colectie::dim() const {
	
	return this->dimensiune;
}

// Complexitate Theta(1)
bool Colectie::vida() const {
	
	if (this->dimensiune == 0)

		return true;

	return false;
}

// Complexitate Theta(1)
IteratorColectie Colectie::iterator() const {

	return  IteratorColectie(*this);
}

// Complexitate Theta(n), unde n e numarul de elemente
Colectie::~Colectie() {
	
	this->distruge_rec(this->rad);
}

// Complexitate O(h), unde h este inaltimea arborelui
/*
*		Inceput subalgoritm elimina_toate_recursiv(p, e, nr_ap, ok)
* 
*			daca p = NIL atunci
* 
*				elimina_toate_recursiv <- NIL
* 
*			altfel
* 
*				daca e < [p].e atunci
* 
*					[p].st <- elimina_toate_recursiv([p].st, e, nr_ap, ok)
*					elimina_toate_recursiv <- p
*				
*				altfel
* 
*					daca e > [p].e atunci
* 
*						[p].dr <- elimina_toate_recursiv([p].dr, e, nr_ap, ok)
*						elimina_toate_recursiv <- p
* 
*					altfel
* 
*						daca ok = fals atunci
* 
*							ok <- adevarat
*							nr_ap <- [p].frecv
*							dimensiune <- dimensiune - [p].frecv
* 
*						sfDaca
* 
*						daca [p].st != NIL ^ [p].dr != NIL atunci
* 
*							temp <- minim([p].dr)
*							[p].e <- [temp].e
*							[p].frecv <- [temp].frecv
*							[p].dr <- elimina_toate_recursiv([p].dr, e, nr_ap, ok)
*							elimina_toate_recursiv <- p
*				
*						altfel
* 
*							temp <- p
*							
*							daca [p].st = NIL atunci
*					
*								repl <- [p].dr
*				
*							altfel
* 
*								repl <- [p].st
* 
*							sfDaca
* 
*							dealoca(temp)
*							elimina_toate_recursiv <- repl
*						
*						sfDaca
*					
*					sfDaca
* 
*				sfDaca
* 
*			sfDaca
* 
* Sfarsit subalgoritm						
*/
PNod Colectie::elimina_toate_recursiv(PNod p, TElem e, int& nr_ap, bool& ok) {

	if (p == nullptr)

		return nullptr;

	else {

		if (e < p->e) {

			p->st = elimina_toate_recursiv(p->st, e, nr_ap,ok);
			return p;
		}
		else if (e > p->e) {

			p->dr = elimina_toate_recursiv(p->dr, e, nr_ap,ok);
			return p;
		}
		else {

			if (ok == false) {

				ok = true;
				nr_ap = p->frecv;
				this->dimensiune -= p->frecv;
			}

			if (p->st != nullptr && p->dr != nullptr) {

				PNod temp = minim(p->dr);
				p->e = temp->e;
				p->frecv = temp->frecv;
				p->dr = elimina_toate_recursiv(p->dr, p->e, nr_ap, ok);
				return p;
			}
			else {

				PNod temp = p;

				PNod repl = nullptr;

				if (p->st == nullptr)

					repl = p->dr;

				else

					repl = p->st;

				delete temp;

				return repl;
			}
		}
	}
}

// Complexitate O(h), unde h este inaltimea arborelui
/*
*	Inceput subalgoritm eliminaToateAparitiile(arb, elem)
* 
*			nr_ap <- 0
*			ok <- fals
*			arb.rad <- elimina_toate_recursiv(arb.rad, elem, nr_ap, ok)
*			eliminaToateAparitiile <- nr_ap
* 
*	Sfarsit subalgoritm
*/
int Colectie::eliminaToateAparitiile(TElem elem) {

	int nr_ap = 0;
	bool ok = false;
	this->rad = elimina_toate_recursiv(this->rad, elem, nr_ap, ok);
	
	return nr_ap;
}

// Se putea face si mai simplu recicland codul
// Retineam intr o variabila numar de aparitii al nr respectiv, dupa care intr-un for apelam functia de stergere de nr de ap ori
// Returnam numarul de aparitii retinut in variabila de la inceput