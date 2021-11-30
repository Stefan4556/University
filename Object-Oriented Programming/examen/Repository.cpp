#include "Repository.h"
#include <fstream>

void Repository::load_from_file()
{
	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id;
		double pret;
		string titlu, tip;

		in >> id; 

		if (in.eof())

			break;

		in >> titlu >> tip >> pret;

		Carte c{ id, titlu, tip, pret };
		this->lista.push_back(c);
	}
	in.close();
}

void Repository::write_to_file()
{
	std::ofstream out(this->nume_fisier);

	for (auto el : this->lista) {

		out << el.get_id() << '\n';
		out << el.get_titlu() << '\n';
		out << el.get_tip() << '\n';
		out << el.get_pret() << '\n';
	}
}

vector<Carte> Repository::get_all()
{
	return this->lista;
}

void Repository::adauga_carte(Carte c)
{

	string erori = "";

	for (auto el : this->lista) {

		if (el.get_id() == c.get_id())

			erori += "Mai exista o carte cu acest id!\n";

		if (el.get_titlu() == c.get_titlu())

			erori += "Nu putem avea doua carti cu acelasi titlu!\n";

		if (erori != "")

			throw erori;
	}

	this->lista.push_back(c);
	write_to_file();
}
