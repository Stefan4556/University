#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>
#include <fstream>

void teste_domain() {

	Carte c{ 1,"a","a",2 };
	assert(c.get_id() == 1);
	assert(c.get_titlu() == "a");
	assert(c.get_tip() == "a");
	assert(c.get_pret() == 2);

	Validator val;
	Carte c1{ 1,"","a",101 };
	try {
		val.valideaza(c1);
		assert(false);
	}
	catch (const string&) {
		assert(true);
	}
}

void teste_repo() {

	std::ofstream out("teste.txt");

	out << 2 << '\n';
	out << "a" << '\n';
	out << "bb" << '\n';
	out << 2 << '\n';
	out << 1 << '\n';
	out << "b" << '\n';
	out << "c" << '\n';
	out << "3";

	out.close();

	Repository repo{ "teste.txt" };

	assert(repo.get_all().size() == 2);

	Carte c{ 1, "ccc","ccc",3 };
	try {
		repo.adauga_carte(c);
		assert(false);
	}
	catch (const string&) {

		assert(true);
	}
	Carte c1{ 4, "a","aaa",4 };
	try {
		repo.adauga_carte(c1);
		assert(false);
	}
	catch (const string&) {

		assert(true);
	}
	Carte c2{ 3,"aaa","aaa",3 };
	repo.adauga_carte(c2);
	assert(repo.get_all().size() == 3);

	Repository repoerr{ "" };
}

void teste_service() {

	std::ofstream out("teste.txt");

	out << 2 << '\n';
	out << "a" << '\n';
	out << "bb" << '\n';
	out << 2 << '\n';
	out << 1 << '\n';
	out << "b" << '\n';
	out << "c" << '\n';
	out << "3" << '\n';

	out.close();

	Repository repo{ "teste.txt" };
	Validator val;
	Service srv(repo, val);

	vector<Carte> filtru = srv.get_lista_tip("c");
	assert(filtru.size() == 1);

	vector<Carte> rez = srv.sortare_litere();
	assert(rez.at(0).get_tip() == "c");
	assert(rez.at(1).get_tip() == "bb");

	assert(srv.get_all().size() == 2);
	srv.adauga_carte(3, "aaa", "aaa", 3);
	assert(srv.get_all().size() == 3);
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}