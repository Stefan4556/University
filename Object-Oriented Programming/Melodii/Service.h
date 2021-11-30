#pragma once

// Rolul acestui modul este de a realiza legatura dintre GUI si celelaltle module

#include "Repository.h"

// Clasa Service are un singur camp si anume referinta catre repo si metodele aferente acesteia
class Service {

private:

	Repository& repo;

public:

	// Constructorul acestei clase primeste referinta la repo pentru a se putea realiza legatura
	Service(Repository& repo0) : repo{ repo0 } {};

	// Aceasta metoda returneaza lista de melodii din repo
	vector<Melodie> get_all();

	// Aceasta metoda se ocupa cu sortarea listei de melodii din repo in oridne crescatoare dupa rank
	vector<Melodie> sortare_rank();

	// Rolul acestei metode este de a actualiza o melodie corespunzatoare unui id cu un titlu si un rank nou
	void modifica_titlu_rank(int id, string titlu_nou, int rank_nou);

	// Aceasta metoda incearca sa stearga o melodie corespunzatopare unui titlu, altfel arunca exceptie
	void sterge_melodie(string titlu);
};