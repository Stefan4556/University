#include "IteratorMDO.h"
#include "MDO.h"
#include <iostream>
#include <vector>

#include <exception>
using namespace std;

// Complexitatea este Teta(1)
Nod_lista::Nod_lista(TElem e, PNod_lista urm, PNod_lista next_ord){

    this->e = e;
    this->next = urm;
    this->next_ordine = next_ord;
}

// Complexitatea este Teta(1)
TCheie Nod_lista::get_cheie() {

    return e.first;
}

// Complexitatea este Teta(1)
TValoare Nod_lista::get_valoare() {

    return e.second;
}

// Complexitatea este Teta(1)
PNod_lista Nod_lista::urmator() {

    return this->next;
}

// Complexitatea este Teta(1)
PNod_lista Nod_lista::urmator_ordine() {

    return this->next_ordine;
}

// Complexitatea este Teta(m), unde m este valoarea ce se foloseste in functia de dispersie
MDO::MDO(Relatie r) {

    this->r = r;
    this->dimensiune = 0;
    this->m = 1003;
    this->minim = nullptr;
    //this->m = 21;
    //this->m = 301;        // varianta asta trece de testele crescatoare dar nu si de cele descresc
    this->dictionar = new PNod_lista [m];

    for(int i = 0; i < m; i++)

        this->dictionar[i] = nullptr;

}

// Complexitatea este O(n), unde n este numarul de elemente
void MDO::adauga(TCheie c, TValoare v) {

    int val_td = abs(c % this->m);

    //if(this->dimensiune + 1 > this->m)  // poate ar trb sa se schimbe cond

        //redimensionare();

    this->dimensiune++;

    PNod_lista p;
    PNod_lista prec = nullptr;
    p = this->dictionar[val_td];
    while(p != nullptr && this->r(p->get_cheie(),c) == true){

        prec = p;
        p = p->urmator();
    }
    if(prec == nullptr){    // inseamna ca inseram pe prima pozitie

        PNod_lista nod_nou = new Nod_lista(make_pair(c,v), this->dictionar[val_td], nullptr);
        this->dictionar[val_td] = nod_nou;
        this->restabileste_ordine(nod_nou,prec);
    }
    else{   // inseram pe o pozitie random

        PNod_lista nod_nou = new Nod_lista(make_pair(c,v), p, nullptr);
        prec->next = nod_nou;
        this->restabileste_ordine(nod_nou,prec);
    }
}

// Complexitatea este O(n), unde n este numarul de elemente
vector<TValoare> MDO::cauta(TCheie c) const {

    vector<TValoare> rez;

    PNod_lista p = this->dictionar[abs(c) % this->m];

    while(p != nullptr){

        if(p->get_cheie() == c)

            rez.push_back(p->get_valoare());

        p = p->urmator();
    }

    return rez;
}

// Complexitatea este O(n), unde n este numarul de elemente
bool MDO::sterge(TCheie c, TValoare v) {

    int val_td = abs(c % this->m);

    if(this->dictionar[val_td] != nullptr){

        PNod_lista p = this->dictionar[val_td];
        PNod_lista prec = nullptr;
        while(p != nullptr && this->r(c,p->get_cheie()) == true && p->get_valoare() != v){

            prec = p;
            p = p->urmator();
        }
        if(prec == nullptr && p->get_valoare() == v){   // suntem pe prima pozitie

            this->dictionar[val_td] = p->urmator();
            this->dimensiune--;
            if(p == this->minim)

                minim = this->minim->next_ordine;

            else{

                PNod_lista pp = minim;
                while(pp->next_ordine != nullptr && pp->next_ordine != p)

                    pp = pp->next_ordine;

                pp->next_ordine = p->next_ordine;
            }

            return true;
        }
        else if(p != nullptr && p->get_valoare() == v && prec != nullptr){

            prec->next = p->urmator();
            this->dimensiune--;
            prec->next_ordine = p->next_ordine;
            return true;
        }
    }

    return false;
}

// Complexitatea este Teta(1)
int MDO::dim() const {

    return this->dimensiune;
}

// Complexitatea este Teta(1)
bool MDO::vid() const {

    if (this->dimensiune == 0)

        return true;

    return false;
}

// Complexitatea este Teta(1)
IteratorMDO MDO::iterator() const {
    return IteratorMDO(*this);
}

// Complexitatea este Teta(1)
MDO::~MDO() {

    delete [] this->dictionar;
}
/*
void MDO::redispersare(TElem* vec, int lung){

    for(int i = 0; i < lung; i++){

        this->adauga(vec[i].first, vec[i].second);
    }
}

void MDO::redimensionare() {

    Nod_lista** nou = new Nod_lista* [m * 2];

    TElem* val = new TElem [m * 2];

    int ct = 0;

    for(int i = 0; i < m ; i++) {

        nou[i] = nullptr;

        if(this->dictionar[i] != nullptr){

            Nod_lista* p = this->dictionar[i];
            while(p != nullptr){

                val[ct] = pair(p->get_cheie(),p->get_valoare());
                ct++;
                p = p->urmator();
            }
        }
    }

    for(int i = m; i < m * 2; i++)

        nou[i] = nullptr;

    delete[] this->dictionar;
    this->dictionar = nou;
    this->m *= 2;
    this->dimensiune = 0;

    redispersare(val, ct);
}*/

// Complexitatea este O(n), unde n este numarul de elemnte
void MDO::restabileste_ordine(PNod_lista curent, PNod_lista precedent) {

    if(precedent == nullptr){

        PNod_lista p = this->minim;
        if(p == nullptr) {

            this->minim = curent;
            return;
        }

        if(this->r(p->get_cheie(),curent->get_cheie()) == false){

            curent->next_ordine = this->minim;
            this->minim = curent;
            return;
        }

        while(p->urmator_ordine() != nullptr && this->r(p->urmator_ordine()->get_cheie(),curent->get_cheie()) == true){

            p = p->urmator_ordine();
        }

        curent->next_ordine = p->urmator_ordine();
        p->next_ordine = curent;
    }
    else{

        PNod_lista p = precedent;

        while(p->urmator_ordine() != nullptr && this->r(p->urmator_ordine()->get_cheie(),curent->get_cheie()) == true){

            p = p->urmator_ordine();
        }

        curent->next_ordine = p->urmator_ordine();
        p->next_ordine = curent;
    }
}
