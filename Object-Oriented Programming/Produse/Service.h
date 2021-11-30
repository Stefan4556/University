#pragma once

// Rolul acestui modul este de a retine clasa Service ce realizeaza legatura dintre GUI si restul codului

#include "Repository.h"
#include "Observer.h"

// Clasa Service are 2 campuri si anume, referinta catre repo si catre validator
class Service : public Observable{

private:

	Repository& repo;
	Validator& val;

public:

	// Constructorul clasei se ocupa cu initializarea legaturilor catre service si validator, asa ca primeste referinta catre acestea ca si parametrii
	Service(Repository& repo, Validator& val) : repo{ repo }, val{ val }{};

	// Rolul acestei functii este de a returna lista de produse
	vector<Produs> get_all();

	// Aceasta metoda sorteaza crescator lista de produse dupa pret
	vector<Produs> sortare_pret();

	// Aceasta metoda cum ii spune si numele creeaza un obiect, incearca sa-l valideze dupa care incearca sa-l adauge, poate arunca erori in cazul in care este produsul este invalid sau exista unul cu id-ul lui
	void adauga_produs(int id, string nume, string tip, double pret);
};