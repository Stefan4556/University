#include "IteratorLI.h"
#include "LI.h"
#include <exception>

/*
 *      Complexitatea de timp a functiei ce se ocupa cu initializarea iteratorului este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 */
IteratorLI::IteratorLI(const LI& li):
        lista(li) {


    curent = li.prim;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea pointerului catre primul element este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 */
void IteratorLI::prim(){

    curent = lista.prim;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu mutarea pointerului catre urmatorul element este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 */
void IteratorLI::urmator(){

    if (curent == nullptr)
        throw std::exception();
    curent = curent->urmator();
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu validarea pointerului este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 */
bool IteratorLI::valid() const{

    return curent != nullptr;
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu returnarea valorii ce se afla la adresa pointerului este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 */
TElem IteratorLI::element() const{

    if (curent == nullptr)
        throw std::exception();
    return curent->element();
}

/*
 *      Complexitatea de timp a functiei ce se ocupa cu mutarea iteratorului pe pozitia precedenta este:
 *
 *          - BC = WC = AC = OC = Teta(1)
 *
 *      Pseudocod:
 *
 *          Incepeput subalgoritm
 *
 *                  daca curent == NIL atunci
 *
 *                       arunca exceptie
 *
 *                  Sf daca
 *
 *                  daca precedent(curent) = NIL atunci
 *
 *                      curent <- NIL
 *
 *                  altfel
 *
 *                       curent <- precedent(curent)
 *
 *                  Sf daca
 *
 *          Sfarsit subalgoritm
 */
void IteratorLI::anterior(){

    if (curent == nullptr)  // cazul in care nu este valid iteratorul curent

        throw std::exception();

    if (curent->precedent() == nullptr) { // verificam daca suntem pe prima pozitie

        //throw std::exception();
        curent = nullptr;

    } else
        curent=curent->precedent();

}
