#pragma once

#include "Domain.h"
#include <vector>

class RepoAbstract {

public:

	virtual void adauga_film(const Film& f) = 0;

	virtual Film sterge_film(int id) = 0;

	virtual const std::vector<Film> get_all() const = 0;

	virtual int dimensiune() const = 0;

	virtual bool cauta_film(int id_cautat) = 0;

	virtual Film modifica_titlu_film(int id, const std::string titlu_nou) = 0;

	virtual Film modifica_gen_film(int id, const std::string gen_nou) = 0;

	virtual Film modifica_anul_film(int id, const int an_nou) = 0;

	virtual Film modifica_actor_film(int id, const std::string actor_nou) = 0;

	virtual const Film& get_item_by_id(int i) = 0;

	virtual Film get_item_by_title(std::string titlu) = 0;

	virtual ~RepoAbstract() = default;
};