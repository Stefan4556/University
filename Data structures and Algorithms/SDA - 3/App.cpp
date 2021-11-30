#include <iostream>
#include <exception>
#include <assert.h>

#include "TestScurt.h"
#include "TestExtins.h"
#include "IteratorLI.h"
#include "LI.h"

void testeaza_lab(){

    LI lista = LI();
    lista.adaugaSfarsit(1);
    lista.adaugaSfarsit(2);
    lista.adaugaSfarsit(3);

    IteratorLI it = lista.iterator();
    it.anterior();                      // cazul in care suntem pe prima pozitie
    assert(it.valid() == false);
    IteratorLI it2 = lista.iterator();
    assert(it2.element() == 1);
    it2.urmator();
    assert(it2.element() == 2);
    it2.anterior();
    assert(it2.element() == 1);
    it2.urmator();
    it2.urmator();
    it2.urmator();
    try{                                // cazul in care suntem pe un iterator invalid
        it2.anterior();
        assert(false);
    } catch (std::exception&){
        assert(true);
    }
}

int main(){
    testeaza_lab();
    testAll();
    testAllExtins();
    std::cout<<"Finished LI Tests!"<<std::endl;
}
