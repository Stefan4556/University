#include "GUI.h"
#include "Clasa_generica.h"
#include <unordered_map>

void GUI::initGUI()
{
	
	QVBoxLayout* lay = new QVBoxLayout;
	this->setLayout(lay);

	tabel_view = new QTableView;
	model_tabel = new MyTableModel(this->srv.sortare_litere());
	tabel_view->setModel(model_tabel);
	lay->addWidget(tabel_view);

	slider = new QSlider(Qt::Horizontal);
	slider->setMinimum(0);
	slider->setMaximum(100);
	lay->addWidget(slider);

	id_lab = new QLabel("Id");
	lay->addWidget(id_lab);
	id_l = new QLineEdit;
	lay->addWidget(id_l);
	titlu_lab = new QLabel("Titlu");
	lay->addWidget(titlu_lab);
	titlu_l = new QLineEdit;
	lay->addWidget(titlu_l);
	tip_lab = new QLabel("Tip");
	lay->addWidget(tip_lab);
	tip_l = new QLineEdit;
	lay->addWidget(tip_l);
	pret_lab = new QLabel("Pret");
	lay->addWidget(pret_lab);
	pret_l = new QLineEdit;
	lay->addWidget(pret_l);
	adauga = new QPushButton("Adauga");
	lay->addWidget(adauga);
}

void GUI::connectButtons(){

	QObject::connect(slider, &QSlider::valueChanged, this, [this]() {

		auto val = slider->value();
		model_tabel->set_filtru(val);
		model_tabel->setTabel(this->srv.sortare_litere());
	});

	QObject::connect(adauga, &QPushButton::clicked, this, [this]() {

		auto id = id_l->text().toInt();
		auto titlu = titlu_l->text().toStdString();
		auto tip = tip_l->text().toStdString();
		auto pret = pret_l->text().toDouble();
		id_l->clear();
		titlu_l->clear();
		tip_l->clear();
		pret_l->clear();

		try {

			this->srv.adauga_carte(id, titlu, tip, pret);
			model_tabel->setTabel(this->srv.sortare_litere());
		}
		catch (const string& err) {

			QMessageBox::warning(nullptr, "Eroare", QString::fromStdString(err));
		}
	});
}

void GUI::setInitGUI()
{

	std::unordered_map<string, bool> dict;

	vector<Carte> v = this->srv.get_all();

	for (auto el : v) {

		if (dict[el.get_tip()] == false) {

			dict[el.get_tip()] = true;
			Clasa_generica* cls = new Clasa_generica(this->srv, el.get_tip());
			cls->show();
		}
	}

}
