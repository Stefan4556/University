#include "Domain.h"

void Validator::valideaza(Produs p) {

	string erori = "";

	if (p.get_nume() == "")

		erori += "Numele nu poate sa fie vid!\n";

	if (p.get_pret() < 1 || p.get_pret() > 100)

		erori += "Pretul nu este in intervalul 1-100!\n";

	if (erori != "")

		throw erori;}