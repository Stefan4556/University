#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <cassert>
#include <fstream>

void teste_domain() {

	Joc j{ 1, 3, "XOXOXOXOX", "X", "Terminat" };
	assert(j.get_id() == 1);
	assert(j.get_dim() == 3);
	assert(j.get_tabla() == "XOXOXOXOX");
	assert(j.get_jucator() == "X");
	assert(j.get_stare() == "Terminat");

	j.set_dim(2);
	j.set_jucator("p");
	j.set_tabla("12312");
	j.set_stare("da");

	Validator val;
	try{
		
		val.valideaza(j);
		assert(false);
	}
	catch (const string&) {

		assert(true);
	}

	Joc j2{ 1,3,"aaaaaaaaa","X","Over" };
	try {
		val.valideaza(j2);
		assert(false);
	}
	catch (const string&) {

		assert(true);
	}
}

void teste_repo(){

	std::ofstream out{ "teste.txt" };

	out << "1 3 XX-XO-XOO X Terminat\n";
	out << "2 3 X-OXO-XOO X Inderulare\n";
	out << "3 3 XXXXO-XOO X Neinceput\n";
	out << "4 3 X-OOO-XXO X Terminat\n";
	out.close();

	Repository repo{ "teste.txt" };

	assert(repo.get_all().size() == 4);

	Joc j{ 5, 3, "XOXOXOXOX", "X", "Terminat" };
	repo.adauga_joc(j);	
	assert(repo.get_all().size() == 5);

	repo.modifica_joc(5, 2, "a", "a", "a");
	assert(repo.get_all().at(4).get_dim() == 2);
	assert(repo.get_all().at(4).get_tabla() == "a");

	Joc j2 = repo.get_item_by_id(1);
	assert(j2.get_id() == 1);

	Repository repoerr{ "" };
}

void teste_service() {

	std::ofstream out{ "teste.txt" };

	out << "1 3 XX-XO-XOO X Terminat\n";
	out << "2 3 X-OXO-XOO X Inderulare\n";
	out << "3 3 XXXXO-XOO X Neinceput\n";
	out << "4 3 X-OOO-XXO X Terminat\n";
	out.close();

	Repository repo{ "teste.txt" };
	Validator val;
	Service srv(repo, val);

	assert(srv.get_all().size() == 4);

	srv.adauga_joc(3, "XOXOXOXOX", "X");
	assert(srv.get_all().size() == 5);
	srv.modifica_joc(5, 3, "XOXOXOXOX", "X", "Terminat");
	assert(srv.get_all().at(4).get_tabla() == "XOXOXOXOX");

	Joc j2 = srv.get_item_by_id(1);
	assert(j2.get_id() == 1);
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}