#include "Service.h"
#include <algorithm>

vector<Produs> Service::get_all(){

	return this->repo.get_all();
}

vector<Produs> Service::sortare_pret(){
	
	vector<Produs> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Produs p1, Produs p2) {

		return p1.get_pret() < p2.get_pret();
	});

	return rez;
}

void Service::adauga_produs(int id, string nume, string tip, double pret) {

	Produs p{ id, nume, tip, pret };

	this->val.valideaza(p);

	this->repo.adauga_produs(p);

	notify();
}