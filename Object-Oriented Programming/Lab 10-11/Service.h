#pragma once
//#include "Repository.h"
//#include "Domain.h"
//#include "VectorDinamic.h"
#include "Cos.h"
#include "Undo.h"
//#include "RepoAbstract.h"
#include <algorithm>
#include <map>
#include <memory>
#include <list>

using std::unique_ptr;
using std::vector;

/*
*		Aceasta este clasa Serivce_filme ce se ocupa cu realizarea legaturii dintre ui, domain si repo si are ca si campuri:
*
*			- repo - legatura catre repo
*			- valid - legatura catre validator
*/
class Service_filme {

private:

	RepoAbstract& repo;
	Validator& valid;
	Cos& cos;
	vector<unique_ptr<ActiuneUndo>> undoActions;

public:

	/*
	*	Rolul acestei functii este de a initializa legaturile intre ui, repo si domain
	*	Preconditii: repo-ul sa fie initializat, validatorul sa fie initializat
	*	Param de intrare: repo_filme - Repository_filme, validator - Validator
	*	Param de iesire: sunt actualizate campurile clasei service
	*	Postconditii: sa fie realizate corect legaturile
	*/
	Service_filme(RepoAbstract& repo_filme, Validator& validator, Cos& cos) noexcept : repo{ repo_filme }, valid{ validator }, cos{ cos } {};

	/*
	*	Rolul acestei functii este de a returna lista de filme
	*	Preconditii: lista sa nu fie vida
	*	Param de intrare: nu avem
	*	Param de iesire: returneaza lista de filme
	*	PostconditiiL lista de filem sa nu fie vida
	*/
	std::vector<Film> get_all() noexcept(false);

	/*
	*	Rolul acestei functii este de a cauta filmul corespunzator unui id prmit ca si parametru
	*	Preconditii: lista sa nu fie vida, id ul urmeaza sa fie validat
	*	Param de intrare: id - int
	*	Param de iesire: rez - int care returneaza ori un code de eroare ori ca a fost adaugat ori ca nu exista
	*	Postconditii: fiecare valaore returnata are o semnificatie
	*/
	int cauta_film(int id);

	/*
	*	Rolul acestei functii este de a adauga un nou film in lista noastra
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*					  titlu - string
	*					  an - int
	*				      actor - string
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare ori faptul ca s a adaugat
	*	Postconditii: rezultatul sa fie intreg
	*/
	void adauga_film(int id, const std::string titlu, const std::string gen, const int an, const std::string actor);

	/*
	*	Rolul acestei functii este de a sterge un film cu id ul primit ca si parametru
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	void sterge_film(int id);

	/*
	*	Rolul acestei functii este de a modifica titlul unui film al carui id este transmis ca parametru
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*					  titlu_nou - string
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	void modifica_titlu_film(int id, const std::string titlu_nou);

	/*
	*	Rolul acestei functii este de a genul unui film al carui id este transmis ca parametru
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*					  gen_nou - string
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	void modifica_gen_film(int id, const std::string gen_nou);

	/*
	*	Rolul acestei functii este de a modifica anul unui film al carui id este transmis ca parametru
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*					  an_nou - int
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	void modifica_anul_film(int id, const int an_nou);

	/*
	*	Rolul acestei functii este de a modifica actorul principal al unui film al carui id este transmis ca parametru
	*	Preconditii: nu avem
	*	Param de intrare: id - int
	*					  actor_nou - string
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	void modifica_actor_film(int id, const std::string actor_nou);

	/*
	*	Rolul acestei functii este de a returna un obiect corespunzator unui id
	*	Preconditii: nu avem
	*	Param de intrare: i - int
	*	Param de iesire: returneaza un cod ce reprezinta ori o eroare, ori faptul ca s a adaugat cu succes
	*	Postconditii: rezultatul sa fie intreg
	*/
	const Film& get_item_by_id(int i);

	/*
	*	Rolul acestei functii este de a filtra lista de filme dupa un string citit de la tastatura
	*	Preconditii: string-ul introdus sa fie nevid
	*	Param de intrare: titlu - string
	*	Param de iesire: returneaza o lista de filme ce contin in titlu, string ul primit ca si parametru
	*	Postconditii: lista sa fie returnata corect
	*/
	std::vector<Film> filtrare_titlu(std::string titlu);

	/*
	*	Rolul acestei functii este de a filtra lista de filme dupa un an pe care il primeste ca si parametru
	*	Preconditii: anul primit ca si parametru sa fie valid
	*	Param de intrare: an - int
	*	Param de iesire: returneaza o lista de filme ce au anul mai mic sau egal decat cel trimis ca parametru
	*	Postconditii: lista sa fie returnata corect
	*/
	std::vector<Film> filtrare_an(int an);

	/*
	*	Rolul acestei functii este de a returna true sau false daca elementele sunt in ordine sau nu in functie de un camp si de o ordine
	*	Preconditii: camp - diferit de null, ordine - diferit de null
	*	Param de intrare: camp - string, ordine - string, f1 - Film, f2 - Film
	*	Param de iesire: returneaza true sau false daca cele 2 filme sunt sau nu sunt in ordine
	*	Postconditii: nu avem
	*/
	bool comparator(std::string camp, std::string ordine, const Film f1, const Film f2);

	/*
	*	Rolul acestei functii este de a sorta o lista de filem dupa un anumit camp si intr o anumita ordine
	*	Preconditii: camp diferit de null si ordine diferita de null
	*	Param de intrare: camp - string, ordine - string
	*	Param de iesire: returneaza o lista de filme sortata dupa un anumit camp si ordonata intr o anumita ordine
	*	Postconditii: lista sa fie returnata corect
	*/
	std::vector<Film> sortare_filme(std::string camp, std::string ordine);

	/*
	*	Rolul acestei metode este de a goli cosul curent de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: nu avem
	*	Postconditii: cosul de filme sa fie gol
	*/
	void goleste_cos() noexcept;

	/*
	*	Rolul acestei metode este de a adauga dupa titlu un film in cos
	*	Preconditii: titlul sa fie valid
	*	Param de intrare: titlu - string
	*	Param de iesire: nu avem
	*	Postconditii: sa fie adaugat in cosul cu filme daca exista, filmul cu titlul primit ca parametru
	*/
	void adauga_in_cos(string titlu);

	/*
	*	Rolul acestei metode este de a adauga un numar de filme
	*	Preconditii: numar_total sa fie pozitiv
	*	Param de intrare: numar_total - unsigned int
	*	Param de iesire: nu avem
	*	Postconditii: sa fie adaugate in cos un numar de filme primit ca parametru
	*/
	void adauga_random_cos(unsigned int numar_total);

	/*
	*	Rolul acestei metode este de a exporta intr un fisier primit ca parametru cosul de cumparaturi
	*	Preconditii: numele fisierului sa fie valid
	*	Param de intrare: nume_fisier - string
	*	Param de iesire: o sa fie scris in fisier cosul de filme
	*	Postconditii: nu avem
	*/
	void exporta_fisier(const string& nume_fisier);

	/*
	*	Rolul acestei metode este de a returna numarul de filme din cosul curent
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: rez - int
	*	Posconditii: numarul returnat sa fie mai mare sau egal decat 0
	*/
	int numar_filme_cos() noexcept;

	/*
	*	Rolul acestei metode este de a returna cosul de filme
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: un vector de filme
	*	Postconditii: nu avem
	*/
	vector<Film> get_cos_filme();

	/*
	*	Cerinta laborator: dictionar ce contine perechi cheie valoare, unde cheia este genul, iar valoarea este numarul de filme de genul respectiv
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: un dictionar
	*	Postconditii: sa contina cel putin o pereche cheie valoare
	*/
	std::map<std::string, int> raport();

	/*
	*	Rolul acestei functii este de a realiza undo-ul, ce functioneaza in urmatorul fel, retine operatie inversa operatiei efectuate
	*	Preconditii: nu avem
	*	Param de intrare: avem unul implicit, si anume lista de undo
	*	Param de iesire: nu avem
	*	Postconditii: in cazul in care s-au efectuat modificari, lista sa fie adusa la forma ei inainte de a suferi modificarea respectiva
	*/
	void undo();


	// Rolul acestei metode este de a returna referinta la cosul de filme
	Cos& getCos() {

		return this->cos;
	}

};

class SrvError : public POSError {

public:

	/*
	*	Constructorul clasei SrvError ce retine erorile ce pot aparea la nivelul serviceului
	*	Preconditii: string diferit de null
	*	Param de intrare: message - string
	*	Param de iesire: se retine eroarea
	*	Postconditii: eroarea sa fie retinuta cu succes
	*/
	SrvError(std::string message) :

		POSError(message) {

	}
};