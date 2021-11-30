#include "Service.h"
#include <algorithm>

vector<Melodie> Service::get_all(){

	return this->repo.get_all();
}

vector<Melodie> Service::sortare_rank(){

	vector<Melodie> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Melodie m1, Melodie m2) {

		return m1.get_rank() < m2.get_rank();
	});

	return rez;
}

void Service::modifica_titlu_rank(int id, string titlu_nou, int rank_nou){

	this->repo.modifica_titlu_rank(id, titlu_nou, rank_nou);
}

void Service::sterge_melodie(string titlu){

	this->repo.sterge(titlu);
}
