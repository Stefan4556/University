#include "IteratorColectie.h"
#include "Colectie.h"

// Complexitate Theta(n), unde n este numarul de elemente
void IteratorColectie::inordine(PNod radacina) {	// SRD

	stack<PNod> stiva;

	PNod prec = nullptr;

	PNod p = radacina;

	while (!stiva.empty() || p != nullptr) {

		while (p != nullptr) {

			stiva.push(p);
			p = p->stanga();
		}
		p = stiva.top();	// luam valoarea din varful stivei
		if (this->primul == nullptr) {// trebuie sa o salvam undeva

			this->primul = new Nod(p->element(), nullptr, nullptr);
			prec = this->primul;
		}
		else {

			PNod pp = new Nod(p->element(), nullptr, nullptr);

			if(prec != nullptr)

				prec->dr = pp;

			prec = pp;
		}

		stiva.pop();
		p = p->dreapta();
	}

}

// Complexitate Theta(n), unde n este numarul de elemente
IteratorColectie::IteratorColectie(const Colectie& c) : col(c) {
	
	this->primul = nullptr;
	inordine(c.rad);
	this->curent = this->primul;
}

// Complexitate Theta(1)
TElem IteratorColectie::element() const {
	if (valid() == false)

		throw std::exception();
	
	return this->curent->e;
}

// Complexitate Theta(1)
bool IteratorColectie::valid() const {
	
	if (this->curent != nullptr)

		return true;

	return false;
}

// Complexitate Theta(1)
void IteratorColectie::urmator() {
	
	if (valid() == false)

		throw std::exception();

	this->curent = this->curent->dr;
}

// Complexitate Theta(1)
void IteratorColectie::prim() {
	
	this->curent = this->primul;
}
