#pragma once

// Aceasta clasa se ocupa cu realizarea legaturii dintre GUI si repo

#include "Repository.h"

// Clasa Service are un singur camp privat, si anume legatura catre repo si alte metode
class Service {

private:

	Repository& repo;

public:

	// Constructorul primeste ca si parametru referinta la repo, element ce ne ajuta sa realizam legatura
	Service(Repository& rep) : repo{ rep } {};

	// Aceasta functie retunreaza lista de melodii din repo
	vector<Melodie> get_all();

	// Rolul acestei metode este de a returna lista curent de melodii sortata crescator dupa autor
	vector<Melodie> sortare_autor();

	// Dupa cum ii spune si numele, aceasta metoda creeaza si trimite mai departe o melodie cu scopul de a fi adaugata in lista
	void adauga_melodie(int id, string titlu, string artist, string gen);

	// Dupa cum ii spune si nuemel, rolul acesteia este de a sterge melodia corespunzatoare id-ului primit ca si parametru
	void sterge_melodie(int id);
};