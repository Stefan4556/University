#include "Clasa_generica.h"
#include <QListWidgetItem>

void Generic_class::initGUI(){

	lay = new QVBoxLayout;
	this->setLayout(lay);

	lista = new QListWidget;
	lay->addWidget(lista);

	QHBoxLayout* lay1 = new QHBoxLayout;
	lay->addLayout(lay1);

	open = new QPushButton("Open");
	inprogress = new QPushButton("Inprogress");
	close = new QPushButton("Close");
	lay1->addWidget(open);
	lay1->addWidget(inprogress);
	lay1->addWidget(close);
}

void Generic_class::connectButtons(){

	QObject::connect(lista, &QListWidget::itemClicked, this, [this]() {

		auto txt = lista->currentItem()->text().split(" ");
		int id = txt.at(0).toInt();
		this->id_modifica = id;
	});

	QObject::connect(open, &QPushButton::clicked, this, [this]() {
		
		this->srv.modifica_stare(id_modifica, "open");
	});

	QObject::connect(inprogress, &QPushButton::clicked, this, [this]() {

		this->srv.modifica_stare(id_modifica, "inprogress");
	});

	QObject::connect(close, &QPushButton::clicked, this, [this]() {

		this->srv.modifica_stare(id_modifica, "closed");
	});
}

void Generic_class::setInitStateGUI(){

	load_items_into_list(this->srv.filtrare_stare(this->stare));
}

void Generic_class::update(){

	load_items_into_list(this->srv.filtrare_stare(this->stare));
}

void Generic_class::load_items_into_list(vector<Task> v){

	lista->clear();

	for (auto el : v) {

		auto text = QString::fromStdString(std::to_string(el.get_id()) + " " + el.get_descriere());
		QListWidgetItem* it = new QListWidgetItem(text);
		lista->addItem(it);
	}
}
