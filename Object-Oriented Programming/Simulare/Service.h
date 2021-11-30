#pragma once

#include "Repository.h"

class Service_carti {

private:

	Repository_carti& repo;

public:

	Service_carti(Repository_carti& repo) : repo{ repo } {

	};

	vector<Carte> get_all();

	Carte get_item_by_title(string titlu);

	vector<Carte> sortare_dupa_grosime();

	vector<Carte> sortare_dupa_titlu();
};