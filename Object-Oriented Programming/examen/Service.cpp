#include "Service.h"
#include <algorithm>

vector<Carte> Service::get_all()
{
	return this->repo.get_all();
}

void Service::adauga_carte(int id, string titlu, string tip, double pret)
{
	Carte c{ id,titlu,tip,pret };

	this->val.valideaza(c);

	this->repo.adauga_carte(c);

	notify();
}

vector<Carte> Service::sortare_litere()
{
	vector<Carte> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Carte c1, Carte c2) {

		return c1.get_tip().size() < c2.get_tip().size();
	});

	return rez;
}

vector<Carte> Service::get_lista_tip(string tip)
{
	vector<Carte> rez;
	vector<Carte> lista = this->repo.get_all();

	for (auto elem : lista)

		if (elem.get_tip() == tip)

			rez.push_back(elem);

	return rez;
}
