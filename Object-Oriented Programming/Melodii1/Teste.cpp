#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>

void teste_domain() {

	Melodie m{ 1,"a","a","pop" };

	assert(m.get_id() == 1);
	assert(m.get_titlu() == "a");
	assert(m.get_gen() == "pop");
	assert(m.get_artist() == "a");
}

void teste_repo() {

	Repository repoerr{ "" };

	Repository repo{ "teste.txt" };

	assert(repo.get_all().size() == 2);

	Melodie m{ 3,"c","c","rock" };

	repo.adauga_melodie(m);

	assert(repo.get_all().size() == 3);

	repo.sterge_melodie(3);

	assert(repo.get_all().size() == 2);
}

void teste_service() {

	Repository repo{ "teste.txt" };
	Service srv(repo);

	assert(srv.get_all().size() == 2);

	assert(srv.sortare_autor().at(0).get_artist() == "a");

	srv.adauga_melodie(3, "c", "c", "rock");

	assert(srv.get_all().size() == 3);

	srv.sterge_melodie(3);

	assert(srv.get_all().size() == 2);
}

void ruleaza_teste() {
	
	teste_domain();
	teste_repo();
	teste_service();
}