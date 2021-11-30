#include "GUI.h"

void GUI::initGUI(){

	lay = new QVBoxLayout;
	this->setLayout(lay);

	tabel_view = new QTableView;
	model_tabel = new MyTableModel(srv.sortare_stare());
	tabel_view->setModel(model_tabel);
	lay->addWidget(tabel_view);

	dim_lab = new QLabel("Dimensiune");
	lay->addWidget(dim_lab);
	dim_l = new QLineEdit;
	lay->addWidget(dim_l);
	tabla_lab = new QLabel("Tabla");
	lay->addWidget(tabla_lab);
	tabla_l = new QLineEdit;
	lay->addWidget(tabla_l);
	jucator_lab = new QLabel("Jucator");
	lay->addWidget(jucator_lab);
	jucator_l = new QLineEdit;
	lay->addWidget(jucator_l);
	
	stare_lab = new QLabel("Stare");
	lay->addWidget(stare_lab);
	stare_l = new QLineEdit;
	lay->addWidget(stare_l);
	
	adauga = new QPushButton("Adauga");
	lay->addWidget(adauga);

	modifica = new QPushButton("Modifica");
	lay->addWidget(modifica);

	butoane_multe = new QWidget;
	lay->addWidget(butoane_multe);
}

void GUI::connectButtons(){

	QObject::connect(adauga, &QPushButton::clicked, this, [this]() {

		auto dim = dim_l->text().toInt();
		auto tabla = tabla_l->text().toStdString();
		auto jucator = jucator_l->text().toStdString();
		dim_l->clear();
		tabla_l->clear();
		jucator_l->clear();
		try {

			this->srv.adauga_joc(dim, tabla, jucator);
			model_tabel->setTabel(this->srv.sortare_stare());
		}
		catch (const string& err) {

			QMessageBox::warning(nullptr, "Eroare", QString::fromStdString(err));
		}
	});

	QObject::connect(tabel_view->selectionModel(), &QItemSelectionModel::selectionChanged, this, [this]() {

		auto var = tabel_view->selectionModel()->selectedIndexes();

		if (var.isEmpty())

			return;

		auto ind = var.at(0).row();
		auto cel0 = tabel_view->model()->index(ind, 0);
		auto id = tabel_view->model()->data(cel0, Qt::DisplayRole).toInt();

		id_modifica = id;
		modifica_butoane_widget();
	});

	QObject::connect(modifica, &QPushButton::clicked, this, [this]() {
			
		auto dim = dim_l->text().toInt();
		auto tabla = tabla_l->text().toStdString();
		auto jucator = jucator_l->text().toStdString();
		auto stare = stare_l->text().toStdString();
		dim_l->clear();
		tabla_l->clear();
		jucator_l->clear();
		stare_l->clear();

		try {

			this->srv.modifica_joc(id_modifica, dim, tabla, jucator, stare);
			model_tabel->setTabel(this->srv.sortare_stare());
		}
		catch (const string& err) {

			QMessageBox::warning(nullptr, "Eroare", QString::fromStdString(err));
		}
	});
	
}

void GUI::modifica_butoane_widget(){

	lay->removeWidget(butoane_multe);
	delete butoane_multe;
	butoane_multe = new QWidget;
	lay->addWidget(butoane_multe);
	Joc j = this->srv.get_item_by_id(id_modifica);
	QVBoxLayout* lay_vertical = new QVBoxLayout;
	butoane_multe->setLayout(lay_vertical);
	int dim = j.get_dim();	// dim mat
	string tabla = j.get_tabla();

	for (int i = 0; i < dim; i++) {

		QHBoxLayout* lay_oriz = new QHBoxLayout;

		for (int l = 0; l < dim; l++) {

			QPushButton* but = new QPushButton(QString(tabla[i * dim + l]));
			int poz = i * dim + l;
			QObject::connect(but, &QPushButton::clicked, this, [=]() {

				Joc j = this->srv.get_item_by_id(id_modifica);

				if (but->text() != "-")

					return;

				string juc = j.get_jucator();

				string tabla = j.get_tabla();

				tabla[poz] = juc.c_str()[0];

				string juc_nou;

				if (juc == "X")

					juc_nou = "O";

				else

					juc_nou = "X";

				this->srv.modifica_joc(id_modifica, j.get_dim(), tabla, juc_nou, j.get_stare());
				but->setText(QString::fromStdString(juc));
				model_tabel->setTabel(this->srv.sortare_stare());
			});
			lay_oriz->addWidget(but);
		}
		lay_vertical->addLayout(lay_oriz);
	}
}