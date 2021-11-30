#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>

void teste_domain() {

	Melodie m{ 1,"a","a",1 };

	assert(m.get_id() == 1);
	assert(m.get_titlu() == "a");
	assert(m.get_artist() == "a");
	assert(m.get_rank() == 1);

	m.set_rank(2);
	m.set_titlu("b");
	assert(m.get_rank() == 2);
	assert(m.get_titlu() == "b");
}

void teste_repo() {

	std::ofstream out("teste.txt");

	out << 3 << '\n';
	out << "a" << '\n';
	out << "a" << '\n';
	out << 3 << '\n';
	out << 1 << '\n';
	out << "b" << '\n';
	out << "b" << '\n';
	out << 1 << '\n';
	out << 2 << '\n';
	out << "c" << '\n';
	out << "c" << '\n';
	out << 2 << '\n';
	out << 4 << '\n';
	out << "f" << '\n';
	out << "f" << '\n';
	out << 4 << '\n';
	out << 5 << '\n';
	out << "g" << '\n';
	out << "f" << '\n';
	out << 5;
	out.close();

	Repository repo{ "teste.txt" };

	assert(repo.get_all().size() == 5);
	repo.sterge("f");
	assert(repo.get_all().size() == 4);

	try {
		repo.sterge("g");
		assert(false);
	}
	catch (std::exception) {
		assert(true);
	}

	vector<Melodie> l = repo.get_all();
	assert(l.size() == 4);
	assert(l.at(0).get_id() == 3);

	Repository repoErr{ "" };

	repo.modifica_titlu_rank(1, "d", 4);
	l = repo.get_all();
	assert(l.at(1).get_titlu() == "d");
	assert(l.at(1).get_rank() == 4);
	repo.modifica_titlu_rank(1, "b", 1);
}

void teste_service() {

	std::ofstream out("teste.txt");

	out << 3 << '\n';
	out << "a" << '\n';
	out << "a" << '\n';
	out << 3 << '\n';
	out << 1 << '\n';
	out << "b" << '\n';
	out << "b" << '\n';
	out << 1 << '\n';
	out << 2 << '\n';
	out << "c" << '\n';
	out << "c" << '\n';
	out << 2 << '\n';
	out << 4 << '\n';
	out << "f" << '\n';
	out << "f" << '\n';
	out << 4 << '\n';
	out << 5 << '\n';
	out << "g" << '\n';
	out << "f" << '\n';
	out << 5;
	out.close();

	Repository repo{ "teste.txt" };
	Service srv{repo};

	assert(srv.get_all().size() == 5);
	srv.sterge_melodie("f");
	assert(srv.get_all().size() == 4);

	try {
		srv.sterge_melodie("g");
		assert(false);
	}
	catch (std::exception) {

		assert(true);
	}

	vector<Melodie> l = srv.get_all();
	assert(l.size() == 4);
	l = srv.sortare_rank();
	assert(l.at(0).get_rank() == 1);

	srv.modifica_titlu_rank(1, "d", 4);
	l = srv.get_all();
	assert(l.at(1).get_titlu() == "d");
	assert(l.at(1).get_rank() == 4);
	srv.modifica_titlu_rank(1, "b", 1);
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}