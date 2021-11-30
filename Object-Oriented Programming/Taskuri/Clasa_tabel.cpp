#include "Clasa_tabel.h"

void Tabel::initGUI(){

	lay = new QVBoxLayout;
	this->setLayout(lay);

	tabel = new QTableWidget;
	lay->addWidget(tabel);

	load_items_into_table();
}

void Tabel::load_items_into_table(){

	vector<Task> v;

	if (this->update_filtru == true) {

		v = this->srv.filtrare(filtru);
		update_filtru = false;
		filtru = "";
	}
	else
		
		v = this->srv.sortare_stare();

	tabel->setColumnCount(4);
	tabel->setRowCount(v.size());

	int i = 0;
	for (auto el : v) {

		QTableWidgetItem* it0 = new QTableWidgetItem(QString::fromStdString(std::to_string(el.get_id())));
		tabel->setItem(i, 0, it0);

		QTableWidgetItem* it1 = new QTableWidgetItem(QString::fromStdString(el.get_descriere()));
		tabel->setItem(i, 1, it1);

		QTableWidgetItem* it2 = new QTableWidgetItem(QString::fromStdString(std::to_string(el.get_lista().size())));
		tabel->setItem(i, 2, it2);

		QTableWidgetItem* it3 = new QTableWidgetItem(QString::fromStdString(el.get_stare()));
		tabel->setItem(i, 3, it3);

		i++;
	}
}

void Tabel::update(){

	load_items_into_table();
}
