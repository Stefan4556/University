#include "Service.h"

vector<Carte> Service_carti::get_all()
{
	return this->repo.get_all();
}

Carte Service_carti::get_item_by_title(string titlu)
{
	return this->repo.get_item_by_title(titlu);
}

vector<Carte> Service_carti::sortare_dupa_grosime()
{
	vector<Carte> rez = this->repo.get_all();

	for (int i = 0; i < rez.size() - 1; i++)

		for (int j = i + 1; j < rez.size(); j++)

			if (rez[i].get_grosime() > rez[j].get_grosime())

				std::swap(rez[i], rez[j]);

	return rez;
}

vector<Carte> Service_carti::sortare_dupa_titlu()
{
	vector<Carte> rez = this->repo.get_all();

	for (int i = 0; i < rez.size() - 1; i++)

		for (int j = i + 1; j < rez.size(); j++)

			if(rez[i].get_titlu() > rez[j].get_titlu())

				std::swap(rez[i], rez[j]);

	return rez;
}
