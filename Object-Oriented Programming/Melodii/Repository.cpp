#include "Repository.h"
#include <exception>

void Repository::load_from_file() {

	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id, rank;
		string titlu, artist;
		in >> id >> titlu >> artist >> rank;
		Melodie m{ id,titlu,artist,rank };
		lista.push_back(m);
	}
	in.close();
}

void Repository::write_to_file() {

	std::ofstream out(this->nume_fisier);

	if (!out.is_open())

		return;

	int i = 0;

	for (auto el : this->lista) {

		out << el.get_id() << '\n';
		out << el.get_titlu() << '\n';
		out << el.get_artist() << '\n';
		out << el.get_rank();
		if (i != this->lista.size() - 1)
			out << '\n';
		i++;
	}
	out.close();
}

vector<Melodie> Repository::get_all() {

	return this->lista;
}

void Repository::modifica_titlu_rank(int id, string titlu_nou, int rank_nou) {

	for(int i = 0 ; i < this->lista.size(); i++)

		if (this->lista.at(i).get_id() == id) {

			this->lista[i].set_rank(rank_nou);
			this->lista[i].set_titlu(titlu_nou);
			break;
		}
	write_to_file();
}

void Repository::sterge(string titlu){

	string artist = "default";
	vector<Melodie>::iterator it;

	for(auto itr = this->lista.begin(); itr != this->lista.end(); itr++)

		if ((*itr).get_titlu() == titlu) {

			artist = (*itr).get_artist();
			it = itr;
		}

	int ct = 0;

	for (auto el : this->lista)

		if (el.get_artist() == artist)

			ct++;

	if (ct == 1)

		throw std::exception();

	this->lista.erase(it);

	write_to_file();
}
