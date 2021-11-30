#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>
#include <fstream>

void teste_domain() {

	vector<string> l{ "a","b" };

	Task t{ 1,"a",l,"open" };

	assert(t.get_id() == 1);
	assert(t.get_descriere() == "a");
	assert(t.get_lista() == l);
	assert(t.get_stare() == "open");

	vector<string> l1;

	Task t1{ 1,"",l1,"salut" };
	Validator val;

	try {
		val.valideaza(t1);
		assert(false);
	}
	catch (const string&) {
		assert(true);
	}

	t1.set_stare("open");
	assert(t1.get_stare() == "open");
}

void teste_repo() {

	std::ofstream out("teste.txt");
	out << 1 << '\n';
	out << "a" << '\n';
	out << "Bob" << '\n';
	out << "Man" << '\n';
	out << "open" << '\n';
	out << 2 << '\n';
	out << "b" << '\n';
	out << "Michael" << '\n';
	out << "closed";
	out.close();

	Repository repo{ "teste.txt" };

	assert(repo.get_all().size() == 2);

	try {
		vector<string> l{ "Bob" };
		Task t{ 1,"a",l,"open" };
		repo.adauga_task(t);
		assert(false);
	}
	catch (const string&) {

		assert(true);
	}

	vector<string> l{ "Bob" };
	Task t{ 3,"a",l,"open" };
	repo.adauga_task(t);
	assert(repo.get_all().size() == 3);

	repo.modifica_stare(3, "closed");
	assert(repo.get_all().at(2).get_stare() == "closed");

	Repository repoerr{ "" };
}

void teste_service() {

	std::ofstream out("teste.txt");
	out << 1 << '\n';
	out << "a" << '\n';
	out << "Bob" << '\n';
	out << "Man" << '\n';
	out << "open" << '\n';
	out << 2 << '\n';
	out << "b" << '\n';
	out << "Michael" << '\n';
	out << "closed";
	out.close();

	Repository repo{ "teste.txt" };
	Validator val;
	Service srv(repo, val);

	assert(srv.get_all().size() == 2);
	assert(srv.sortare_stare().at(0).get_stare() == "closed");
	vector<string> l{ "Bob" };
	srv.adauga_task(3, "a", l, "open");
	assert(srv.get_all().size() == 3);

	vector<Task> rez = srv.filtrare("a");
	assert(rez.size() == 1);

	srv.modifica_stare(3, "closed");
	assert(srv.get_all().at(2).get_stare() == "closed");

	vector<Task> rez1 = srv.filtrare_stare("open");
	assert(rez1.size() == 1);
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}