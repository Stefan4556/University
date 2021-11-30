#include "GUI.h"

void GUI::initGuiDesign()
{
	QVBoxLayout* lay = new QVBoxLayout;

	this->setLayout(lay);

	this->tabel = new QTableWidget;
	lay->addWidget(tabel);

	this->culoare = new QLineEdit;
	lay->addWidget(culoare);

	QHBoxLayout* lay2 = new QHBoxLayout;

	this->sortare_grosime = new QPushButton("Sortare grosime");
	this->sortare_titlu = new QPushButton("Sortare titlu");
	this->nesortat = new QPushButton("Nesortat");

	lay->addLayout(lay2);
}
