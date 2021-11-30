#include "GUI.h"
#include "QDebug"

#include "Clasa_generica.h"

void GUI::initGUI(){

	QVBoxLayout* lay = new QVBoxLayout;
	this->setLayout(lay);

	//tabel = new QTableWidget;
	tabel = new Tabel(this->srv);
	lay->addWidget(tabel);

	id_lab = new QLabel("Id");
	lay->addWidget(id_lab);
	id_l = new QLineEdit;
	lay->addWidget(id_l);
	descriere_lab = new QLabel("Descriere");
	lay->addWidget(descriere_lab);
	descriere_l = new QLineEdit;
	lay->addWidget(descriere_l);
	programatori_lab = new QLabel("Programatori");
	lay->addWidget(programatori_lab);
	programatori_l = new QLineEdit;
	lay->addWidget(programatori_l);
	stare_lab = new QLabel("Stare");
	lay->addWidget(stare_lab);
	stare_l = new QLineEdit;
	lay->addWidget(stare_l);
	adauga = new QPushButton("Adauga");
	lay->addWidget(adauga);

	search = new QLabel("Search");
	lay->addWidget(search);
	nume_search = new QLineEdit;
	lay->addWidget(nume_search);
}

void GUI::connectButtons(){

	QObject::connect(adauga, &QPushButton::clicked, this, [this]() {

		auto id = id_l->text().toInt();
		id_l->clear();
		auto descriere = descriere_l->text().toStdString();
		descriere_l->clear();
		auto prog_text = programatori_l->text();
		programatori_l->clear();
		vector<string> programatori;
		if (prog_text.size() != 0) {

			auto prog_lista = programatori_l->text().split(" ");

			for (auto el : prog_lista)
				programatori.push_back(el.toStdString());
		}
		qDebug() << programatori.size();
		auto stare = stare_l->text().toStdString();
		stare_l->clear();
		try {

			this->srv.adauga_task(id, descriere, programatori, stare);
			tabel->update();
		}
		catch (const string& err) {

			QMessageBox::warning(nullptr, "Eroare", QString::fromStdString(err));
		}
	});

	QObject::connect(nume_search, &QLineEdit::textEdited, this, [this]() {

		auto str = nume_search->text().toStdString();
		tabel->set_update_filtru(str);
		tabel->update();
	});
}

void GUI::initStateGui(){

	//load_items_into_table(this->srv.sortare_stare());
	tabel->update();

	Generic_class* c_open = new Generic_class(this->srv, "open");
	c_open->show();
	Generic_class* c_inprogress = new Generic_class(this->srv, "inprogress");
	c_inprogress->show();
	Generic_class* c_closed = new Generic_class(this->srv, "closed");
	c_closed->show();
}
/*
void GUI::load_items_into_table(vector<Task> v){

	tabel->setRowCount(v.size());
	tabel->setColumnCount(4);

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
}*/
