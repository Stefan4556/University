#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>

void teste_domain() {

	Produs p{ 1,"a","a",1 };

	assert(p.get_id() == 1);
	assert(p.get_nume() == "a");
	assert(p.get_tip() == "a");
	assert(p.get_pret() == 1);

	Validator val;
	Produs p1{ 1,"","a",111 };
	try {
		val.valideaza(p1);
		assert(false);
	}
	catch (const string&) {
		assert(true);
	}
}

void teste_repo() {

	Repository repo{ "teste.txt" };
	Produs p{ 1,"a","a",1 };
	try {
		repo.adauga_produs(p);
		assert(false);
	}
	catch (const string&) {
		assert(true);
	}
	Produs p1{ 3,"c","c",3 };
	assert(repo.get_all().size() == 2);
	repo.adauga_produs(p1);
	assert(repo.get_all().size() == 3);

	Repository repoErr{ "" };
}

void teste_service() {

	Repository repo{ "teste.txt" };
	Validator val;
	Service srv(repo, val);

	assert(srv.get_all().size() == 2);
	vector<Produs> l = srv.sortare_pret();
	assert(l.at(0).get_pret() == 1);
	assert(l.at(1).get_pret() == 2);

	assert(srv.get_all().size() == 2);
	srv.adauga_produs(3, "d", "d", 3);
	assert(srv.get_all().size() == 3);
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}