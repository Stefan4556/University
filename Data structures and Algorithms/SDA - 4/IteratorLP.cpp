#include "IteratorLP.h"
#include "Lista.h"
#include <exception>

// Complexitate - Teta(1)
IteratorLP::IteratorLP(const Lista& l):lista(l) {
    /* de adaugat */
    curent = l.primu;
}

// Complexitate - Teta(1)
void IteratorLP::prim(){
    /* de adaugat */
    curent = lista.primu;
}

// Complexitate - Teta(1)
void IteratorLP::urmator(){
    /* de adaugat */
    if(this->valid() == false)
        throw std::exception();
    curent = lista.urm[curent];

}

// Complexitate - Teta(1)
bool IteratorLP::valid() const{
    /* de adaugat */
    if(curent != -1)
        return true;
    return false;
}

// Complexitate - Teta(1)
TElem IteratorLP::element() const{
    /* de adaugat */
    if(this->valid() == false)
        throw std::exception();

    return lista.e[curent];
}


