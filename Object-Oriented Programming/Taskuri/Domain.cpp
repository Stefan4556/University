#include "Domain.h"

void Validator::valideaza(Task t) {

	string erori = "";

	if (t.get_descriere() == "")

		erori += "Descrierea nu poate sa fie vida!\n";

	if (t.get_stare() != "open" && t.get_stare() != "inprogress" && t.get_stare() != "closed")

		erori += "Starea nu este corecta!\n";

	if (t.get_lista().size() < 1 || t.get_lista().size() > 4)

		erori += "Eroare la lista de programatori!\n";

	if (erori != "")

		throw erori;}