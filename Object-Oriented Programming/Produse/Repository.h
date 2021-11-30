#pragma once

// Acesta este modulul ce se ocupa cu retinerea clasei ce are ca scop gestionarea listei de produse

#include "Domain.h"
#include <vector>

using std::vector;

// clasa Repository are 2 campuri si anume, numele fisierului si lista de produse, plus metodele aferente
class Repository {

private:

	string nume_fisier;
	vector<Produs> lista;

public:

	// Constructorul clasei Repository, primeste ca si parametru fisierul de unde urmeaza sa incarce datele si apeleaza o metoda ce face incarcarea
	Repository(string nume_fis) : nume_fisier{ nume_fis } {

		load_from_file();
	}

	// Aceasta metoda, dupa cum ii spune si numele, are scopul de a incarca produsele ce sunt stocate in fisierul primit ca si parametru in constructor
	void load_from_file();

	// Aceasta metoda are rolul de a incerca sa adauge un produs, pentru ca in cazul in care mai exista unul cu id-ul respectiv, este aruncata o exceptie
	void adauga_produs(Produs p);

	// Rolul acestei metode este de a returna lista de produse
	vector<Produs> get_all();
};