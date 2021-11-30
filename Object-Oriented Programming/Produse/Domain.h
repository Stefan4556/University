#pragma once

// Rolul acestui modul este de a retine clasa ce reprezinta un produs

#include <string>

using std::string;

// Clasa produs are 4 campuri private ce consta in: id, nume, tip si pret + metodele aferente acestora pentru a ne putea asigura ca informatiile unui produs pot fi aflate
class Produs {

private:

	int id;
	string nume, tip;
	double pret;

public:

	// Constructorul clasei primeste 4 parametrii, acestia reprezentand campurile unui produs
	Produs(int id, string nume, string tip, double pret) : id{ id }, nume{ nume }, tip{ tip }, pret{ pret }{};

	// Metoda returneaza id-ul unui produs
	int get_id() {

		return id;
	}

	// Metoda returneaza numele unui produs
	string get_nume() {

		return nume;
	}

	// Metoda returneaza tipul unui produs
	string get_tip() {

		return tip;
	}

	// Metoda returneaza pretul unui produs
	double get_pret() {

		return pret;
	}
};

// Clasa Validator se ocupa cu validarea campurilor unui produs
class Validator {

public:

	// Aceasta metoda valideaza un produs trimis ca si parametru si in caz de ceva arunca exceptie
	void valideaza(Produs p);
};