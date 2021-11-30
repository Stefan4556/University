#include "Service.h"
#include <algorithm>

vector<Joc> Service::get_all(){

	return this->repo.get_all();
}

void Service::adauga_joc(int dim, string tabla, string jucator){

	string stare = "Neinceput";

	int id = this->repo.get_all().size();

	Joc j{ id, dim, tabla, jucator, stare };

	this->val.valideaza(j);

	this->repo.adauga_joc(j);
}

vector<Joc> Service::sortare_stare(){

	vector<Joc> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Joc j1, Joc j2) {

		return j1.get_stare() < j2.get_stare();
	});

	return rez;
}

void Service::modifica_joc(int id, int dim, string tabla, string jucator, string stare){

	Joc j{ id,dim,tabla,jucator,stare };

	this->val.valideaza(j);

	this->repo.modifica_joc(id, dim, tabla, jucator, stare);
}

Joc Service::get_item_by_id(int id){
	
	return this->repo.get_item_by_id(id);
}
