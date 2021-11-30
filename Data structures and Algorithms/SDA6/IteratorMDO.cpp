#include "IteratorMDO.h"
#include "MDO.h"

// Complexitatea este Teta(1)
IteratorMDO::IteratorMDO(const MDO& d) : dict(d){

    //this->pozCurenta = 0;
    this->curent = d.minim;
    //deplasare();
}

// Complexitatea este Teta(1)
void IteratorMDO::prim(){

    this->curent = dict.minim;
}

// Complexitatea este Teta(1)
void IteratorMDO::urmator(){

    if(this->valid() == false)

        throw exception();

    this->curent = this->curent->urmator_ordine();

}

// Complexitatea este Teta(1)
bool IteratorMDO::valid() const{

    if(this->curent != nullptr)

        return true;

    return false;
}

// Complexitatea este Teta(1)
TElem IteratorMDO::element() const{

    if(valid() == false)

        throw exception();

    return std::make_pair(this->curent->get_cheie(),this->curent->get_valoare());
}
/*
void IteratorMDO::deplasare() {

    while(this->pozCurenta < dict.m && dict.dictionar[this->pozCurenta] == nullptr)

        this->pozCurenta++;

    if(this->pozCurenta < dict.m)

        this->curent = dict.dictionar[this->pozCurenta];
}*/