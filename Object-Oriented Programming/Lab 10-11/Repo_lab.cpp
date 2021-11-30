#include "Repo_lab.h"

const std::vector<Film> RepoLab::get_all() const {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	std::vector<Film> rez;

	for (const auto& el : this->lista_filme)

		rez.push_back(el.second);

	return rez;
}

int RepoLab::dimensiune() const {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	return this->lista_filme.size();
}

bool RepoLab::cauta_film(int id_cautat) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	std::unordered_map<int, Film>::const_iterator it = this->lista_filme.find(id_cautat);

	return it != this->lista_filme.end();
}

void RepoLab::adauga_film(const Film& f) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(f.get_id()) == false) {

		this->lista_filme[f.get_id()] = f;
		return;
	}

	throw RepoError("Acest film a mai fost adaugat o data!\n");
}

Film RepoLab::sterge_film(int id) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(id) == true) {

		Film fil = this->lista_filme[id];
		this->lista_filme.erase(id);
		return fil;
	}

	throw RepoError("Filmul pe care doriti sa-l stergeti nu exista!\n");
}

Film RepoLab::modifica_titlu_film(int id, const std::string titlu_nou) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(id) == true) {

		Film fil = this->lista_filme[id];
		this->lista_filme[id].set_titlu(titlu_nou);
		return fil;
	}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film RepoLab::modifica_gen_film(int id, const std::string gen_nou) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(id) == true) {

		Film fil = this->lista_filme[id];
		this->lista_filme[id].set_gen(gen_nou);
		return fil;
	}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film RepoLab::modifica_anul_film(int id, const int an_nou) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(id) == true) {

		Film fil = this->lista_filme[id];
		this->lista_filme[id].set_an_aparitie(an_nou);
		return fil;
	}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film RepoLab::modifica_actor_film(int id, const std::string actor_nou) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	if (cauta_film(id) == true) {

		Film fil = this->lista_filme[id];
		this->lista_filme[id].set_actor_principal(actor_nou);
		return fil;
	}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

const Film& RepoLab::get_item_by_id(int id) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	for (const auto& el : this->lista_filme)

		if (el.first == id)

			return el.second;

	throw RepoError("Nu exista in lista un film cu acest id!\n");}

Film RepoLab::get_item_by_title(std::string titlu) {

	const double p = static_cast<double>(static_cast <double> (rand()) / static_cast <double> (RAND_MAX));

	if (p < this->probabilitate)

		throw RepoError("Probabilitatea nu a fost in favoarea ta!\n");

	for (const auto& el : this->lista_filme)

		if (el.second.get_titlu() == titlu)

			return el.second;

	throw RepoError("Nu exista in lista un film cu acest nume!\n");}