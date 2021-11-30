#pragma once

// Rolul acestei modul este de a retine definitia obiectelor de tipul Melodie

#include <string>

using std::string;

// Rolul clasei melodie este de a retine metodele aferente acesteia si campurile obiectului

class Melodie {

private:

	int id;
	string titlu, artist, gen;

public:

	// Constructorul clasei atribuie fiecarui camp, cate un parametru primit
	Melodie(int i, string t, string a, string g) : id{ i }, titlu{ t }, artist{ a }, gen{ g }{};

	// Metoda get_id, retunreaza id-ul unei melodii
	int get_id() {

		return id;
	}

	// Rolul acestei metode este de a returna titlul unei melodii
	string get_titlu() {

		return titlu;
	}

	// Rolul acestei metode este de a returna artistul unei melodii
	string get_artist() {

		return artist;
	}

	// Rolul acestei metode este de a returna genul unei melodii
	string get_gen() {

		return gen;
	}
};