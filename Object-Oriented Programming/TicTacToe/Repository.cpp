#include "Repository.h"
#include <fstream>

void Repository::load_from_file(){

	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		return;

	while (!in.eof()) {

		int id, dim;
		string tabla, jucator, stare, aux;
		in >> id;
		if (in.eof())
			break;
		in >> dim >> tabla >> jucator >> stare;
		if (stare == "In") {

			in >> aux;
			stare += " ";
			stare += aux;
		}
		Joc j{ id,dim,tabla,jucator,stare };
		this->lista.push_back(j);
	}
	in.close();
}

void Repository::write_to_file() {

	std::ofstream out(this->nume_fisier);

	for (auto el : this->lista) {

		out << el.get_id() << " " << el.get_dim() << " " << el.get_tabla() << " " << el.get_jucator() << " " << el.get_stare() << '\n';
	}

	out.close();
}

vector<Joc> Repository::get_all(){
	
	return this->lista;
}

void Repository::adauga_joc(Joc j){

	this->lista.push_back(j);
	write_to_file();
}

void Repository::modifica_joc(int id, int dim, string tabla, string jucator, string stare) {

	for (int i = 0; i < this->lista.size(); i++) {

		if (this->lista.at(i).get_id() == id) {

			this->lista[i].set_dim(dim);
			this->lista[i].set_tabla(tabla);
			this->lista[i].set_jucator(jucator);
			this->lista[i].set_stare(stare);
			break;
		}
	}
	write_to_file();
}

Joc Repository::get_item_by_id(int id){

	for (auto elem : this->lista)

		if (elem.get_id() == id)

			return elem;}
