#include<iostream>
#include <string>
#include <vector>
#include "VectorDinamic.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"

/*
*	Aceasta este clasa Console ce se ocupa cu gestiunea interfetei grafice si cu preluarea comenziilor de la utilizator
*		
*		- campul service retine legatura dintre ui si service
*/
class Console {

private:

	Service_filme& service;

	/*
	*	Rolul acestei functii este de a afisa meniul pe care utilizatorul il vede in momentul in care porneste aplicatia
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void afiseaza_meniu();

	/*
	*	Rolul acestei functii este de a apela functia ce se ocupa cu adaugarea unui element in lista de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void adauga_film();

	/*
	*	Rolul acestei functii este de a afisa lista de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void afisare_filme(std::vector<Film> lista);

	/*
	*	Rolul acestei functii este de a apela functia ce se ocupa cu stergerea unui element din lista de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void sterge_film();

	/*
	*	Rolul acestei functii este de a apela functia ce se ocupa cu, cautarea unui element in lista de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void cauta_film();

	/*
	*	Rolul acestei functii este de a apela functia ce se ocupa cu modificarea unui element din lista de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void modifica_film();

public:

	/*
	*	Rolul acestei functii este de a initializa legatura dintre utilziator si cod
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	Console(Service_filme& srv)noexcept;

	/*
	*	Rolul acestei functii este de a realiza filtrarea filmelor dupa titlu sau dupa anul aparitiei
	*	Preconditii: lista sa nu fie vida
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void filtrare_filme();

	/*
	*	Rolul acestei functii este de a realiza sortarea filmelor din lista dupa un anumit camp
	*	Preconditii: lista sa nu fie vida
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void sortare_filme();

	/*
	*	Rolul acestei functii este de a citi si adauga un film in cos dupa titlu
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: poate arunca eroare daca nu exista un film cu id-ul respectiv
	*/
	void adauga_cos_titlu();

	/*
	*	Rolul acestei functii este de a citi si adauga un numar de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: poate arunca eroare daca nu exista atatea filme in lista de filme
	*/
	void adauga_cos_random();

	/*
	*	Rolul acestei functii este de a goli cosul de filme curent
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void goleste_cos();

	/*
	*	Rolul acestei functii este de a exporta intr-un fisier citit de la tastatura continutul cosului curent de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void export_cos();

	/*
	*	Rolul acestei functii este de a afisa continutul cosului de filme curent
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void afiseaza_cos();

	/*
	*	Rolul acestei functii este de a creea un raport ce este retinut sub forma de dictionar, al caror chei este format din genuri de filme si val este numarul de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void cerinta_lab_raport();

	/*
	*	Rolul acestei functii este de a apela functia de undo din service, functie ce reface operatia pe care lista a suferit-o
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void undo_lista();

	/*
	*	Rolul acestei functii este de a porni aplicatia
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: nu avem
	*/
	void run();

};