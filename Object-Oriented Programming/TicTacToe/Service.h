#pragma once
#include "Repository.h"

class Service {

private:

	Repository& repo;
	Validator& val;

public:

	Service(Repository& repo, Validator& val) : repo{ repo }, val{ val }{};

	vector<Joc> get_all();

	void adauga_joc(int dim, string tabla, string jucator);

	vector<Joc> sortare_stare();

	void modifica_joc(int id, int dim, string tabla, string jucator, string stare);

	Joc get_item_by_id(int id);
};