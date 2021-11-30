/*
#include<iostream>
#include <string>

#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include "Ui.h"

void Console::afiseaza_meniu() {

	std::cout << "			Meniu\n\n";
	std::cout << "1) Adauga un film.\n";
	std::cout << "2) Sterge un film. \n";
	std::cout << "3) Modifica un camp al unui film. \n";
	std::cout << "4) Cauta un film.\n";
	std::cout << "5) Filtrare lista de filme. \n";
	std::cout << "6) Sortare lista de filme. \n";
	std::cout << "7) Afisare lista filme. \n";
	std::cout << "8) Adauga un film dupa titlu in cos\n";
	std::cout << "9) Genereaza random un cos\n";
	std::cout << "10) Goleste cos de filme\n";
	std::cout << "11) Export intr-un fisier al cosului de filme\n";
	std::cout << "12) Afiseaza filme din cosul curent\n";
	std::cout << "13) Cerinta laborator - raport dupa gen\n";
	std::cout << "14) Undo\n";
	std::cout << "15) Exit. \n";

}

Console::Console(Service_filme& srv) noexcept :service(srv) {

}

void Console::adauga_film() {

	std::string titlu, gen, actor;

	int an, id;

	std::cout << "Introduceti id-ul filmului: ";
	std::cin >> id;

	std::cin.get();
	std::cout << "Introduceti titlul filmului: ";
	getline(std::cin, titlu);

	std::cout << "Introduceti genul filmului: ";
	getline(std::cin, gen);

	std::cout << "Introduceti anul filmului: ";
	std::cin >> an;

	std::cin.get();
	std::cout << "Introduceti actorul principal filmului: ";
	getline(std::cin, actor);

	try {
		this->service.adauga_film(id, titlu, gen, an, actor);	// grija cand citesti un film dar cu id diferit ca trece de validari
		std::cout << "Filmul a fost adaugat cu succes!\n\n";
	}
	catch (const ValidationError& err) {

		std::cout << err.getMessage();
	}
	catch (const RepoError& err) {

		std::cout << err.getMessage();
	}
}

void Console::afisare_filme(std::vector<Film> lista) {

	for (auto& f : lista)

		std::cout << "Id: " << f.get_id() << " Titlu: " << f.get_titlu() << " Gen: " << f.get_gen() << " Anul aparitiei: " << f.get_an_aparitie() << " Actor principal: " << f.get_actor_principal() << '\n';


}

void Console::sterge_film() {

	int id;

	std::cout << "Introduceti id-ul filmului pe care doriti sa l stergeti: ";
	std::cin >> id;
	std::cin.get();

	try {

		this->service.sterge_film(id);
		std::cout << "Filmul a fost sters cu succes!\n";
	}
	catch (const ValidationError& err) {

		std::cout << err.getMessage();
	}
	catch (const RepoError& err) {

		std::cout << err.getMessage();
	}

}

void Console::cauta_film() {

	int id;

	std::cout << "Introduceti id-ul filmului pe care doriti sa l cautati: ";
	std::cin >> id;
	std::cin.get();

	try {

		this->service.cauta_film(id);

		const Film& f = this->service.get_item_by_id(id);
		std::cout << "Id: " << f.get_id() << " Titlu: " << f.get_titlu() << " Gen: " << f.get_gen() << " Anul aparitiei: " << f.get_an_aparitie() << " Actor principal: " << f.get_actor_principal() << '\n';
	}
	catch (const ValidationError& err) {

		std::cout << err.getMessage();
	}
	catch (const SrvError& err) {

		std::cout << err.getMessage();
	}
}

void Console::modifica_film() {

	std::string raspuns;

	int id = 0;

	std::cout << "Introduceti id-ul obiectului pe care doriti sa-l modificati: ";
	std::cin >> id;

	std::cin.get();
	std::cout << "Introduceti ce camp doriti sa schimbati (titlul/gen/an/actor): ";
	getline(std::cin, raspuns);

	if (raspuns == "titlul") {

		std::string titlu_nou;
		std::cout << "Introduceti noul titlul al filmului selectat: ";
		getline(std::cin, titlu_nou);

		try {

			this->service.modifica_titlu_film(id, titlu_nou);
			std::cout << "Filmul a fost modificat cu succes!\n";
		}
		catch (const ValidationError& err) {

			std::cout << err.getMessage();
		}
		catch (const RepoError& err) {

			std::cout << err.getMessage();
		}
	}
	else if (raspuns == "gen") {

		std::string gen_nou;
		std::cout << "Introduceti noul gen al filmului selectat: ";
		getline(std::cin, gen_nou);

		try {

			this->service.modifica_gen_film(id, gen_nou);
			std::cout << "Filmul a fost modificat cu succes!\n";
		}
		catch (const ValidationError& err) {

			std::cout << err.getMessage();
		}
		catch (const RepoError& err) {

			std::cout << err.getMessage();
		}
	}
	else if (raspuns == "an") {

		int an_nou;
		std::cout << "Introduceti noul an al filmului selectat: ";
		std::cin >> an_nou;
		std::cin.get();
		try {

			this->service.modifica_anul_film(id, an_nou);
			std::cout << "Filmul a fost modificat cu succes!\n";
		}
		catch (const ValidationError& err) {

			std::cout << err.getMessage();
		}
		catch (const RepoError& err) {

			std::cout << err.getMessage();
		}
	}
	else if (raspuns == "actor") {

		std::string actor_nou;
		std::cout << "Introduceti noul actor principal al filmului selectat: ";
		getline(std::cin, actor_nou);

		try {

			this->service.modifica_actor_film(id, actor_nou);
			std::cout << "Filmul a fost modificat cu succes!\n";
		}
		catch (const ValidationError& err) {

			std::cout << err.getMessage();
		}
		catch (const RepoError& err) {

			std::cout << err.getMessage();
		}
	}
	else {

		std::cout << "Nu s a ales vreo modificare!\n";
	}
}

void Console::filtrare_filme() {

	std::cout << "Introduceti campul dupa care doriti sa filtrati(titlu/an): ";
	std::string raspuns;
	std::cin >> raspuns;
	if (raspuns == "titlu") {

		std::cout << "Introduceti subsirul ce doriti sa fie regasit in titlul filmelor: ";
		std::string titlu;
		std::cin >> titlu;
		std::cin.get();

		std::vector<Film> lista_filtrata = this->service.filtrare_titlu(titlu);
		afisare_filme(lista_filtrata);
	}
	else if (raspuns == "an") {

		std::cout << "Introduceti anul maxim pe care-l poate avea un film: ";
		int an;
		std::cin >> an;
		std::cin.get();

		std::vector<Film> lista_filtrata = this->service.filtrare_an(an);
		afisare_filme(lista_filtrata);
	}
	else {

		std::cout << "Nu a fost un ales un criteriu de filtrare!\n";
		std::cin.get();
	}
}

void Console::sortare_filme() {

	std::cout << "Introduceti campul dupa care doriti sa realizati sortarea(titlu/actor/an si gen): ";
	std::string raspuns;
	getline(std::cin, raspuns);

	std::string ordine;
	std::cout << "Introduceti daca doriti sa sortati crescator sau descrescator filmele(crescator/descrescator): ";
	getline(std::cin, ordine);

	if (raspuns != "titlu" && raspuns != "actor" && raspuns != "an si gen") {

		std::cout << "Campul introdus este invalid!\n";
		return;
	}

	if (ordine != "crescator" && ordine != "descrescator") {

		std::cout << "Oridinea introdusa este invalida!\n";
		return;
	}

	std::vector<Film> lista_sortata = this->service.sortare_filme(raspuns, ordine);
	afisare_filme(lista_sortata);
}

void Console::adauga_cos_titlu() {

	string titlu;
	std::cout << "Introduceti titlul filmului pe care doriti sa-l adaugati: ";
	getline(std::cin, titlu);
	try {

		this->service.adauga_in_cos(titlu);
		std::cout << "Filmul a fost adaugat cu succes in cos!\n";
	}
	catch (const RepoError& err) {

		std::cout << err.getMessage();
	}
}

void Console::adauga_cos_random() {

	unsigned int nr_filme;
	std::cout << "Introduceti numarul de filme pe care doriti sa-l adaugati: ";
	std::cin >> nr_filme;
	std::cin.get();
	try {

		this->service.adauga_random_cos(nr_filme);
		std::cout << "Au fost adaugate cu succes " << nr_filme << " filme!\n";
	}
	catch (const CosError& err) {

		std::cout << err.getMessage();
	}
}

void Console::goleste_cos() {

	this->service.goleste_cos();
	std::cout << "Cosul de filme a fost golit!\n";
}

void Console::export_cos() {

	string fisier;
	std::cout << "Introduceti numele fisierului(cu sau fara full path): ";
	getline(std::cin, fisier);

	try {

		this->service.exporta_fisier(fisier);
		std::cout << "Cosul de filme a fost exportat cu succes in fisier!\n";
	}
	catch (const CosError& err) {

		std::cout << err.getMessage();
	}
}

void Console::afiseaza_cos() {

	vector<Film> cos = this->service.get_cos_filme();
	afisare_filme(cos);
}

void Console::cerinta_lab_raport() {

	std::map<std::string, int> rez = this->service.raport();

	for (const auto& el : rez)

		std::cout << "Genul: " << el.first << " Numar de filme: " << el.second << "\n";
}

void Console::undo_lista() {

	try {

		this->service.undo();
		std::cout << "A fost efectuat undo-ul!\n";
	}
	catch (const SrvError& err) {

		std::cout << err.getMessage();
	}
}

void Console::run() {

	while (true) {

		afiseaza_meniu();

		std::string cmd;

		std::cout << "Introduceti comanda: ";

		getline(std::cin, cmd);
		std::cout << "\n";

		if (cmd == "15") {

			std::cout << "La revedere!";
			return;
		}
		else if (cmd == "1") {

			adauga_film();
		}
		else if (cmd == "2") {

			sterge_film();
		}
		else if (cmd == "3") {

			modifica_film();
		}
		else if (cmd == "4") {

			cauta_film();
		}
		else if (cmd == "5") {

			filtrare_filme();
		}
		else if (cmd == "6") {

			sortare_filme();
		}
		else if (cmd == "7") {
			try {
				const std::vector<Film> lista = this->service.get_all();
				afisare_filme(lista);
			}
			catch (const RepoError& err) {

				std::cout << err.getMessage();
			}
		}
		else if (cmd == "8") {

			adauga_cos_titlu();
		}
		else if (cmd == "9") {

			adauga_cos_random();
		}
		else if (cmd == "10") {

			goleste_cos();
		}
		else if (cmd == "11") {

			export_cos();
		}
		else if (cmd == "12") {

			afiseaza_cos();
		}
		else if (cmd == "13") {

			cerinta_lab_raport();//this->service.Raport();
		}
		else if (cmd == "14") {

			undo_lista();
		}
		else {

			std::cout << "Comanda invalida!\n";
		}

		std::cout << "\nNumar filme din cos: " << this->service.numar_filme_cos() << '\n';

	}
}*/