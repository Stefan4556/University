#include "Service.h"
#include <algorithm>

vector<Task> Service::get_all(){

	return this->repo.get_all();
}

vector<Task> Service::sortare_stare(){

	vector<Task> rez = this->repo.get_all();

	std::sort(rez.begin(), rez.end(), [](Task t1, Task t2) {

		return t1.get_stare() < t2.get_stare();
	});

	return rez;
}

void Service::adauga_task(int id, string descriere, vector<string> lista, string stare){
	
	Task t{ id,descriere,lista,stare };
	this->val.valideaza(t);
	this->repo.adauga_task(t);
	notify();
}

vector<Task> Service::filtrare(string str){

	vector<Task> rez;
	vector<Task> elem = this->repo.get_all();

	for (auto el : elem) {

		vector<string> prog = el.get_lista();

		bool ok = true;

		for (auto p : prog)

			if (p.find(str) == string::npos)

				ok = false;

		if (ok == true)

			rez.push_back(el);
	}

	return rez;
}

void Service::modifica_stare(int id, string stare_noua){

	this->repo.modifica_stare(id, stare_noua);
	notify();
}

vector<Task> Service::filtrare_stare(string stare){

	vector<Task> rez;
	vector<Task> elems = this->repo.get_all();

	for (auto el : elems)

		if (el.get_stare() == stare)

			rez.push_back(el);

	return rez;
}
