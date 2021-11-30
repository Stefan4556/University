#include "../Proiect C++/IteratorLI.h"
#include "../Proiect C++/LI.h"
#include <exception>

IteratorLI::IteratorLI(const LI& li): 
    lista(li) {
 	/* de adaugat */

    curent = li.prim;
}

void IteratorLI::prim(){
 	/* de adaugat */
    curent = lista.prim;
}

void IteratorLI::urmator(){
 	/* de adaugat */
    curent = curent->urmator();
}

bool IteratorLI::valid() const{
 	/* de adaugat */
    return curent != nullptr;
	//return false;
}

TElem IteratorLI::element() const{
 	/* de adaugat */
    return curent->element();
	//return -1;
}
