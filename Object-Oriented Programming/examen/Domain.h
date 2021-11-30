#pragma once

// Modulul Domain.h retine 2 clase, Cartea ce este obiectul de baza in aplicatia noastra si Validatorul ce se ocupa cu validarea obiectelor de tipul
// Carte

#include <string>

using std::string;

// Clasa Carte are 4 campuri private reprezentand cele 4 campuri ale unui obiect de acest tip si metodele aferente acestora
class Carte {

private:

	int id;
	double pret;
	string titlu, tip;

public:

	// Constructorul clasei Carte primeste ca si parametrii, campurile unui obiect carte ce urumeaza a fi creat si ii atribuie fiecarui camp cate un
	// parametru
	Carte(int id, string titlu, string tip, double pret) : id{ id }, titlu{ titlu }, tip{ tip }, pret{ pret }{};

	// Metoda get_id returneaza id-ul unei Carti
	int get_id();

	// Functia get_titlu se ocupa cu returnarea titlului unei carti
	string get_titlu();

	// Metoda get_tip returneaza tipul unei Carti
	string get_tip();

	// Functia get_pret se ocupa cu returnarea pretului unei Carti
	double get_pret();

};

// Clasa Validator, dupa cum ii spune si numele se ocupa cu validarea obiectelor de tipul Carte si are o singura metoda ce poate arunca exceptii
class Validator {

public:

	// Aceasta este metoda ce se ocupa cu validarea campurilor unei carti si in cazul in care detecteaza vreo problema la unul sau mai multe campuri
	// o eroare o sa fie ridicata
	void valideaza(Carte c);
};