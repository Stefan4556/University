#pragma once

// Modulul repository.h are rolul de a retine o clasa ce se ocupa cu gestionarea listei de carti

#include "Domain.h"
#include <vector>

using std::vector;

// clasa Repository are 2 campuri private, acestea constand in numele fisierului de unde isi procura datele si lista de carti
class Repository {

private:

	string nume_fisier;
	vector<Carte> lista;

public:

	// constructorul clasei repository, primeste ca si parametru numele fisierului din care realizeaza citirea si apeleaza o metoda ce se ocupa cu
	// incarcarea datelor din el
	Repository(string nume_fis) : nume_fisier{ nume_fis } {

		load_from_file();
	}

	// Dupa cum ii spune si numele, metoda load_from_file incarca din fisier obiectele de tip Carte si le adauga in lista de carti+
	void load_from_file();

	// Metoda write_to_file este apelata doar cand lista de carti sufera o modificare, aceasta ocupandu-se cu actualizarea fisierului
	void write_to_file();

	// Functia get_all returneaza lista de carti
	vector<Carte> get_all();

	// Aceasta metoda incearca adaugarea unei carti primita ca si parametru, dar in cazul in care mai exista o carte cu acelasi id si / sau cu acelasi titlu
	// este aruncata o exceptie
	void adauga_carte(Carte c);
};