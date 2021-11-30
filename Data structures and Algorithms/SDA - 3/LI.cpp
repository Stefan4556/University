#include <exception>
#include <iostream>
#include "LI.h"
#include "IteratorLI.h"

using namespace std;

/*
 *      Complexitatea de timp a functiei ce se ocupa cu initializarea unui nod este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se acutalizeaza doar 3 campuri
 */
Nod::Nod(TElem e, PNod previous, PNod urmator) {

    this->e = e;
    this->prev = previous;
    this->next = urmator;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea valorii unui nod este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se returneaza unul dintre cele 3 campuri ale unui nod
 */
TElem Nod::element() {

    return e;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea pointerului unui nod catre urmatorul nod este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se returneaza unul dintre cele 3 campuri ale unui nod
 */
PNod Nod::urmator() {

    return next;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea pointerului unui nod catre nodul precedent este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se returneaza unul dintre cele 3 campuri ale unui nod
 */
PNod Nod::precedent() {

    return prev;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu initializarea listei inlantuite este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se acutalizeaza doar 3 campuri
 */
LI::LI() {

    prim = nullptr;
    ultim = nullptr;
    lungime = 0;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea dimensiunii listei inlantuite este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se returneaza doar un camp al acestei clase
 */
int LI::dim() const {

    return lungime;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu verificarea daca lista noastra este vida este:
 *
 *          - BC = WC = AC = OC = Teta(1) - deoarece se realizeaza o singura verificare a 2 campuri din clasa
 */
bool LI::vida() const {

    if(prim == nullptr && ultim == nullptr)

        return true;

    return false;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea unui element din lista ce se afla pe pozitia i este:
 *
 *          - BC = Teta(1), daca i nu este valid sau elementul este gasit pe prima pozitie
 *          - WC = Teta(n), unde n este numarul de elemente din lista, caz in care elementul este pe ultima pozitie
 *          - AC = Suma(0,n-1) poz*prob = 0 * 1/(n) + 1 * 1/(n)  + ... + (n-1) * 1/(n) = (1+2+...+(n-1))/(n) = n(n-1)/(2*n) = (n-1) / 2 = aproximativ n => Teta(n), unde n este numarul de elemente
 *          - OC = O(n) - unde n este numarul de elemente din lista
 */
TElem LI::element(int i) const {

    if (i < 0 || i >= lungime)
        throw exception();

    PNod p = prim;

    for (int j = 0; j < dim(); j++) {

        if (j == i) {	// daca ne aflam pe pozitia respectiva inseamna ca trebuie sa returnam valoarea acestuia

            return p->element();
        }

        p = p->next;

    }

}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu modificarea unui element din lista ce se afla pe pozitia i este:
 *
 *          - BC = Teta(1), daca i nu este valid sau elementul este gasit pe prima pozitie si este actualizat
 *          - WC = Teta(n), unde n este numarul de elemente din lista, caz in care elementul este pe ultima pozitie
 *          - AC = Suma(0,n-1) poz*prob = 0 * 1/(n) + 1 * 1/(n)  + ... + (n-1) * 1/(n) = (1+2+...+(n-1))/(n) = n(n-1)/(2*n) = (n-1) / 2 = aproximativ n => Teta(n), unde n este numarul de elemente
 *          - OC = O(n) - unde n este numarul de elemente din lista
 */
TElem LI::modifica(int i, TElem e) {

    if (i < 0 || i >= lungime)
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

}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu adaugarea unui element la finalul listei este:
 *
 *          - BC = WC = AC = OC = Teta(1), deoarece stim deja unde trebuie sa adaugam elementul nefiind nevoie si de alte operatii
 */
void LI::adaugaSfarsit(TElem e) {

    if (prim == nullptr) {	// inseamna ca adaugam pe prima pozitie

        PNod q = new Nod(e, nullptr, ultim);
        prim = q;
        lungime++;
    }
	else if (ultim == nullptr) {	// inseamna ca in lista e un singur element

		PNod q = new Nod(e, prim, nullptr);
		ultim = q;
		prim->next = ultim;
		lungime++;
	}
    else{

        PNod q = new Nod(e, ultim, nullptr);	// creem noul nod ce urmeaza sa fie plasat pe ultima pozitie
        ultim->next = q;
        ultim = q;
        lungime ++;
    }
}

/*
 *      Complexitatea de timp pentru functia ce se ocupa cu adaugarea unui element pe pozitia i este:
 *
 *          - BC = Teta(1), cand elementul trebuie adaugat pe prima pozitie sau nu este valid i
 *          - WC = Teta(n), cand elementul trebuie adaugat pe penultima pozitie, n - numar elemente
 *          - AC = Suma(0,n-2) poz * prob = 0 * 1/(n-1) + 1 * 1/(n-1) + ... + (n-2)*1/(n-1) = (1 + 2 + ... + (n-2)) / (n-1) = (n-1)(n-2)/(2*(n-1)) = (n - 2) / 2 = aproxiamtiv n => Teta(n), n - numar elemente
 *          - OC = O(n), unde n este numarul de elemente
 */
void LI::adauga(int i, TElem e) {

    if (i < 0 || i > lungime)
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
        for (int j = 0; j < i; j++)	// ajungem pe pozitia i in lista noastra
            p = p->next;
        PNod inainte = p->prev;
        inainte->next = nou;
        nou->prev = inainte;
        nou->next = p;
        p->prev = nou;
    }
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu stergerea unui element de pe pozitia i este:
 *
 *          - BC = Teta(1), daca i nu este valid sau trebuie sters primul element sau ultimul sau lista devine vida dupa ce este sters elementul
 *          - WC = Teta(n), daca trebuie sters penultimul element din lista, unde n este numarul de elemente
 *          - AC = Suma(0,n-2) poz * prob = 0 * 1/(n-1) + 1 * 1/(n-1) + ... + (n-2)*1/(n-1) = (1 + 2 + ... + (n-2)) / (n-1) = (n-1)(n-2)/(2*(n-1)) = (n - 2) / 2 = aproxiamtiv n => Teta(n), n - numar elemente
 *          - OC = O(n), unde n este numarul de elemente
 */
TElem LI::sterge(int i) {	// posibil sa fie nevoie sa eliberezi pointerul dupa ce l stergi

    if (i < 0 || i >= lungime)
        throw exception();
    if (i == 0 && lungime == 1){    // inseamna ca mai este doar un singur element in lista

        int val = prim->e;
        ultim= nullptr;
        prim= nullptr;   // marcam faptul ca lista noastra este goala
        lungime--;
        return val;
    }
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
        for (int j = 0; j < i; j++)	// ne deplasam pe pozitia i

            p = p->next;

        PNod inainte = p->prev;
        PNod dupa = p->next;
        inainte->next = dupa;
        dupa->prev = inainte;
        lungime--;
        return p->e;
    }

}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu cautarea unei valori in lista este:
 *
 *          - BC = Teta(1), daca elementul se afla pe prima pozitie
 *          - WC = Teta(n), daca elementul nu exista, unde n este numarul de elemente
 *          - AC = Suma(0,n+1) poz * prob = 0 * 1/(n+1) + 1 * 1/(n+1) + ... + (n+1)*1/(n+1) = (1 + 2 + ... + (n+1)) / (n+1) = (n+1)(n+2)/(2*(n+1)) = (n + 2) / 2 = aproxiamtiv n => Teta(n), n - numar elemente
 *          - OC = Teta(n), unde n este numarul de elemente
 */
int LI::cauta(TElem e) const{

    PNod p = prim;
    for (int i = 0; i < lungime; i++) {

        if (p -> e == e)

            return i;

        p = p -> next;
    }

    return -1;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea iteratorului este:
 *
 *          - BC = WC = AC = OC = Teta(1), pentru ca doar se initializeaza iteratorul
 */
IteratorLI LI::iterator() const {
    return  IteratorLI(*this);
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu dezalocarea elementelor din lista este:
 *
 *          - BC = WC = AC = OC = Teta(n), unde n este numarul de elemente
 */
LI::~LI() {

    for (int i = 0; i < lungime; i++) {

        PNod p = prim;
        prim = prim->next;
        delete p;
    }
}

