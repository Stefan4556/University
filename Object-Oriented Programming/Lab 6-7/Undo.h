#pragma once
#include "Domain.h"
#include "Repository.h"
#include "RepoAbstract.h"

// clasa abstracta
class ActiuneUndo {

public:
	
	virtual void doUndo() = 0;	// metoda pur virtuala

	//ActiuneUndo()noexcept = default;

	//ActiuneUndo(const ActiuneUndo&) = default;

	//ActiuneUndo& operator=(const ActiuneUndo&) = default;

	//ActiuneUndo(ActiuneUndo&&) = default;

	//ActiuneUndo& operator=(ActiuneUndo&&) = default;

	virtual ~ActiuneUndo() = default;
};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoAdauga : public ActiuneUndo {

	Film filmAdaugat;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoAdauga
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoAdauga
	*	Postconditii: nu avem
	*/
	UndoAdauga(RepoAbstract& rep, const Film& f) :rep { rep }, filmAdaugat{ f } {}

	/*
	*	Aceasta metoda realizeaza operatia inversa adaugarii, si anume stergerea
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes stergerea filmului adaugat
	*/
	void doUndo() override {

		const int id = filmAdaugat.get_id();
		rep.sterge_film(id);
	}

};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoSterge : public ActiuneUndo {

	Film filmSters;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoSterge
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoSterge
	*	Postconditii: nu avem
	*/
	UndoSterge(RepoAbstract& repo, const Film& f) : rep{ repo }, filmSters{ f } {}

	/*
	*	Aceasta metoda realizeaza operatia inversa stergerii, si anume adaugarea
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes adaugarea filmului sters
	*/
	void doUndo() override {

		rep.adauga_film(filmSters);
	}
};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoModificaTitlu : public ActiuneUndo {

	Film filmModificat;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoModificaTitlu
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoModificaTitlu
	*	Postconditii: nu avem
	*/
	UndoModificaTitlu(RepoAbstract& repo, const Film& f) : rep{ repo }, filmModificat{ f }{};

	/*
	*	Aceasta metoda realizeaza operatia inversa modificarii, si anume modificarea la starea initiala
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes modificarea filmului la starea initiala
	*/
	void doUndo() override {

		rep.modifica_titlu_film(filmModificat.get_id(), filmModificat.get_titlu());
	}
};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoModificaGen : public ActiuneUndo {

	Film filmModificat;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoModificaGen
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoModificaGen
	*	Postconditii: nu avem
	*/
	UndoModificaGen(RepoAbstract& repo, const Film& f) : rep{ repo }, filmModificat{ f }{};

	/*
	*	Aceasta metoda realizeaza operatia inversa modificarii, si anume modificarea la starea initiala
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes modificarea filmului la starea initiala
	*/
	void doUndo() override {

		rep.modifica_gen_film(filmModificat.get_id(), filmModificat.get_gen());
	}
};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoModificaAn : public ActiuneUndo {

	Film filmModificat;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoModificaAn
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoModificaAn
	*	Postconditii: nu avem
	*/
	UndoModificaAn(RepoAbstract& repo, const Film& f) : rep{ repo }, filmModificat{ f }{};

	/*
	*	Aceasta metoda realizeaza operatia inversa modificarii, si anume modificarea la starea initiala
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes modificarea filmului la starea initiala
	*/
	void doUndo() override {

		rep.modifica_anul_film(filmModificat.get_id(), filmModificat.get_an_aparitie());
	}
};

/*
*	Rolul acestei clase este de a retine constructorul si functia ce este apelata in momentul in care este construit un astfel de obiect
*/
class UndoModificaActor : public ActiuneUndo {

	Film filmModificat;
	//Repository_filme& rep;
	RepoAbstract& rep;

public:

	/*
	*	Aceasta metoda reprezinta constructorul obiectelor de tipul UndoModificaActor
	*	Preconditii: f sa fie valid
	*	Param de intrare: rep - Repository_film, f - Film
	*	Param de iesire: un obiect de tipul UndoModificaActor
	*	Postconditii: nu avem
	*/
	UndoModificaActor(RepoAbstract& repo, const Film& f) : rep{ repo }, filmModificat{ f }{};

	/*
	*	Aceasta metoda realizeaza operatia inversa modificarii, si anume modificarea la starea initiala
	*	Preconditii: nu avem
	*	Param de intrare: avem implicit un film si repo-ul
	*	Param de iesire: nu avem
	*	Postconditii: sa fie efectuata cu succes modificarea filmului la starea initiala
	*/
	void doUndo() override {

		rep.modifica_actor_film(filmModificat.get_id(), filmModificat.get_actor_principal());
	}
};
