#include "Repository.h"
#include <fstream>

void Repository::load_from_file(){

	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id;
		string descriere, stare, prog = "";
		in >> id >> descriere;
		vector<string> lis;
		in >> prog;
		while (prog != "open" && prog != "inprogress" && prog != "closed") {

			lis.push_back(prog);
			in >> prog;
		}
		stare = prog;
		Task t{ id,descriere,lis,stare };
		this->lista.push_back(t);
	}
	in.close();
}

vector<Task> Repository::get_all(){

	return this->lista;
}

void Repository::adauga_task(Task t){

	for (auto el : this->lista)

		if (el.get_id() == t.get_id())

			throw string("Mai exista un task cu acelasi id!\n");

	this->lista.push_back(t);

	write_to_file();
}

void Repository::modifica_stare(int id, string stare_noua){

	for (int i = 0; i < this->lista.size(); i++)

		if (this->lista.at(i).get_id() == id)

			this->lista[i].set_stare(stare_noua);

	write_to_file();
}

void Repository::write_to_file(){

	std::ofstream out(this->nume_fisier);

	if (!out.is_open())

		return;

	int i = 0;

	for (auto el : this->lista) {

		out << el.get_id() << '\n';
		out << el.get_descriere() << '\n';
		for (auto p : el.get_lista())
			out << p << '\n';
		out << el.get_stare();
		if (i != this->lista.size() - 1)
			out << '\n';
		i++;
	}
	out.close();
}
