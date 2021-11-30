#pragma once

#include <string>
#include <vector>

using std::string;
using std::vector;

// clasa ce se ocupa cu instantierea unui obiect de tipul task
class Task {

private:

	int id;
	string descriere;
	vector<string> lista_programatori;
	string stare;

public:

	// Constructorul clasei ce primeste cele 4 campuri ale  unui obiect si le initializeaza
	Task(int id, string descriere, vector<string> lista, string stare) : id{ id }, descriere{ descriere }, lista_programatori{ lista }, stare{ stare }{};

	// Metoda ce reutrneaza id ul unui task
	int get_id() {

		return id;
	}

	// Metoda ce reutrneaza descrierea unui task
	string get_descriere() {

		return descriere;
	}

	// Metoda ce reutrneaza lista unui task
	vector<string> get_lista() {

		return lista_programatori;
	}

	// Metoda ce reutrneaza starea unui task
	string get_stare() {

		return stare;
	}

	// Metoda ce seteaza starea unui task
	void set_stare(string stare_noua) {

		stare = stare_noua;
	}
};

// clasa Validator contine o metoda ce se ocupa cu validarea taskurilor
class Validator {

public:

	// are rolul de a valida task ul primit ca parametru
	void valideaza(Task t);
};