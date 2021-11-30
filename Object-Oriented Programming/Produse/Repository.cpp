#include "Repository.h"
#include <fstream>

void Repository::load_from_file(){

	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id;
		double pret;
		string nume, tip;
		in >> id >> nume >> tip >> pret;
		Produs p{ id,nume,tip,pret };
		this->lista.push_back(p);
	}
	in.close();
}

void Repository::adauga_produs(Produs p) {

	for (auto el : lista)

		if (el.get_id() == p.get_id())

			throw string("Mai exista un produs cu acest id!\n");

	this->lista.push_back(p);
}


vector<Produs> Repository::get_all(){

	return this->lista;
}
