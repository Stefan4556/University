#pragma once
//#include <string>
//#include <vector>
//#include <fstream>
#include <algorithm>
#include <random>
#include <chrono>
//#include "Domain.h"
#include "Repository.h"
#include "Observer.h"

using std::string;
using std::vector;

class Cos : public Observable{

private:

	vector<Film> lista;
	RepoAbstract& repo;

public:

	//Cos(Repository_filme& repo) noexcept;

	Cos(RepoAbstract& repo) : repo{ repo } {};

	/*
	*	Rolul acestei metode este de a goli cosul curent de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: cosul de filme sa fie gol
	*/
	void goleste_cos() noexcept;

	/*
	*	Rolul acestei metode este de a adauga un film in cos
	*	Preconditii: f sa existe
	*	Param de intrare: f - Film
	*	Param de iesire: nu avem
	*	Postconditii: sa fie adaugat filmul
	*/
	void adauga_in_cos(const Film& f);

	/*
	*	Rolul acestei metode este de a adauga un numar de filme
	*	Preconditii: numar_total sa fie pozitiv
	*	Param de intrare: lis - lista de filme, numar_total - unsigned int
	*	Param de iesire: nu avem
	*	Postconditii: sa fie adaugate in cos un numar de filme primit ca parametru alese random din lista trimisa tot ca parametru
	*/
	void genereaza_cos(unsigned int numar_total);

	/*
	*	Rolul acestei metode este de a returna numarul de filme din cosul curent
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: rez - int
	*	Posconditii: numarul returnat sa fie mai mare sau egal decat 0
	*/
	void exporta(const string& nume_fisier);

	/*
	*	Rolul acestei metode este de a returna numarul de filme din cosul curent
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: rez - int
	*	Posconditii: numarul returnat sa fie mai mare sau egal decat 0
	*/
	int numar_filme() noexcept;

	/*
	*	Rolul acestei metode este de a returna cosul de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: un vector de filme
	*	Postconditii: nu avem
	*/
	vector<Film> get_cos();

	/*
	*	Rolul acestei metode este de a sterge din cos, filmele ce sunt sterse din lista de filme
	*	Preconditii: id sa fie valid
	*	Param de intrare: id - int
	*	Param de iesire: nu avem
	*	Postconditii: cosul sa nu mai contina filme cu id-ul primit ca parametru
	*/
	//void mentenanta_stergere(int id);

};

class CosError : public POSError {

public:

	CosError(string message) : POSError(message) {

	}
};