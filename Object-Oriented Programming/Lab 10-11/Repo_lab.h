#pragma once

#include "Domain.h"
#include "RepoAbstract.h"
#include "Repository.h"
#include <unordered_map>
#include <vector>

class RepoLab : public RepoAbstract {

private:

	std::unordered_map<int, Film> lista_filme;

	double probabilitate;

public:

	RepoLab(double probabilitate) : probabilitate{ probabilitate } {};

	void adauga_film(const Film& f) override;

	Film sterge_film(int id) override;

	const std::vector<Film> get_all() const override;

	int dimensiune() const override;

	bool cauta_film(int id_cautat) override;

	Film modifica_titlu_film(int id, const std::string titlu_nou) override;

	Film modifica_gen_film(int id, const std::string gen_nou) override;

	Film modifica_anul_film(int id, const int an_nou) override;

	Film modifica_actor_film(int id, const std::string actor_nou) override;

	const Film& get_item_by_id(int i) override;

	Film get_item_by_title(std::string titlu) override;

};
/*
class RepoError : public POSError {

public:

	/*
	*	Constructorul clasei RepoError ce retine erorile ce pot aparea la nivelul repositoryului
	*	Preconditii: string diferit de null
	*	Param de intrare: message - string
	*	Param de iesire: se retine eroarea
	*	Postconditii: eroarea sa fie retinuta cu succes
	*
	RepoError(std::string message) :

		POSError(message) {

	}
};
*/