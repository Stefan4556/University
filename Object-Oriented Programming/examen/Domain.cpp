#include "Domain.h"

int Carte::get_id(){

	return id;
}

string Carte::get_titlu()
{
	return titlu;
}

string Carte::get_tip()
{
	return tip;
}

double Carte::get_pret()
{
	return pret;
}

void Validator::valideaza(Carte c)
{
	string erori = "";

	if (c.get_titlu() == "")

		erori += "Titlul este vid!\n";

	if (c.get_pret() < 1 || c.get_pret() > 100)

		erori += "Pret invalid!\n";

	if (erori != "")

		throw erori;}
