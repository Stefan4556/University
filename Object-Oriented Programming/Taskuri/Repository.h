#pragma once
#include "Domain.h"

// clasa Repository se ocupa cu gestiunea listei de taskuri
class Repository {

private:

	string nume_fisier;
	vector<Task> lista;

public:

	// Constructorul primeste numele de fisier de unde citeste datele si apeleaza metoda ce incarca taskurile in lista
	Repository(string nume) : nume_fisier{ nume } {

		load_from_file();
	}

	// metoda ce incarca taskurile din fisier in lista
	void load_from_file();

	// metoda ce returneaza lista de taskuri
	vector<Task> get_all();

	// metoda ce adauga un task primit ca si parametru in lista
	void adauga_task(Task t);

	// metoda ce modifica starea unui task cu id ul primit ca parametru
	void modifica_stare(int id, string stare_noua);

	// metoda ce se ocupa cu scrierea in fisier a listei
	void write_to_file();
};