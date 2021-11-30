#pragma once
#include <vector>
#include "Domain.h"

using std::vector;

class Repository {

private:

	vector<Joc> lista;
	string nume_fisier;

public:

	Repository(string nume_fis) : nume_fisier{ nume_fis } {

		load_from_file();
	}

	void load_from_file();

	void write_to_file();

	vector<Joc> get_all();

	void adauga_joc(Joc j);

	void modifica_joc(int id, int dim, string tabla, string jucator, string stare);

	Joc get_item_by_id(int id);
};