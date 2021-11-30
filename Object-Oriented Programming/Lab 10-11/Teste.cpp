#include <iostream>
#include "Teste.h"
#include <assert.h>
#include <string>
#include <vector>
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include "VectorDinamic.h"
#include "Cos.h"
#include "Repo_lab.h"

void teste_domain() {

	Film f(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel");

	assert(f.get_id() == 1);
	assert(f.get_titlu() == "Fast and Furious");
	assert(f.get_gen() == "Actiune");
	assert(f.get_an_aparitie() == 2018);
	assert(f.get_actor_principal() == "Vin Diesel");

	f.set_id(7);
	assert(f.get_id() == 7);

	f.set_titlu("Furios si iute");
	assert(f.get_titlu() == "Furios si iute");

	f.set_gen("Comedie");
	assert(f.get_gen() == "Comedie");

	f.set_an_aparitie(2019);
	assert(f.get_an_aparitie() == 2019);

	f.set_actor_principal("Paul Walker");
	assert(f.get_actor_principal() == "Paul Walker");

	Film f1(-10, "", "", -1, "");
	Validator val;

	try {

		val.valideaza(f1);
		assert(false);
	}
	catch (ValidationError) {
		assert(true);
	}
	f1.set_id(1);

	try {

		val.valideaza(f1);
		assert(false);
	}
	catch (ValidationError) {
		assert(true);
	}

	f1.set_titlu("Inception");
	try {

		val.valideaza(f1);
		assert(false);
	}
	catch (ValidationError) {
		assert(true);
	}

	f1.set_gen("Psihologic");
	try {

		val.valideaza(f1);
		assert(false);
	}
	catch (ValidationError) {
		assert(true);
	}

	f1.set_an_aparitie(2015);
	try {

		val.valideaza(f1);
		assert(false);
	}
	catch (ValidationError) {
		assert(true);
	}

	f1.set_actor_principal("Leonardo Di Caprio");
	try {

		val.valideaza(f1);
		assert(true);
	}
	catch (ValidationError) {
		assert(false);
	}

	Film f2(-1, "a", "a", 1, "a");
	try {

		val.valideaza(f2);
		assert(false);
	}
	catch (const ValidationError& err) {

		assert(err.getMessage() == "Id-ul nu poate sa fie un numar mai mic sau egal decat 0!\n");
	}
}

void teste_repo() {

	Repository_filme_file repo("teste.txt");
	try {

		Film ff = repo.get_item_by_id(22);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// teste pentru adauga
	repo.adauga_film(Film(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel"));
	repo.adauga_film(Film(2, "The Wolf of the Wall Street", "Business", 2015, "Leonardo Di Caprio"));
	repo.adauga_film(Film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh"));
	assert(repo.dimensiune() == 3);

	// teste pentru get item by title
	assert(repo.get_item_by_title("Fast and Furious").get_id() == 1);
	try {

		repo.get_item_by_title("asdasdas");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// teste pentru get all
	std::vector<Film> l = repo.get_all();
	assert(l.size() == 3);
	try {
		repo.adauga_film(Film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh"));
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	assert(repo.dimensiune() == 3);

	// teste pentru cauta
	assert(repo.cauta_film(1) == true);
	assert(repo.cauta_film(7) == false);

	// teste pentru sterge
	try {

		repo.sterge_film(7);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}
	repo.sterge_film(3);
	assert(repo.dimensiune() == 2);

	// test pentru modifica titlu
	repo.modifica_titlu_film(2, "Modificat");
	l = repo.get_all();
	Film f = l.at(1);
	assert(f.get_titlu() == "Modificat");
	try {
		repo.modifica_titlu_film(22, "bbb");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica gen
	repo.modifica_gen_film(2, "Modificat");
	l = repo.get_all();
	assert(l.at(1).get_gen() == "Modificat");
	try {

		repo.modifica_gen_film(22, "Modificat");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica an
	repo.modifica_anul_film(2, 111);
	l = repo.get_all();
	assert(l.at(1).get_an_aparitie() == 111);
	try {
		repo.modifica_anul_film(22, 111);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica actor principal
	repo.modifica_actor_film(2, "Modificat");
	l = repo.get_all();
	assert(l.at(1).get_actor_principal() == "Modificat");
	try {
		repo.modifica_actor_film(22, "Modificat");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru get item by id
	Film flm = repo.get_item_by_id(2);
	assert(flm.get_id() == 2);
	assert(flm.get_actor_principal() == "Modificat");

	repo.sterge_film(1);
	repo.sterge_film(2);

	Repository_filme_file repo1("teste.txt");
	repo1 = repo1;
	repo1.adauga_film(Film(1, "a", "a", 1, "a"));
	repo1.adauga_film(Film(2, "b", "b", 2, "b"));
	repo1.adauga_film(Film(3, "c", "c", 3, "c"));
	assert(repo1.dimensiune() == 3);
	repo1.sterge_film(2);
	assert(repo1.dimensiune() == 2);
	repo1.sterge_film(1);
	repo1.sterge_film(3);

	try {

		Repository_filme_file repo2("");
		repo2.write_to_file();
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	Repository_filme_file repo2("teste.txt");
	repo2.nume_fisier = "";
	try {

		repo2.write_to_file();
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

}

void teste_service() {

	std::ofstream g("teste.txt");

	g << "1 a a 1 a\n2 b b 2 b\n";

	g.close();

	Repository_filme_file repo("teste.txt");
	Validator valid;
	Cos cos(repo);
	Service_filme srv(repo, valid, cos);

	// test pentru read from file
	std::vector<Film> listaaa = repo.get_all();
	assert(listaaa.size() == 2);

	srv.sterge_film(1);
	srv.sterge_film(2);

	// test pentru adauga
	srv.adauga_film(1, "a", "a", 1, "a");
	srv.adauga_film(2, "b", "b", 2, "b");
	srv.adauga_film(3, "c", "c", 3, "c");
	try {

		srv.adauga_film(3, "c", "c", 3, "c");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	try {

		srv.adauga_film(1, "", "", -1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.adauga_film(1, "a", "", -1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.adauga_film(1, "a", "a", -1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.adauga_film(1, "a", "a", 1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	// test pentru getall


	std::vector<Film> lista;
	lista = srv.get_all();
	assert(lista.size() == 3);

	// test pentru cauta film
	assert(srv.cauta_film(1) == 1);
	try {

		srv.cauta_film(7);
		assert(false);
	}
	catch (SrvError) {

		assert(true);
	}

	try {

		srv.cauta_film(-1);
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	// test pentru sterge film
	srv.adauga_film(4, "d", "d", 4, "d");
	try {

		srv.sterge_film(-4);
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}
	lista = srv.get_all();
	assert(lista.size() == 4);
	srv.sterge_film(4);
	lista = srv.get_all();
	assert(lista.size() == 3);
	try {

		srv.sterge_film(4);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}
	lista = srv.get_all();
	assert(lista.size() == 3);

	// test pentru modifica titlu film
	try {

		srv.modifica_titlu_film(-1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.modifica_titlu_film(1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	srv.modifica_titlu_film(1, "A");

	try {

		srv.modifica_titlu_film(7, "A");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	lista = srv.get_all();
	assert(lista.at(0).get_titlu() == "A");

	// test pentru modifica gen film
	try {

		srv.modifica_gen_film(-1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.modifica_gen_film(1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	srv.modifica_gen_film(1, "A");

	try {

		srv.modifica_gen_film(7, "A");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	lista = srv.get_all();
	assert(lista.at(0).get_gen() == "A");

	// test pentru modifica anul film
	try {

		srv.modifica_anul_film(-1, -1);
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.modifica_anul_film(1, -1);
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	srv.modifica_anul_film(1, 2);

	try {

		srv.modifica_anul_film(7, 2);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	lista = srv.get_all();
	assert(lista.at(0).get_an_aparitie() == 2);

	// test pentru modifica actor film
	try {

		srv.modifica_actor_film(-1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	try {

		srv.modifica_actor_film(1, "");
		assert(false);
	}
	catch (ValidationError) {

		assert(true);
	}

	srv.modifica_actor_film(1, "A");

	try {

		srv.modifica_actor_film(7, "A");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	lista = srv.get_all();
	assert(lista.at(0).get_actor_principal() == "A");

	// teste pentru get item by index
	Film ff = srv.get_item_by_id(2);
	assert(ff.get_id() == 2);
	assert(ff.get_titlu() == "b");

	srv.sterge_film(1);
	srv.sterge_film(2);
	srv.sterge_film(3);

}

void teste_filtrari() {

	Repository_filme_file repo("teste.txt");
	Validator valid;
	Cos cos(repo);
	Service_filme srv(repo, valid, cos);

	srv.adauga_film(1, "ab", "a", 1, "a");
	srv.adauga_film(2, "ba", "b", 2, "b");
	srv.adauga_film(3, "c", "c", 3, "c");

	std::vector<Film> lista_rezultat = srv.filtrare_titlu("a");
	assert(lista_rezultat.size() == 2);

	lista_rezultat = srv.filtrare_an(1);
	assert(lista_rezultat.size() == 1);

	srv.sterge_film(1);
	srv.sterge_film(2);
	srv.sterge_film(3);
}

void teste_sortari() {

	Repository_filme_file repo("teste.txt");
	Validator valid;
	Cos cos(repo);
	Service_filme srv(repo, valid, cos);

	Film f1(1, "a", "a", 1, "a");
	Film f2(2, "b", "b", 2, "b");
	Film f3(3, "c", "c", 2, "c");

	// teste pentru comparatori
	assert(srv.comparator("titlu", "crescator", f1, f2) == true);
	assert(srv.comparator("titlu", "crescator", f2, f1) == false);
	assert(srv.comparator("titlu", "descrescator", f1, f2) == false);
	assert(srv.comparator("titlu", "descrescator", f2, f1) == true);

	assert(srv.comparator("actor", "crescator", f1, f2) == true);
	assert(srv.comparator("actor", "crescator", f2, f1) == false);
	assert(srv.comparator("actor", "descrescator", f1, f2) == false);
	assert(srv.comparator("actor", "descrescator", f2, f1) == true);

	assert(srv.comparator("an si gen", "crescator", f1, f2) == true);
	assert(srv.comparator("an si gen", "crescator", f2, f1) == false);
	assert(srv.comparator("an si gen", "descrescator", f1, f2) == false);
	assert(srv.comparator("an si gen", "descrescator", f2, f1) == true);
	assert(srv.comparator("an si gen", "crescator", f2, f3) == true);
	assert(srv.comparator("an si gen", "crescator", f3, f2) == false);
	assert(srv.comparator("an si gen", "descrescator", f2, f3) == false);
	assert(srv.comparator("an si gen", "descrescator", f3, f2) == true);

	// teste pentru functia de sortare
	srv.adauga_film(1, "a", "a", 1, "a");
	srv.adauga_film(2, "b", "b", 2, "b");
	srv.adauga_film(3, "c", "c", 3, "c");

	std::vector<Film> lista_sortata = srv.sortare_filme("titlu", "crescator");
	assert(lista_sortata.at(0).get_titlu() == "a");
	lista_sortata = srv.sortare_filme("titlu", "descrescator");
	assert(lista_sortata.at(0).get_titlu() == "c");

	lista_sortata = srv.sortare_filme("actor", "crescator");
	assert(lista_sortata.at(0).get_actor_principal() == "a");
	lista_sortata = srv.sortare_filme("actor", "descrescator");
	assert(lista_sortata.at(0).get_actor_principal() == "c");

	srv.adauga_film(4, "d", "d", 1, "d");
	lista_sortata = srv.sortare_filme("an si gen", "crescator");
	assert(lista_sortata.at(0).get_gen() == "a");
	assert(lista_sortata.at(1).get_gen() == "d");

	lista_sortata = srv.sortare_filme("an si gen", "descrescator");
	assert(lista_sortata.at(2).get_gen() == "d");
	assert(lista_sortata.at(3).get_gen() == "a");

	srv.sterge_film(1);
	srv.sterge_film(2);
	srv.sterge_film(3);
	srv.sterge_film(4);

}

void testeaza_iterator() {

	DynamicArray<Film> lista;
	Film f1(1, "a", "a", 1, "a");
	Film f2(2, "b", "b", 2, "b");
	Film f3(3, "c", "c", 3, "c");
	assert(lista.size() == 0);
	lista.push_back(f1);
	assert(lista.size() == 1);
	lista.push_back(f2);
	assert(lista.size() == 2);
	lista.push_back(f3);
	assert(lista.size() == 3);

	IteratorDynamicArray<Film> it = lista.begin();

	assert(it.valid() == true);

	assert(it.element().get_id() == 1);

	int ct = 1;

	for (const auto& f : lista) {

		assert(f.get_id() == ct);
		ct++;

	}

	it.next();

	assert(it.element().get_id() == 2);

}

void teste_cos() {

	Repository_filme_file repo("teste.txt");
	Cos cos(repo);
	Film f1(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel");
	Film f2(2, "The Wolf of the Wall Street", "Business", 2015, "Leonardo Di Caprio");
	repo.adauga_film(f1);
	repo.adauga_film(f2);
	repo.adauga_film(Film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh"));
	assert(repo.dimensiune() == 3);

	// test pentru adauga
	cos.adauga_in_cos(f1);
	assert(cos.numar_filme() == 1);


	// test pentru goleste
	cos.goleste_cos();
	assert(cos.numar_filme() == 0);

	// test pentru genereaza
	cos.genereaza_cos(2);
	assert(cos.numar_filme() == 2);
	try {

		cos.genereaza_cos(12);
		assert(false);
	}
	catch (CosError) {

		assert(true);
	}

	// test pentru exporta
	cos.goleste_cos();
	cos.adauga_in_cos(f1);
	cos.adauga_in_cos(f2);
	assert(cos.numar_filme() == 2);
	try {

		cos.exporta("");
		assert(false);
	}
	catch (CosError) {

		assert(true);
	}
	cos.exporta("test_exporta.txt");

	// test pentru get_cos
	cos.goleste_cos();
	cos.adauga_in_cos(f1);
	vector<Film> l = cos.get_cos();
	assert(l.at(0).get_id() == 1);

	repo.sterge_film(1);
	repo.sterge_film(2);
	repo.sterge_film(3);

}

void teste_service_cos() {

	Validator val;
	Repository_filme_file repo("teste.txt");
	Cos cos(repo);
	Service_filme srv(repo, val, cos);
	srv.adauga_film(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel");
	srv.adauga_film(2, "The Wolf of the Wall Street", "Business", 2015, "Leonardo Di Caprio");
	srv.adauga_film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh");

	srv.adauga_in_cos("Looking for Alaska");
	assert(srv.numar_filme_cos() == 1);

	Cos& cos1 = srv.getCos();

	vector<Film> vvv = cos1.get_cos();

	assert(vvv.size() == 1);

	vector<Film> vec = srv.get_cos_filme();
	assert(vec.at(0).get_id() == 3);

	srv.goleste_cos();
	assert(srv.numar_filme_cos() == 0);

	srv.adauga_random_cos(3);
	assert(srv.numar_filme_cos() == 3);

	srv.exporta_fisier("test_exporta.txt");

	srv.sterge_film(1);
	srv.sterge_film(2);
	srv.sterge_film(3);
}

void teste_cerinta_raport() {

	Validator val;
	Repository_filme_file repo("teste.txt");
	Cos cos(repo);
	Service_filme srv(repo, val, cos);
	srv.adauga_film(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel");
	srv.adauga_film(2, "The Wolf of the Wall Street", "Actiune", 2015, "Leonardo Di Caprio");
	srv.adauga_film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh");

	std::map<std::string, int> rez = srv.raport();
	int ok = 1;
	for (const auto& f : rez)
		if (ok == 1) {

			assert(f.first == "Actiune");
			assert(f.second == 2);
			ok = 0;
		}
		else {

			assert(f.first == "Drama");
			assert(f.second == 1);
		}

	srv.sterge_film(1);
	srv.sterge_film(2);
	srv.sterge_film(3);

}

void teste_undo() {

	Validator val;
	Repository_filme_file repo("teste.txt");
	Cos cos(repo);
	Service_filme srv(repo, val, cos);
	srv.adauga_film(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel");
	srv.adauga_film(2, "The Wolf of the Wall Street", "Actiune", 2015, "Leonardo Di Caprio");
	srv.adauga_film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh");

	// undo adauga
	vector<Film> lista_filme = srv.get_all();
	assert(lista_filme.size() == 3);
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.size() == 2);

	// undo sterge
	srv.sterge_film(2);
	lista_filme = srv.get_all();
	assert(lista_filme.size() == 1);
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.size() == 2);

	// undo modifica
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.size() == 1);

	// titlu
	srv.modifica_titlu_film(1, "a");
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_titlu() == "a");
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_titlu() == "Fast and Furious");

	// gen
	srv.modifica_gen_film(1, "a");
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_gen() == "a");
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_gen() == "Actiune");

	// an
	srv.modifica_anul_film(1, 1);
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_an_aparitie() == 1);
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_an_aparitie() == 2018);

	// actor
	srv.modifica_actor_film(1, "a");
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_actor_principal() == "a");
	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.at(0).get_actor_principal() == "Vin Diesel");

	srv.undo();
	lista_filme = srv.get_all();
	assert(lista_filme.size() == 0);
	try {

		srv.undo();
		assert(false);
	}
	catch (SrvError) {

		assert(true);
	}
}

void teste_repo_nou() {

	RepoLab repo(0);
	try {

		Film ff = repo.get_item_by_id(22);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// teste pentru adauga
	repo.adauga_film(Film(1, "Fast and Furious", "Actiune", 2018, "Vin Diesel"));
	repo.adauga_film(Film(2, "The Wolf of the Wall Street", "Business", 2015, "Leonardo Di Caprio"));
	repo.adauga_film(Film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh"));
	assert(repo.dimensiune() == 3);

	// teste pentru get item by title
	assert(repo.get_item_by_title("Fast and Furious").get_id() == 1);
	try {

		repo.get_item_by_title("asdasdas");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// teste pentru get all
	std::vector<Film> l = repo.get_all();
	assert(l.size() == 3);
	try {
		repo.adauga_film(Film(3, "Looking for Alaska", "Drama", 2018, "Christine Froseteh"));
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	assert(repo.dimensiune() == 3);

	// teste pentru cauta
	assert(repo.cauta_film(1) == true);
	assert(repo.cauta_film(7) == false);

	// teste pentru sterge
	try {

		repo.sterge_film(7);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}
	repo.sterge_film(3);
	assert(repo.dimensiune() == 2);

	// test pentru modifica titlu
	repo.modifica_titlu_film(2, "Modificat");
	l = repo.get_all();
	Film f = l.at(1);
	assert(f.get_titlu() == "Modificat");
	try {
		repo.modifica_titlu_film(22, "bbb");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica gen
	repo.modifica_gen_film(2, "Modificat");
	l = repo.get_all();
	assert(l.at(1).get_gen() == "Modificat");
	try {

		repo.modifica_gen_film(22, "Modificat");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica an
	repo.modifica_anul_film(2, 111);
	l = repo.get_all();
	assert(l.at(1).get_an_aparitie() == 111);
	try {
		repo.modifica_anul_film(22, 111);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru modifica actor principal
	repo.modifica_actor_film(2, "Modificat");
	l = repo.get_all();
	assert(l.at(1).get_actor_principal() == "Modificat");
	try {
		repo.modifica_actor_film(22, "Modificat");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// test pentru get item by id
	Film flm = repo.get_item_by_id(2);
	assert(flm.get_id() == 2);
	assert(flm.get_actor_principal() == "Modificat");

	repo.sterge_film(1);
	repo.sterge_film(2);

	RepoLab repo1(0);
	repo1 = repo1;
	repo1.adauga_film(Film(1, "a", "a", 1, "a"));
	repo1.adauga_film(Film(2, "b", "b", 2, "b"));
	repo1.adauga_film(Film(3, "c", "c", 3, "c"));
	assert(repo1.dimensiune() == 3);
	repo1.sterge_film(2);
	assert(repo1.dimensiune() == 2);
}

void teste_repo_nou_exceptii() {

	RepoLab repo(10);

	// adauga
	try {

		repo.adauga_film(Film(1, "a", "a", 1, "a"));
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// sterge
	try {

		repo.sterge_film(1);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// get all
	try {

		repo.get_all();
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// dimensiune
	try {

		repo.dimensiune();
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// cauta film
	try {

		repo.cauta_film(1);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// modifica titlu
	try {

		repo.modifica_titlu_film(1, "a");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// modifica gen
	try {

		repo.modifica_gen_film(1, "a");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// modifica anul
	try {

		repo.modifica_anul_film(1, 1);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// modifica titlu
	try {

		repo.modifica_actor_film(1, "a");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// get item by id
	try {

		repo.get_item_by_id(1);
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}

	// get item by title
	try {

		repo.get_item_by_title("a");
		assert(false);
	}
	catch (RepoError) {

		assert(true);
	}
}

void ruleaza_teste() {

	std::cout << "Se ruleaza testele pentru domain.....\n";
	teste_domain();
	std::cout << "Se ruleaza testele pentru repository.\n";
	teste_repo();
	testeaza_iterator();
	std::cout << "Se ruleaza testele pentru service....\n";
	teste_service();
	teste_filtrari();
	teste_sortari();
	teste_service_cos();
	teste_cerinta_raport();
	std::cout << "Se ruleaza testele pentru cos........\n";
	teste_cos();
	std::cout << "Se ruleaza testele pentru undo.......\n";
	teste_undo();
	std::cout << "Se ruleaza testele pentru repo nou...\n";
	teste_repo_nou();
	teste_repo_nou_exceptii();
	std::cout << "Testele au fost rulate cu succes!\n";
}