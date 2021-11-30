#pragma once

// Modulul Service.h retine o singura clasa, aceasta realizand legatura dintre GUI si Repo

#include "Repository.h"
#include "Observer.h"

// Clasa Service se ocupa cu realizarea conexiunii dintre stratul inferior si stratul superior al aplicatiei
class Service : public Observable{

private:

	Validator& val;
	Repository& repo;

public:

	// Constructorul clasei primeste ca si parametrii, referinta la repo pentru a realiza legatura dintre repo si GUI si referinta catre Validator
	// pentru a se asigura ca obiectele ce i le trimite repo-ului sunt valide
	Service(Repository& repo, Validator& val) : repo{ repo }, val{ val }{};

	// Metoda get_all are rolul de a returna lista de carti primita din repo
	vector<Carte> get_all();

	// Functia adauga_carte incearca adaugarea unei carti daca datele acesteia sunt corecte si daca nu mai exista o carte cu acelasi id sau acelasi
	// titlu, caz in care ar arunca o exceptie
	void adauga_carte(int id, string titlu, string tip, double pret);

	// Dupa cum ii spune si numele, functia se ocupa cu returnarea listei de carti sortate dupa numarul de litere din tip
	vector<Carte> sortare_litere();

	// Aceasta metoda se ocupa cu returnarea listei de carti ce au un anumit tip primit ca si parametru
	vector<Carte> get_lista_tip(string tip);
};