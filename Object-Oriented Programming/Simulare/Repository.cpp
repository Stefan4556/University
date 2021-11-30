#include "Repository.h"

void Repository_carti::load_from_file()
{
	std::ifstream f(this->nume_fisier);

	if (!f.is_open())

		return;

	while (!f.eof()) {

		string titlu, autor, culoare;
		int grosime;

		f >> titlu >> autor >> culoare >> grosime;

		Carte c(titlu, autor, culoare, grosime);

		this->lista_carti.push_back(c);
	}

	f.close();
}

vector<Carte> Repository_carti::get_all()
{
	return this->lista_carti;
}

Carte Repository_carti::get_item_by_title(string titlu)
{
	for (auto& c : this->lista_carti)

		if (c.get_titlu() == titlu)

			return c;}
