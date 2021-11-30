#pragma once

#include "Domain.h"
#include <vector>
#include <fstream>

using std::vector;

class Repository_carti {

private:

	vector<Carte> lista_carti;

	string nume_fisier;

public:

	Repository_carti(string nume_fisier) : nume_fisier{ nume_fisier } {

		load_from_file();
	}

	void load_from_file();

	vector<Carte> get_all();

	Carte get_item_by_title(string titlu);
};