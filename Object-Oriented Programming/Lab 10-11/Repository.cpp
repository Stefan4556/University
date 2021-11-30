#include "Repository.h"
#include "Domain.h"
#include <string>
#include <iostream>

const std::vector<Film> Repository_filme::get_all() const noexcept(false) {

	return this->lista_filme;
}

int Repository_filme::dimensiune() const noexcept {

	return this->lista_filme.size();
}

bool Repository_filme::cauta_film(int id_cautat) {
	/*
		for (int i = 0; i < dimensiune(); i++) {

			if (this->lista_filme.at(i).get_id() == id_cautat)

				return true;
		}*/

		/*for (auto f : this->lista_filme) {

			if (f.get_id() == id_cautat)

				return true;
		}*/

	std::vector<Film>::iterator it = std::find_if(this->lista_filme.begin(), this->lista_filme.end(), [id_cautat](const Film& f) noexcept {return f.get_id() == id_cautat; });

	if (it != this->lista_filme.end())

		return true;

	return false;

}

void Repository_filme::adauga_film(const Film& f) {

	if (cauta_film(f.get_id()) == false) {	// inseamna ca filmul nu a mai fost adaugat inca o data

		this->lista_filme.push_back(f);
		//write_to_file();
		return;
	}

	throw RepoError("Acest film a mai fost adaugat o data!\n");
}

Film Repository_filme::sterge_film(int id) {

	if (cauta_film(id) == true) {
		/*
		for (int i = 0; i < this->lista_filme.size(); i++) {

			if (this->lista_filme.at(i).get_id() == id) {

				this->lista_filme.erase(i);	// sterge dupa id si faci stergere dupa 2 for uri
				return 1;
			}

		}*/
		auto it = this->lista_filme.begin();
		for (auto f : this->lista_filme) {

			if (f.get_id() == id) {

				Film fil = f;
				this->lista_filme.erase(it);
				//write_to_file();
				return fil;
			}
			it++;
		}}

	throw RepoError("Filmul pe care doriti sa-l stergeti nu exista!\n");
}

Film Repository_filme::modifica_titlu_film(int id, const std::string titlu_nou) {


	if (cauta_film(id) == true)

		/*for (int i = 0; i < dimensiune(); i++) {

			if (this->lista_filme.at(i).get_id() == id) {

				this->lista_filme.at(i).set_titlu(titlu_nou);
				return 1;
			}

		}*/

		for (auto& f : this->lista_filme) {

			if (f.get_id() == id) {

				Film fil = f;
				f.set_titlu(titlu_nou);
				//write_to_file();
				return fil;
			}
		}


	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film Repository_filme::modifica_gen_film(int id, const std::string gen_nou) {


	if (cauta_film(id) == true)

		/*for (int i = 0; i < dimensiune(); i++) {

			if (this->lista_filme.at(i).get_id() == id) {

				this->lista_filme.at(i).set_gen(gen_nou);
				return 1;
			}

		}*/
		for (auto& f : this->lista_filme) {

			if (f.get_id() == id) {

				Film fil = f;
				f.set_gen(gen_nou);
				//write_to_file();
				return fil;
			}
		}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film Repository_filme::modifica_anul_film(int id, const int an_nou) {


	if (cauta_film(id) == true)

		/*for (int i = 0; i < dimensiune(); i++) {

			if (this->lista_filme.at(i).get_id() == id) {

				this->lista_filme.at(i).set_an_aparitie(an_nou);
				return 1;
			}

		}*/
		for (auto& f : this->lista_filme) {

			if (f.get_id() == id) {

				Film fil = f;
				f.set_an_aparitie(an_nou);
				//write_to_file();
				return fil;
			}
		}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

Film Repository_filme::modifica_actor_film(int id, const std::string actor_nou) {


	if (cauta_film(id) == true)

		/*for (int i = 0; i < dimensiune(); i++) {

			if (this->lista_filme.at(i).get_id() == id) {

				this->lista_filme.at(i).set_actor_principal(actor_nou);
				return 1;
			}

		}*/
		for (auto& f : this->lista_filme) {

			if (f.get_id() == id) {

				Film fil = f;
				f.set_actor_principal(actor_nou);
				//write_to_file();
				return fil;
			}
		}

	throw RepoError("Filmul pe care doriti sa-l modificati nu exista!\n");}

const Film& Repository_filme::get_item_by_id(int id) {

	/*for (int i = 0; i < dimensiune(); i++) {

		if (this->lista_filme.at(i).get_id() == id)

			return this->lista_filme.at(i);
	}*/

	for (auto& f : this->lista_filme) {

		if (f.get_id() == id) {

			return f;
		}
	}

	throw RepoError("Nu exista in lista un film cu acest id!\n");
}

Film Repository_filme::get_item_by_title(std::string titlu) {

	for (auto& f : this->lista_filme) {

		if (f.get_titlu() == titlu) {

			return f;
		}
	}

	throw RepoError("Nu exista in lista un film cu acest nume!\n");}

void Repository_filme_file::read_from_file() {

	std::string line;
	std::ifstream in(this->nume_fisier);

	if (!in.is_open())

		throw RepoError("Nu s-a putut deschide fisierul!\n");

	std::string linie;

	getline(in, linie);

	while (linie != "") {


		std::string titlu, gen, actor_principal, an_s, id_s;

		int an = 0, id = 0;

		std::istringstream iss(linie);

		iss >> id_s >> titlu >> gen >> an_s >> actor_principal;

		an = stoi(an_s);

		id = stoi(id_s);

		const Film f(id, titlu, gen, an, actor_principal);

		adauga_film(f);

		getline(in, linie);
	}

	in.close();
}

void Repository_filme_file::write_to_file() {

	std::ofstream out(this->nume_fisier);

	if (!out.is_open())

		throw RepoError("Nu s-a putut deschide fisierul!\n");

	std::vector<Film> lista = Repository_filme::get_all();

	for (auto& f : lista) {

		out << f.get_id() << " " << f.get_titlu() << " " << f.get_gen() << " " << f.get_an_aparitie() << " " << f.get_actor_principal() << '\n';
	}

	out.close();
}