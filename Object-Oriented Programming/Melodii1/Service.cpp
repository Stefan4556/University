#include "Service.h"
#include <algorithm>

vector<Melodie> Service::get_all(){

	return this->repo.get_all();
}

vector<Melodie> Service::sortare_autor(){

	vector<Melodie> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Melodie m1, Melodie m2) {

		return m1.get_artist() < m2.get_artist();
	});

	return rez;
}

void Service::adauga_melodie(int id, string titlu, string artist, string gen){

	Melodie m{ id,titlu,artist,gen };
	this->repo.adauga_melodie(m);
}

void Service::sterge_melodie(int id){

	this->repo.sterge_melodie(id);
}
