#pragma once

// Rolul acestui modul este de a retine clasa Repository ce se ocupa cu retinerea listei de melodii

#include "Domain.h"
#include <vector>
#include <fstream>

using std::vector;

// Clasa Repository se ocupa cu retinerea listei de carti, numele fisierului de unde sunt citite datele si cu metodele aferente acestora
class Repository {

private:

	vector<Melodie> lista;
	string nume_fisier;

public:

	// Constructorul nostru primeste ca si parametru un nume de fisier dupa care apeleaza o metoda ce incarca melodiile dintr-un fisier
	Repository(string nume_fis) : nume_fisier{ nume_fis } {

		load_from_file();
	};

	// Rolul acestei metode este de a baga in lista obiectele ce sunt citite din fisierul trimis ca si parametru la repository
	void load_from_file();

	// Rolul acestei metode este de a returna ;ista de melodii
	vector<Melodie> get_all();
	
	// Rolul acestei metode este de a actualiza fisierul cu date de intrare in cazul in care lista de melodii sufera modificari
	void write_to_file();

	// Rolul acestei metode este de a actualiza doua camprui ale unui obiect ce ii corespunde unui id primit ca si parametru
	void modifica_titlu_rank(int id, string titlu_nou, int rank_nou);

	// Rolul acestei metode este de a sterge un obiect cu un anumit titlu in cazul in care melodia corespunzatoarea nu este ultima a autorului
	void sterge(string titlu);
};