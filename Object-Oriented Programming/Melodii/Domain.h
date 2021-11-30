#pragma once

// Rolul acestui modul este de a retine clasa ce ii corespunde obiectului de tipul Melodie

#include <string>

using std::string;

// Clasa Melodie retine vampurile si metodele aferente obiectelor de tipul Melodie
class Melodie {

private:

	int id;
	string titlu;
	string artist;
	int rank;

public:

	// Acesta este constructorul unui obiect de tipul melodie ce primeste ca si parametru 2 intregi si 2 stringuri reprezentand campurile unei melodii
	Melodie(int id0, string titlu0, string artist0, int rank0) : id{ id0 }, titlu{ titlu0 }, artist{ artist0 }, rank{ rank0 }{};

	// Rolul acestei metode este de a returna id-ul corespunzator unui obiect de tipul Melodie
	int get_id() {

		return this->id;
	}

	// Rolul acestei metode este de a returna titlul corespunzator unui obiect de tipul Melodie
	string get_titlu() {

		return this->titlu;
	}

	// Rolul acestei metode este de a returna artistul corespunzator unui obiect de tipul Melodie
	string get_artist() {

		return this->artist;
	}

	// Rolul acestei metode este de a returna rankul corespunzator unui obiect de tipul Melodie
	int get_rank() {

		return this->rank;
	}

	// Rolul acestei metode este de a actualiza campul titlu al unei melodii cu alt titlu primit ca si parametru
	void set_titlu(string titlu_nou) {

		this->titlu = titlu_nou;
	}

	// Rolul acestei metode este de a actualiza campul rank al unei melodii cu alt rank primit ca si parametru
	void set_rank(int rank) {

		this->rank = rank;
	}
};