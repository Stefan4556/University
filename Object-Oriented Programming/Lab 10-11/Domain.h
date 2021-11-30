#pragma once
#include <iostream>
#include <string>

/*
*	Aceasta este clasa Film ce initializeaza obiectele de tipul film, ce contin:
*
*			- id - int
*			- titlu - string
*			- gen - string
*			- am - int
*			- actor_principal - string
*
*	De asemenea sunt observate si metodele aferente acestei clase, acestea fiind specificate mai jos.
*/
class Film {

private:

	std::string titlu;

	std::string gen;

	int an_aparitie;

	int id;

	std::string actor_principal;

public:

	/*
	*	Aceasta functie reprezinta constructorul clasei Film ce initializeaza cele 4 campuri ale unui film
	*	Preconditii: id - sa fie pozitiv
	*				 titlu - diferit de null
	*				 gen - diferit de null
	*				 an_aparitie - mai mare strict decat 0
	*				 actor - diferit de null
	*	Param de intrare: id - int
	*				 titlu - string
	*				 gen - string
	*				 an_aparitie - int
	*				 actor - string
	*	Param de iesire: un obiect de tipul film
	*	Postconditii: sa se creeze cu succes filmul
	*/
	Film(int id, const std::string titlu, const std::string gen, const int an_aparitie, const std::string actor_principal);

	Film(const Film& f) :id{ f.id }, titlu{ f.titlu }, gen{ f.gen }, an_aparitie{ f.an_aparitie }, actor_principal{ f.actor_principal }{

		//std::cout << "S-a copiat!\n";
	}

	Film() noexcept(false) :id{ -1 }, titlu{ "a" }, gen{ "a" }, an_aparitie{ 1 }, actor_principal{ "a" }{

	};

	Film& operator=(const Film& f) = default;

	/*
	*	Aceasta functie returneaza titlul unui film
	*	Preconditii: sa existe filmul
	*	Param de intrare: sa avem un obiect de tipul film
	*	Param de iesire: un string ce reprezinta titlul filmului
	*	Postconditii: stringul returnat sa fie diferit de null
	*/
	std::string get_titlu() const;

	/*
	*	Aceasta functie returneaza genul unui film
	*	Preconditii: sa existe filmul
	*	Param de intrare: sa avem un obiect de tipul film
	*	Param de iesire: un string ce reprezinta genul filmului
	*	Postconditii: stringul returnat sa fie diferit de null
	*/
	std::string get_gen() const;

	/*
	*	Aceasta functie returneaza anul unui film
	*	Preconditii: sa existe filmul
	*	Param de intrare: sa avem un obiect de tipul film
	*	Param de iesire: o valoare intreaga mai mare decat 0
	*	Postconditii: valoarea returnata sa fie valida
	*/
	int get_an_aparitie() const noexcept;

	/*
	*	Aceasta functie returneaza id-ul unui film
	*	Preconditii: sa existe filmul
	*	Param de intrare: sa avem un obiect de tipul film
	*	Param de iesire: o valoare intreaga mai mare decat 0
	*	Postconditii: valoarea returnata sa fie valida
	*/
	int get_id() const noexcept;

	/*
	*	Aceasta functie returneaza actorul principal unui film
	*	Preconditii: sa existe filmul
	*	Param de intrare: sa avem un obiect de tipul film
	*	Param de iesire: un string ce reprezinta actorul principal al filmului
	*	Postconditii: stringul returnat sa fie diferit de null
	*/
	std::string get_actor_principal() const;

	/*
	*	Aceasta functie seteaza id-ul unui film
	*	Preconditii: sa existe filmul, id_nou > 0
	*	Param de intrare: sa avem un obiect de tipul film
						  id_nou - int
	*	Param de iesire: obiectul modificat
	*	Postconditii: id ul nou sa fie egal cu cel primit ca parametru
	*/
	void set_id(int id_nou) noexcept;

	/*
	*	Aceasta functie seteaza titlul unui film
	*	Preconditii: sa existe filmul, titlul_nou != vid
	*	Param de intrare: sa avem un obiect de tipul film
						  titlu_nou - string
	*	Param de iesire: obiectul modificat
	*	Postconditii: titlul nou sa fie egal cu cel primit ca parametru
	*/
	void set_titlu(const std::string titlu_nou);

	/*
	*	Aceasta functie seteaza genul unui film
	*	Preconditii: sa existe filmul, gen_nou != vid
	*	Param de intrare: sa avem un obiect de tipul film
						  gen_nou - string
	*	Param de iesire: obiectul modificat
	*	Postconditii: genul nou sa fie egal cu cel primit ca parametru
	*/
	void set_gen(const std::string gen_nou);

	/*
	*	Aceasta functie seteaza anul unui film
	*	Preconditii: sa existe filmul, an_nou > 0
	*	Param de intrare: sa avem un obiect de tipul film
						  an_nou - int
	*	Param de iesire: obiectul modificat
	*	Postconditii: anul nou sa fie egal cu cel primit ca parametru
	*/
	void set_an_aparitie(const int an_aparitie_nou) noexcept;

	/*
	*	Aceasta functie seteaza actorul unui film
	*	Preconditii: sa existe filmul, actor_principal_nou != vid
	*	Param de intrare: sa avem un obiect de tipul film
						  actor_principal_nou - string
	*	Param de iesire: obiectul modificat
	*	Postconditii: actor principal nou sa fie egal cu cel primit ca parametru
	*/
	void set_actor_principal(const std::string actor_principal_nou);

	//bool operator ==(Film f);

};

/*
*	Clasa Validator se ocupa cu retinerea unei metode numita valideaza, ce se ocupa cu validarea unui film
*/
class Validator {

public:

	/*
	*	Rolul acestei functii este de a valida un film
	*	Preconditii: nu avem
	*	Param de intrare: f - Film
	*	Param de iesire: rez - int
	*	Postconditii: rez = 0 daca filmul este valid, altfel este invalid si returneaza un cod specific unor erori
	*/
	void valideaza(const Film& film);

};

/*
*	Clasa POSError se ocupa cu creearea obiectelor ce reprezinta erori si retinerea metodelor aferente acesteia
*/
class POSError {

public:

	/*
	*	Constructorul clasei ce actualizeaza unicul camp al acesteia si anume un string
	*	Preconditii: message dif de null
	*	Param de intrare: message - string
	*	Param de iesire: obiect de tipul POSError
	*	Postconditii: campul message sa fie actualizat
	*/
	POSError(std::string message) :
		message(message) {

	}

	/*
	*	Rolul acestei metode este de a returna mesajul aferent erorii
	*	Preconditii: obiectul sa existe
	*	Param de intrare: avem implicit obiectul de tip POSError
	*	Param de iesire: un string ce reprezinta mesajul
	*	Postconditii: nu avem
	*/
	const std::string& getMessage() const noexcept {
		return message;
	}

private:

	std::string message;
};

class ValidationError : public POSError {

public:

	/*
	*	Constructorul clasei ValidationError ce retine erorile ce pot aparea la nivelul validatorului
	*	Preconditii: string diferit de null
	*	Param de intrare: message - string
	*	Param de iesire: se retine eroarea
	*	Postconditii: eroarea sa fie retinuta cu succes
	*/
	ValidationError(std::string message) :
		POSError(message) {

	}
};
/*
class DTO {

private:

	std::string tip;
	int count;

public:

	DTO(const std::string& tip, int count);

	std::string get_tip() {

		return tip;
	}

	int
};*/
