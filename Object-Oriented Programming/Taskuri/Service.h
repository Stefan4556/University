#pragma once
#include "Repository.h"
#include "Observer.h"

// clasa service leaga GUI de restul aplicatiei
class Service : public Observable{

private:

	Repository& repo;
	Validator& val;

public:

	// constructorul primeste legatura catre validator si repo
	Service(Repository& repo, Validator& val) : repo{ repo }, val{ val }{};

	// returnam lista de taskuri
	vector<Task> get_all();

	// sortam crecsator dupa stare
	vector<Task> sortare_stare();

	// adaugam un task cu campurile primite ca parametru
	void adauga_task(int id, string descriere, vector<string> lista, string stare);

	// metoda ce returneaza taskurile ce contin un anumit sir de caractere in numele programatorilor
	vector<Task> filtrare(string str);

	// metoda ce modifica starea unui obiect corespunzator unui id cu o stare primita ca parametru
	void modifica_stare(int id, string stare_noua);

	// metoda ce se ocupa cu filtrarea taskurilor dupa stare
	vector<Task> filtrare_stare(string stare);
};