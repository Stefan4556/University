#include "GUI.h"
#include <unordered_map>
#include "Clasa_generica.h"

void GUI::initGUI(){

	QVBoxLayout* lay = new QVBoxLayout;
	this->setLayout(lay);

	tabel_view = new QTableView;
	model_tabel = new MyTableModel(srv.sortare_pret());
	tabel_view->setModel(model_tabel);
	lay->addWidget(tabel_view);

	id = new QLabel("Id");
	lay->addWidget(id);
	id_l = new QLineEdit;
	lay->addWidget(id_l);
	nume = new QLabel("Nume");
	lay->addWidget(nume);
	nume_l = new QLineEdit;
	lay->addWidget(nume_l);
	tip = new QLabel("Tip");
	lay->addWidget(tip);
	tip_l = new QLineEdit;
	lay->addWidget(tip_l);
	pret = new QLabel("Pret");
	lay->addWidget(pret);
	pret_l = new QLineEdit;
	lay->addWidget(pret_l);
	adauga = new QPushButton("Adauga");
	lay->addWidget(adauga);

	slider = new QSlider(Qt::Horizontal);
	slider->setMinimum(1);
	slider->setMaximum(100);
	lay->addWidget(slider);

}

void GUI::connectButtons(){

	QObject::connect(adauga, &QPushButton::clicked, this, [this]() {

		auto Id = id_l->text().toInt();
		id_l->clear();
		auto Nume = nume_l->text().toStdString();
		nume_l->clear();
		auto Tip = tip_l->text().toStdString();
		tip_l->clear();
		auto Pret = pret_l->text().toDouble();
		pret_l->clear();

		try {

			this->srv.adauga_produs(Id, Nume, Tip, Pret);
			this->model_tabel->setTable(this->srv.sortare_pret());
		}
		catch (const string& err) {

			QMessageBox::critical(nullptr, "Eroare", QString::fromStdString(err));
		}
	});

	QObject::connect(slider, &QSlider::valueChanged, this, [this]() {

		int val = slider->value();
		this->model_tabel->set_filtru(val);
		this->model_tabel->setTable(this->srv.sortare_pret());
	});
}

void GUI::setInitGUI(){	

	vector<Produs> v = this->srv.get_all();

	// ceva vec de frecv

	std::unordered_map<string, int> dict;

	for (auto el : v) {

		string tip = el.get_tip();

		if (dict[tip] == 0)

			dict[tip] = 1;
	}

	for (auto el : dict) {

		Generic_class* g = new Generic_class(this->srv, el.first);
		g->show();
	}
}
