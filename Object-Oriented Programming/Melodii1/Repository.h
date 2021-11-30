#pragma once

// In acest modul este retinuta lista de melodii si operatiile crud de la nivelul acesteia

#include "Domain.h"
#include <vector>

using std::vector;

// Clasa Repository are 2 campuri private : lista de melodii si numele fisierului din care incarca datele si in care scrie utlerior in cazul in care lista sufera modificari
class Repository {

private:

	string nume_fisier;
	vector<Melodie> lista;

public:

	// Constructorul clasei noastre primeste doar un nume de fisier, si ulterior apeleaza functia ce se ocupa cu citirea din fisier a datelor si punerea acestora in lista
	Repository(string fis) : nume_fisier{ fis } {

		load_from_file();
	};

	// Rolul functiei, dupa cum ii spune si numele este de a incarca datele din fisier si a le pune in lista
	void load_from_file();

	// Rolul functiei, dupa cum ii spune si numele este de a scrie in fisier lista de elemente, aceasta functie fiind apelata doar daca s-au efectuat modificari asupra listei
	void write_to_file();

	// Metoda returneaza llsita de melodii
	vector<Melodie> get_all();

	// Rolul acestei functii este de a adauga o melodie trimisa ca si parametru in lista de melodii
	void adauga_melodie(Melodie m);

	// Functia se ocupa cu stergerea melodiei corespunzatoare id-ului trimis ca si parametru
	void sterge_melodie(int id);
};