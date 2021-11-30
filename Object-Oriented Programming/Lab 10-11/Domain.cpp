#include "Domain.h"
#include <string>
#include <exception>

Film::Film(int id, const std::string titlu, const std::string gen, const int an_aparitie, const std::string actor_principal) {

	this->id = id;
	this->gen = gen;
	this->an_aparitie = an_aparitie;
	this->titlu = titlu;
	this->actor_principal = actor_principal;
}

std::string Film::get_titlu() const {

	return this->titlu;
}

std::string Film::get_gen() const {

	return this->gen;
}

int Film::get_an_aparitie() const noexcept {

	return this->an_aparitie;
}

std::string Film::get_actor_principal() const {

	return this->actor_principal;
}

int Film::get_id() const noexcept {

	return this->id;
}

void Film::set_id(int id_nou) noexcept {

	this->id = id_nou;
}

void Film::set_titlu(const std::string titlu_nou) {

	this->titlu = titlu_nou;
}

void Film::set_gen(const std::string gen_nou) {

	this->gen = gen_nou;
}

void Film::set_an_aparitie(const int an_aparitie_nou) noexcept {

	this->an_aparitie = an_aparitie_nou;
}

void Film::set_actor_principal(const std::string actor_principal_nou) {

	this->actor_principal = actor_principal_nou;
}
/*
bool Film::operator ==(Film f) {

	return this->id == f.get_id() && this->titlu == f.get_titlu() && this->gen == f.get_gen() && this->an_aparitie == f.get_an_aparitie() && this->actor_principal == f.get_actor_principal();
}*/

void Validator::valideaza(const Film& film) {

	std::string erori = "";

	if (film.get_id() <= 0)

		erori += "Id-ul nu poate sa fie un numar mai mic sau egal decat 0!\n";

	if (film.get_titlu() == "")

		erori += "Titlul nu poate sa fie vid!\n";

	if (film.get_gen() == "")

		erori += "Genul filmului nu poate sa fie vid!\n";

	if (film.get_an_aparitie() <= 0)

		erori += "Anul filmului nu poate sa fie mai mic sau egal decat 0!\n";

	if (film.get_actor_principal() == "")

		erori += "Numele actorului principal nu poate sa fie vid!\n";

	if (erori != "")

		throw ValidationError(erori);

}