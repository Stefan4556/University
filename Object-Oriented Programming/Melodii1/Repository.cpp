#include "Repository.h"
#include <fstream>

void Repository::load_from_file(){

	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id;
		string titlu, artist, gen;
		in >> id >> titlu >> artist >> gen;
		Melodie m{ id,titlu,artist,gen };
		this->lista.push_back(m);
	}
	in.close();
}

void Repository::write_to_file(){

	std::ofstream out(this->nume_fisier);

	if (!out.is_open())

		return;

	int i = 0; 

	for (auto elem : lista) {

		out << elem.get_id() << '\n';
		out << elem.get_titlu() << '\n';
		out << elem.get_artist() << '\n';
		out << elem.get_gen();
		if (i != lista.size() - 1)
			out << '\n';
		i++;
	}

	out.close();
}

vector<Melodie> Repository::get_all(){

	return this->lista;
}

void Repository::adauga_melodie(Melodie m){

	this->lista.push_back(m);

	write_to_file();
}

void Repository::sterge_melodie(int id){

	vector<Melodie>::iterator it;

	for(auto itr = this->lista.begin(); itr != this->lista.end(); itr++)

		if ((*itr).get_id() == id) {

			it = itr;
			break;
		}

	this->lista.erase(it);

	write_to_file();
}
