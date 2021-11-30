#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include <assert.h>

void teste_domain() {

	Carte c("a", "a", "a", 1);

	assert(c.get_autor() == "a");
	assert(c.get_culoare() == "a");
	assert(c.get_grosime() == 1);
	assert(c.get_titlu() == "a");
}

void teste_repo() {

	Repository_carti repo("teste.txt");

	vector<Carte> l = repo.get_all();

	assert(l.size() == 3);

	Carte c = repo.get_item_by_title("a");

	assert(c.get_autor() == "a");

	Repository_carti repo_err("");
}

void teste_service() {

	Repository_carti repo("teste.txt");

	Service_carti srv(repo);

	vector<Carte> l = srv.get_all();

	assert(l.size() == 3);

	Carte c = srv.get_item_by_title("a");

	assert(c.get_autor() == "a");

	vector<Carte> rez_s1 = srv.sortare_dupa_grosime();

	assert(rez_s1[0].get_grosime() == 1);
	assert(rez_s1[1].get_grosime() == 2);
	assert(rez_s1[2].get_grosime() == 3);

	vector<Carte> rez_s2 = srv.sortare_dupa_titlu();

	assert(rez_s2[0].get_titlu() == "a");
	assert(rez_s2[1].get_titlu() == "b");
	assert(rez_s2[2].get_titlu() == "c");
}

void ruleaza_teste() {

	teste_domain();
	teste_repo();
	teste_service();
}