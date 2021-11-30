#include <iostream>


#include "TestScurt.h"
#include "TestExtins.h"
#include "IteratorLP.h"

void test_cerinta(){

    Lista lista = Lista();
    lista.adaugaSfarsit(1);
    lista.adaugaSfarsit(1);
    lista.adaugaSfarsit(1);
    assert(lista.ultimulIndex(1) == 2);
}

int main(){
   testAll();
   testAllExtins();
   test_cerinta();
    std::cout<<"Finished LP Tests!"<<std::endl; // intreaba de activitati la seminar
}



//14.TAD Lista(interfața cu TPoziție=Iterator) –reprezentare folosind o LDI.