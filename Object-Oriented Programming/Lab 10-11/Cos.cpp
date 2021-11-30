#include "Cos.h"

void Cos::goleste_cos() noexcept {

	lista.clear();
	notify();
}

void Cos::adauga_in_cos(const Film& f) {	// arunca exceptii in service
	/*
	* try {

		cos.adauga_in_cos("dsadasda");
		assert(false);
	}
	catch (CosError) {

		assert(true);
	}
	*/
	lista.push_back(f);
	notify();
}

void Cos::genereaza_cos(unsigned int numar_total) {

	vector<Film> lis = this->repo.get_all();

	unsigned int i = 0;

	if (numar_total > lis.size())

		throw CosError("Nu exista atatea filme in lista de filme!\n");

	vector<Film>cos_nou = lis;

	//unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
	std::mt19937 mt{ std::random_device{}() };
	const std::uniform_int_distribution<> dist(0, static_cast<int>(cos_nou.size()) - 1);
	const int rndNr = dist(mt);// numar aleator intre [0,size-1]
	std::shuffle(cos_nou.begin(), cos_nou.end(), std::default_random_engine(rndNr));

	auto it = cos_nou.begin();

	while (i < numar_total) {

		lista.push_back(*it);
		it++;
		i++;
	}
	notify();
}

void Cos::exporta(const string& nume_fisier) {

	vector<Film> cos_filme = get_cos();

	std::ofstream out{ nume_fisier };

	if (!out.is_open())

		throw CosError("A aparut o eroare la creearea fisierului!\n");

	for (const auto& f : cos_filme) {

		out << f.get_id() << ", " << f.get_titlu() << ", " << f.get_gen() << ", " << f.get_an_aparitie() << ", " << f.get_actor_principal() << '\n';
	}

	out.close();

}

int Cos::numar_filme() noexcept {

	return static_cast<int>(lista.size());
}

vector<Film> Cos::get_cos() {

	return lista;
}
/*
void Cos::mentenanta_stergere(int id) {

	for (auto it = lista.begin(); it != lista.end(); it++)

		if ((*it).get_id() == id) {

			vector<Film>::iterator a = remove(lista.begin(), lista.end(), (*it));
			return;
		}
}*/