#pragma once

#include "IteratorColectie.h"
typedef int TElem;

typedef bool(*Relatie)(TElem, TElem);

//in implementarea operatiilor se va folosi functia (relatia) rel (de ex, pentru <=)
// va fi declarata in .h si implementata in .cpp ca functie externa colectiei
bool rel(TElem, TElem);

class Nod;

typedef Nod* PNod;

class IteratorColectie;

class Nod {

public:

	friend class Colectie;

	friend class IteratorColectie;

	Nod(TElem e, PNod st, PNod dr);

	TElem element();

	TElem frecventa();

	PNod stanga();

	PNod dreapta();

private:

	TElem e;

	int frecv;

	PNod st, dr;

};

class Colectie {

	friend class IteratorColectie;

private:
	
	PNod rad;

	//PNod adauga_rec(PNod p, TElem e);

	void distruge_rec(PNod);

	int dimensiune;

	PNod minim(PNod p);

	PNod sterge_rec(PNod p, TElem e, bool& ok);

public:
	//constructorul implicit
	Colectie();

	//adauga un element in colectie
	void adauga(TElem e);

	//sterge o aparitie a unui element din colectie
	//returneaza adevarat daca s-a putut sterge
	bool sterge(TElem e);

	//verifica daca un element se afla in colectie
	bool cauta(TElem elem) const;

	//returneaza numar de aparitii ale unui element in colectie
	int nrAparitii(TElem elem) const;


	//intoarce numarul de elemente din colectie;
	int dim() const;

	//verifica daca colectia e vida;
	bool vida() const;

	//returneaza un iterator pe colectie
	IteratorColectie iterator() const;

	// destructorul colectiei
	~Colectie();

	int eliminaToateAparitiile(TElem elem);

	PNod elimina_toate_recursiv(PNod p, TElem e, int& nr_ap, bool& ok);
};

