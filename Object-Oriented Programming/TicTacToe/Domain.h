#pragma once

#include <string>

using std::string;

class Joc {

private:

	int id, dim;
	string tabla, jucator, stare;

public:

	Joc(int id, int dim, string tabla, string jucator, string stare) : id{ id }, dim{ dim }, tabla{ tabla }, jucator{ jucator }, stare{ stare }{
	};

	int get_id() {

		return id;
	}

	int get_dim() {

		return dim;
	}

	string get_tabla() {

		return tabla;
	}

	string get_jucator() {

		return jucator;
	}

	string get_stare() {

		return stare;
	}

	void set_dim(int dim_noua);

	void set_tabla(string tabla_noua);

	void set_jucator(string jucator_nou);

	void set_stare(string stare_noua);
};

class Validator {

public:

	void valideaza(Joc j);
};