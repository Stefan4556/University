#include "Clasa_generica.h"

void Clasa_generica::initGUI()
{
	
	this->srv.addObserver(this);

	this->setWindowTitle(QString::fromStdString(nume));

	lay = new QVBoxLayout;
	this->setLayout(lay);
	
	lista = new QListWidget;
	lay->addWidget(lista);

}

void Clasa_generica::setInitState()
{

	load_items_into_lista();

}

void Clasa_generica::update()
{

	load_items_into_lista();

}

void Clasa_generica::load_items_into_lista()
{

	lista->clear();

	vector<Carte> v = this->srv.get_lista_tip(nume);

	for (auto elem : v) {

		auto id_s = std::to_string(elem.get_id());
		auto pret_s = std::to_string(elem.get_pret());

		auto text = QString::fromStdString(id_s + " " + elem.get_titlu() + " " + elem.get_tip() + " " + pret_s);
		QListWidgetItem* it = new QListWidgetItem(text);
		lista->addItem(it);
	}

}
