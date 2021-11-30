#include "Service.h"
#include "Domain.h"
#include "Repository.h"

std::vector<Film> Service_filme::get_all() noexcept(false) {

	return this->repo.get_all();
}

int Service_filme::cauta_film(int id) {

	Film f(id, "a", "a", 1, "a");

	this->valid.valideaza(f);

	const bool rez = this->repo.cauta_film(id);

	if (rez == true)

		return 1;

	throw SrvError("Filmul cautat nu exista!\n");}

void Service_filme::adauga_film(int id, const std::string titlu, const std::string gen, const int an, const std::string actor) {

	Film f(id, titlu, gen, an, actor);

	this->valid.valideaza(f);

	this->repo.adauga_film(f);

	undoActions.push_back(std::make_unique<UndoAdauga>(repo, f));
}

void Service_filme::sterge_film(int id) {

	Film f(id, "a", "a", 1, "a");

	this->valid.valideaza(f);

	Film f_sters = this->repo.sterge_film(id);

	undoActions.push_back(std::make_unique<UndoSterge>(repo, f_sters));

}

void Service_filme::modifica_titlu_film(int id, const std::string titlu_nou) {

	Film f(id, titlu_nou, "a", 1, "a");

	this->valid.valideaza(f);

	Film f_modificat = this->repo.modifica_titlu_film(id, titlu_nou);

	undoActions.push_back(std::make_unique<UndoModificaTitlu>(repo, f_modificat));
}

void Service_filme::modifica_gen_film(int id, const std::string gen_nou) {

	Film f(id, "a", gen_nou, 1, "a");

	this->valid.valideaza(f);

	Film f_modificat = this->repo.modifica_gen_film(id, gen_nou);

	undoActions.push_back(std::make_unique<UndoModificaGen>(repo, f_modificat));
}

void Service_filme::modifica_anul_film(int id, const int an_nou) {

	Film f(id, "a", "a", an_nou, "a");

	this->valid.valideaza(f);

	Film f_modificat = this->repo.modifica_anul_film(id, an_nou);

	undoActions.push_back(std::make_unique<UndoModificaAn>(repo, f_modificat));
}

void Service_filme::modifica_actor_film(int id, const std::string actor_nou) {

	Film f(id, "a", "a", 1, actor_nou);

	this->valid.valideaza(f);

	Film f_modificat = this->repo.modifica_actor_film(id, actor_nou);

	undoActions.push_back(std::make_unique<UndoModificaActor>(repo, f_modificat));
}

const Film& Service_filme::get_item_by_id(int i) {

	return this->repo.get_item_by_id(i);
}

std::vector<Film> Service_filme::filtrare_titlu(std::string titlu) { // copy if

	std::vector<Film> lista = this->repo.get_all();
	std::vector<Film> lista_filtrata(lista.size());

	/*for (unsigned int i = 0; i < lista.size(); i++) {	// - var 1

		Film f = lista.at(i);

		if (f.get_titlu().find(titlu) <= f.get_titlu().size() - 1)

			lista_filtrata.push_back(f);
	}*/

	/*for (auto& f : lista) { // - var 2

		if (f.get_titlu().find(titlu) <= f.get_titlu().size() - 1)

			lista_filtrata.push_back(f);
	}*/

	auto it = std::copy_if(lista.begin(), lista.end(), lista_filtrata.begin(), [titlu](Film f) {return f.get_titlu().find(titlu) <= f.get_titlu().size() - 1; });

	lista_filtrata.resize(std::distance(lista_filtrata.begin(), it));

	return lista_filtrata;
}

std::vector<Film> Service_filme::filtrare_an(int an) { // copy if

	std::vector<Film> lista = this->repo.get_all();
	std::vector<Film> lista_filtrata(lista.size());

	/*for (unsigned int i = 0; i < lista.size(); i++) {

		Film f = lista.at(i);

		if (f.get_an_aparitie() <= an)

			lista_filtrata.push_back(f);
	}*/

	/*for (auto& f : lista) {

		if (f.get_an_aparitie() <= an)

			lista_filtrata.push_back(f);
	}*/

	auto it = std::copy_if(lista.begin(), lista.end(), lista_filtrata.begin(), [an](Film f) noexcept {return f.get_an_aparitie() <= an; });

	lista_filtrata.resize(std::distance(lista_filtrata.begin(), it));

	return lista_filtrata;
}

bool Service_filme::comparator(std::string camp, std::string ordine, const Film f1, const Film f2) {

	if (camp == "titlu") {

		if (ordine == "crescator")

			return f1.get_titlu() <= f2.get_titlu();

		return f1.get_titlu() >= f2.get_titlu();}

	else if (camp == "actor") {

		if (ordine == "crescator")

			return f1.get_actor_principal() <= f2.get_actor_principal();

		return f1.get_actor_principal() >= f2.get_actor_principal();}

	else {	//if (camp == "an si gen")

		if (ordine == "crescator") {

			if (f1.get_an_aparitie() != f2.get_an_aparitie())

				return f1.get_an_aparitie() <= f2.get_an_aparitie();

			else

				return f1.get_gen() <= f2.get_gen();}

		else {

			if (f1.get_an_aparitie() != f2.get_an_aparitie())

				return f1.get_an_aparitie() >= f2.get_an_aparitie();

			else

				return f1.get_gen() >= f2.get_gen();}}}

std::vector<Film> Service_filme::sortare_filme(std::string camp, std::string ordine) {

	std::vector<Film> lista_sortata = this->repo.get_all();

	/*for(unsigned int i = 0; i < lista_sortata.size() - 1; i++)

		for(unsigned int j = i + 1; j < lista_sortata.size(); j++)

			if (comparator(camp, ordine, lista_sortata.at(i), lista_sortata.at(j)) == false) {	// ceea ce inseamna ca nu sunt in ordine

				Film aux = lista_sortata.at(i);
				lista_sortata.at(i) = lista_sortata.at(j);
				lista_sortata.at(j) = aux;
			}*/

	std::sort(lista_sortata.begin(), lista_sortata.end(), [camp, ordine, this](Film f1, Film f2) {return comparator(camp, ordine, f1, f2); });

	return lista_sortata;
}

void Service_filme::goleste_cos() noexcept {

	this->cos.goleste_cos();
}

void Service_filme::adauga_in_cos(string titlu) {

	Film f = this->repo.get_item_by_title(titlu);

	this->cos.adauga_in_cos(f);
}

void Service_filme::adauga_random_cos(unsigned int numar_total) {

	//vector<Film> v = this->repo.get_all();

	this->cos.genereaza_cos(numar_total);
}

void Service_filme::exporta_fisier(const string& nume_fisier) {

	this->cos.exporta(nume_fisier);
}

int Service_filme::numar_filme_cos() noexcept {

	return this->cos.numar_filme();
}

vector<Film> Service_filme::get_cos_filme() {

	return this->cos.get_cos();
}

std::map<std::string, int> Service_filme::raport() {

	vector<Film> list = this->repo.get_all();
	std::map<std::string, int> rez;

	for (const auto& el : list)
		rez[el.get_gen()] = 0;

	for (const auto& el : list)
		rez[el.get_gen()]++;

	return rez;
}

void Service_filme::undo() {

	if (undoActions.empty()) {

		throw SrvError("Nu au fost efectuate modificari asupra listei!\n");
	}

	undoActions.back()->doUndo();
	undoActions.pop_back();
}