
#include <exception>

#include "IteratorLP.h"
#include "Lista.h"

#include <iostream>

// Complexitate - Teta (4 * capacitate aprox capacitate)
Lista::Lista() {
    /* de adaugat */
    capacitate = 4; // cred ca trebuie marita dimensiunea
    e = new TElem[capacitate];
    urm = new int[capacitate];
    prec = new int[capacitate];
    primu = -1;
    ultim = -1;
    primLiber = 0;
    lungime = 0;
    for(int i = 0; i < capacitate - 1; i++){

        urm[i] = i + 1;
        prec[i] = i - 1;
    }
    urm[capacitate - 1] = -1;
    prec[capacitate - 1] = capacitate - 2;
}

// Complexitate - Teta(1)
int Lista::dim() const {
    /* de adaugat */
    return lungime;
    //return 0;
}

// Complexitate - Teta(1)
bool Lista::vida() const {
    /* de adaugat */

    if(primu == -1)

        return true;

    return false;
}

// Complexitate - Teta(1)
IteratorLP Lista::prim() const {
    /* de adaugat */
    return IteratorLP(*this);
}

// Complexitate - Teta(1)
TElem Lista::element(IteratorLP poz) const {
    /* de adaugat */
    if (poz.valid() == false)
        throw std::exception();

    return poz.element();
}

// Complexitate - Teta(1)
TElem Lista::sterge(IteratorLP& poz) {
    /* de adaugat */
    if (poz.valid() == false)
        throw std::exception();

    TElem val_precedenta = poz.element();

    int nod = poz.curent;

    int nod_prec, nod_urm;

    nod_prec = this->prec[nod];

    nod_urm = this->urm[nod];

    this->dealoca(nod);

    if(nod_prec != -1)

        this->urm[nod_prec] = nod_urm;

    else

        this->primu = nod_urm;

    if(nod_urm != -1)

        this->prec[nod_urm] = nod_prec;

    else

        this->ultim = nod_prec;

    this->lungime--;

    return val_precedenta;
}

// Complexitate - O(n) - n nr de elemente
IteratorLP Lista::cauta(TElem e) const{
    /* de adaugat */
    IteratorLP it(*this);

    while(it.valid()){

        if(it.element() == e)
            return it;

        it.urmator();
    }

    return it;  // s ar putea sa fie throw exception
}

// Complexitate - Teta(1)
TElem Lista::modifica(IteratorLP poz, TElem e) {
    /* de adaugat */

    if(poz.valid() == false)

        throw std::exception();

    int val_precedenta = this->e[poz.curent];

    this->e[poz.curent] = e;

    return val_precedenta;
}

// Complexitate - Teta(1)
void Lista::dealoca(int nod){

    this->urm[nod] = primLiber;
    this->primLiber = nod;
}

// Complexitate - O(capacitate)
int Lista::aloca(){

    if(primLiber == -1) { // inseamna ca nu mai avem spatiu

        int new_capacity = 2 * this->capacitate;
        int *urm1, *prec1;
        TElem *e1;

        urm1 = new int[new_capacity];
        prec1 = new int[new_capacity];
        e1 = new TElem[new_capacity];

        for(int i = 0; i < this->capacitate; i++){

            urm1[i] = this->urm[i];
            prec1[i] = this->prec[i];
            e1[i] = this->e[i];
        }
        delete[] this->e;
        delete[] this->urm;
        delete[] this->prec;
        this->e = e1;
        this->urm = urm1;
        this->prec = prec1;

        for(int i = this->capacitate; i < new_capacity - 1; i++){

            urm[i] = i + 1;
            prec[i] = i - 1;
        }

        this->primLiber = this->capacitate;

        this->capacitate = new_capacity;

        urm[capacitate - 1] = -1;

        prec[capacitate - 1] = capacitate - 2;
    }
    int nod = primLiber;

    primLiber = this->urm[primLiber];

    return nod;
}

// Complexitate - Teta(1)
void Lista::adauga(IteratorLP& poz, TElem e) {
    /* de adaugat */
    if(poz.valid() == false)
        throw std::exception();

    int nod_poz = poz.curent;

    int nod_urm = this->urm[nod_poz];

    int nod_nou = aloca();

    this->e[nod_nou] = this->e[nod_poz];

    this->e[nod_poz] = e;

    this->urm[nod_poz] = nod_nou;

    this->prec[nod_nou] = nod_poz;

    this->urm[nod_nou] = nod_urm;

    if(nod_urm != -1)   // inseamna ca este valid

        this->prec[nod_urm] = nod_nou;

    else    // inseamna ca este ultimul element

        this->ultim = nod_nou;

    lungime++;

}

// Complexitate - Teta(1)
void Lista::adaugaInceput(TElem e) {
    /* de adaugat */

    int nod_nou = aloca();

    this->e[nod_nou] = e;

    this->urm[nod_nou] = primu;

    this->prec[nod_nou] = -1;

    if(primu != -1)  // verificam daca lista este nevida

        this->prec[primu] = nod_nou;

    else

        this->ultim = nod_nou;

    this->primu = nod_nou;

    lungime++;

}

// Complexitate - Teta(1)
void Lista::adaugaSfarsit(TElem e) {
    /* de adaugat */

    int nod_nou = aloca();

    this->e[nod_nou] = e;

    this->prec[nod_nou] = ultim;

    this->urm[nod_nou] = -1;

    if(ultim != -1) // verificam daca a mai fost actualizat sau nu ultimul element

        this->urm[ultim] = nod_nou;

    else

        this->primu = nod_nou;

    this->ultim = nod_nou;

    lungime++;

}

/*
 *  Complexitate Teta(n) - unde n este numarul de elemente
 *
 *  Pseudocod:
 *
 *  Inceput subalgoritm
 *
 *          it <- Iterator(this)
 *          rez <- -1
 *
 *          cat timp valid(it) = true executa
 *
 *              daca element(it) = elem atunci
 *
 *                  rez = it.curent
 *
 *              Sf daca
 *
 *              urmator(it)
 *
 *          Sf cat timp
 *
 *          returneaza rez
 *
 *  Sfarsit subalgoritm
 */
int Lista::ultimulIndex(TElem elem) const{

    IteratorLP it(*this);

    int rez = -1;

    while(it.valid()){

        if (it.element() == elem){

            rez = it.curent;
        }
        it.urmator();
    }

    return rez;
}

// Complexitate - Teta(1)
Lista::~Lista() {
    /* de adaugat */
    delete[] e;
    delete[] prec;
    delete[] urm;
}
