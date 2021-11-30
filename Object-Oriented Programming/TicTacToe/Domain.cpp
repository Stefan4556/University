#include "Domain.h"

void Joc::set_dim(int dim_noua) {

	dim = dim_noua;
}

void Joc::set_tabla(string tabla_noua){

	tabla = tabla_noua;
}

void Joc::set_jucator(string jucator_nou){

	jucator = jucator_nou;
}

void Joc::set_stare(string stare_noua){

	stare = stare_noua;
}

void Validator::valideaza(Joc j) {

	string erori = "";

	if (j.get_dim() < 3 || j.get_dim() > 5)

		erori += "Dimensiunea jocului este gresita!\n";

	if (j.get_tabla().size() != j.get_dim() * 3)

		erori += "Tabla de joc nu are dimensiunea potrivita!\n";

	else{	// trebuie sa verificam daca elementele acesteia sunt ok
		
		string tab = j.get_tabla();

		bool ok = true;

		for (int i = 0; i < tab.size(); i++)

			if (tab[i] != 'X' && tab[i] != 'O' && tab[i] != '-')

				ok = false;

		if (ok == false)

			erori += "Tabla de joc contine caractere incorecte!\n";
	}

	if (j.get_jucator() != "X" && j.get_jucator() != "O")

		erori += "Jucatorul care urmeaza este gresit!\n";

	if (j.get_stare() != "Neinceput" && j.get_stare() != "In derulare" && j.get_stare() != "Terminat")

		erori += "Starea jocului este incorecta!\n";

	if (erori != "")

		throw erori;
}