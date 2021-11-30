#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include "Domain.h"
#include "VectorDinamic.h"
#include "RepoAbstract.h"

/*
*		Aceasta este clasa Repository filme ce se ocupa cu retinerea listei de filme si are o variabila:
*
*			- lista filme - vector
*
*		Mai jos sun prezentate si specificate metodele aferente acesteia.
*/
class Repository_filme : public RepoAbstract {

	//friend void teste_repo();

private:

	std::vector<Film> lista_filme;
	//std::string nume_fisier;

public:

	Repository_filme() = default;
	//Repository_filme(std::string nume_fis) : nume_fisier{ nume_fis } { read_from_file(); };

	/*
	*	Rolul acestei functii este de a returna lista de filme
	*	Preconditii: lista de filme sa fie nevida
	*	Param de intrare: nu avem, deoarece lista se afla in repo ca si camp
	*	Param de iesire: o lista de filme de tipul vector
	*	Postconditii: lista returnata sa nu fie vida
	*/
	const std::vector<Film> get_all() const noexcept(false) override;

	/*
	*	Rolul acestei functii este de a returna lungimea listei
	*	Preconditii: lista de filme sa fie nevdia
	*	Param de intrare: nu avem, deoarece lista se afla in repo ca si camp
	*	Param de iesire: dimensiunea listei ce reprezinta o valoare intreaga\
	*	Postconditii: dimensiunea sa fie mai mare sau egala decat 0
	*/
	int dimensiune() const noexcept override;

	/*
	*	Rolul acestei functii este de a verifica daca exista un film cu id-ul cautat
	*	Preconditii: lista de filme sa fie nevida si id ul sa fie valid
	*	Param de intrare: id_cautat - int
	*	Param de iesire: True - daca exista elementul cu id-ul primit ca si parametru, False - altfel
	*	Postconditii: returneaza true sau false
	*/
	bool cauta_film(int id_cautat) override;

	/*
	*	Rolul acestei functii este de a adauga un film in lista de filme
	*	Preconditii: filmul f sa fie valid
	*	Param de intrare: f - Film
	*	Param de iesire: nu avem, dar lista este adaugata
	*	Postconditii: lista sa contina elementul trimis ca parametru
	*/
	void adauga_film(const Film& f) override;

	/*
	*	Rolul acestei functii este de a sterge un film dupa id
	*	Preconditii: id-ul sa fie valid
	*	Param de intrare: id - int
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film sterge_film(int id) override;

	/*
	*	Rolul acestei functii este de a modifica titlul unui obiect cu un id trimis ca parametru
	*	Preconditii: id-ul sa fie valid, titlu_nou sa fie valid
	*	Param de intrare: id - int
	*					  titlu_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_titlu_film(int id, const std::string titlu_nou) override;

	/*
	*	Rolul acestei functii este de a modifica genul unui obiect cu un id trimis ca parametru
	*	Preconditii: id-ul sa fie valid, gen_nou sa fie valid
	*	Param de intrare: id - int
	*					  gen_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_gen_film(int id, const std::string gen_nou) override;

	/*
	*	Rolul acestei functii este de a modifica anul unui obiect cu un id trimis ca parametru
	*	Preconditii: id-ul sa fie valid, an_nou sa fie valid
	*	Param de intrare: id - int
	*					  an_nou - int
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_anul_film(int id, const int an_nou) override;

	/*
	*	Rolul acestei functii este de a modifica actorul principal unui obiect cu un id trimis ca parametru
	*	Preconditii: id-ul sa fie valid, actor_nou sa fie valid
	*	Param de intrare: id - int
	*					  actor_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_actor_film(int id, const std::string actor_nou) override;

	/*
	*	Rolul acestei functii este de a returna filmul corespunzator unui id primit ca parametru
	*	Preconditii: id ul primit sa fie valid, iar lista sa nu fie vida
	*	Param de intrare: i - int
	*	Param de iesire: filmul corespuznator id-ului i
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	const Film& get_item_by_id(int i) override;

	/*
	*	Rolul acestei functii este de a returna filmul corespunzator unui titlu primit ca parametru
	*	Preconditii: id ul primit sa fie valid, iar lista sa nu fie vida
	*	Param de intrare: titlu - string
	*	Param de iesire: filmul corespuznator titlului titlu
	*	Postconditii: daca exista este returnat filmul cu titlul primit ca parametru
	*/
	Film get_item_by_title(std::string titlu) override;

};

/*
*		Aceasta este clasa Repository filme cu fisiere si se ocupa cu retinerea fisierului unde sunt stocate filmele si initializarea repository-ului:
*
*			- nume_fisier - string
*
*		Mai jos sun prezentate si specificate metodele aferente acesteia.
*/
class Repository_filme_file : public Repository_filme {

	friend void teste_repo();

private:

	std::string nume_fisier;

public:

	/*
	*	Constructorul clasei Repository_filme_file ce se ocupa cu initializarea repository-ului
	*	Preconditii: nume_fis sa fie valid
	*	Param de intrare: nume_fis - string
	*	Param de iesire: nu avem
	*	Postconditii: filmele sa fie incarcate cu succes din fisier
	*/
	Repository_filme_file(std::string nume_fis) : nume_fisier{ nume_fis }, Repository_filme(){

		read_from_file();
	};

	/*
	*	Rolul acestei metode este de a citii si adauga in lista obiectele ce se regasesc in fisier
	*	Preconditii: fisierul sa fie valid si sa existe
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: filmele sa fie incarcate cu succes
	*/
	void read_from_file();

	/*
	*	Rolul acestei metode este de a actualiza fisierul in care se gasesc filmele din lista curenta
	*	Preconditii: fisierul sa fie valid si sa existe
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: fisierul sa fie actualizat cu succes
	*/
	void write_to_file();

	/*
	*	Rolul acestei functii este de a adauga un film in lista de filme si de a actualiza baza de date din spate
	*	Preconditii: filmul f sa fie valid
	*	Param de intrare: f - Film
	*	Param de iesire: nu avem, dar lista este adaugata
	*	Postconditii: lista sa contina elementul trimis ca parametru
	*/
	void adauga_film(const Film& f) override {

		Repository_filme::adauga_film(f);
		write_to_file();
	}

	/*
	*	Rolul acestei functii este de a sterge un film dupa id si de a actualiza baza de date din spate
	*	Preconditii: id-ul sa fie valid
	*	Param de intrare: id - int
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film sterge_film(int id) override {

		Film f = Repository_filme::sterge_film(id);
		write_to_file();
		return f;
	}

	/*
	*	Rolul acestei functii este de a modifica titlul unui obiect cu un id trimis ca parametru si de a actualiza baza de date din spate
	*	Preconditii: id-ul sa fie valid, titlu_nou sa fie valid
	*	Param de intrare: id - int
	*					  titlu_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_titlu_film(int id, const std::string titlu_nou) override {

		Film f = Repository_filme::modifica_titlu_film(id, titlu_nou);
		write_to_file();
		return f;
	}

	/*
	*	Rolul acestei functii este de a modifica genul unui obiect cu un id trimis ca parametru si de a actualiza baza de date din spate
	*	Preconditii: id-ul sa fie valid, gen_nou sa fie valid
	*	Param de intrare: id - int
	*					  gen_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_gen_film(int id, const std::string gen_nou) override {

		Film f = Repository_filme::modifica_gen_film(id, gen_nou);
		write_to_file();
		return f;
	}

	/*
	*	Rolul acestei functii este de a modifica anul unui obiect cu un id trimis ca parametru si de a actualiza baza de date din spate
	*	Preconditii: id-ul sa fie valid, an_nou sa fie valid
	*	Param de intrare: id - int
	*					  an_nou - int
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_anul_film(int id, const int an_nou) override {

		Film f = Repository_filme::modifica_anul_film(id, an_nou);
		write_to_file();
		return f;
	}

	/*
	*	Rolul acestei functii este de a modifica actorul principal unui obiect cu un id trimis ca parametru si de a actualiza baza de date din spate
	*	Preconditii: id-ul sa fie valid, actor_nou sa fie valid
	*	Param de intrare: id - int
	*					  actor_nou - string
	*	Param de iesire: f - Film
	*	Postconditii: daca exista este returnat filmul cu id ul primit ca parametru
	*/
	Film modifica_actor_film(int id, const std::string actor_nou) override {

		Film f = Repository_filme::modifica_actor_film(id, actor_nou);
		write_to_file();
		return f;
	}

};

class RepoError : public POSError {

public:

	/*
	*	Constructorul clasei RepoError ce retine erorile ce pot aparea la nivelul repositoryului
	*	Preconditii: string diferit de null
	*	Param de intrare: message - string
	*	Param de iesire: se retine eroarea
	*	Postconditii: eroarea sa fie retinuta cu succes
	*/
	RepoError(std::string message) :

		POSError(message) {

	}
};

