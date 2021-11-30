#include "GUI.h"

void GUI::initGUI(){

	QVBoxLayout* lay = new QVBoxLayout;
	this->setLayout(lay);

	desen_sus = new Deseneaza(this->srv, "sus");
	lay->addWidget(desen_sus);

	tabel_normal = new QTableWidget;
	lay->addWidget(tabel_normal);
	
	tabel_view = new QTableView;
	model_tabel = new MyTableModel(this->srv.get_all());
	tabel_view->setModel(model_tabel);
	lay->addWidget(tabel_view);

	titlu = new QLabel("Titlu");
	lay->addWidget(titlu);
	titlu_l = new QLineEdit;
	lay->addWidget(titlu_l);

	artist = new QLabel("Artist");
	lay->addWidget(artist);
	artist_l = new QLineEdit;
	lay->addWidget(artist_l);

	gen = new QLabel("Gen");
	lay->addWidget(gen);
	gen_l = new QLineEdit;
	lay->addWidget(gen_l);

	adauga = new QPushButton("Adauga");
	lay->addWidget(adauga);

	sterge = new QPushButton("Sterge");
	lay->addWidget(sterge);

	desen_jos = new Deseneaza(this->srv, "jos");
	lay->addWidget(desen_jos);
}

void GUI::connectButtons(){

	QObject::connect(adauga, &QPushButton::clicked, this, [this]() {

		int id = rand() % 10000 + 20;

		auto titlu = titlu_l->text().toStdString();
		auto artist = artist_l->text().toStdString();
		auto gen = gen_l->text().toStdString();
		titlu_l->clear();
		artist_l->clear();
		gen_l->clear();

		this->srv.adauga_melodie(id, titlu, artist, gen);
		load_into_table(this->srv.sortare_autor());
		model_tabel->setTable(this->srv.get_all());
		desen_sus->repaint();
		desen_jos->repaint();
	});

	QObject::connect(tabel_view->selectionModel(), &QItemSelectionModel::selectionChanged, this, [this]() {

		if (tabel_view->selectionModel()->selectedIndexes().isEmpty())

			return;

		auto ind = tabel_view->selectionModel()->selectedIndexes().at(0).row();
		auto cel0 = tabel_view->model()->index(ind, 0);
		auto id = tabel_view->model()->data(cel0, Qt::DisplayRole).toInt();
		this->id_sterge = id;
	});

	QObject::connect(sterge, &QPushButton::clicked, this, [this]() {

		this->srv.sterge_melodie(this->id_sterge);
		id_sterge = 0;
		load_into_table(this->srv.sortare_autor());
		model_tabel->setTable(this->srv.get_all());
		desen_sus->repaint();
		desen_jos->repaint();
	});
}

void GUI::setInitGUI(){

	load_into_table(this->srv.sortare_autor());
}

void GUI::load_into_table(vector<Melodie> v){

	tabel_normal->setColumnCount(4);
	tabel_normal->setRowCount(v.size());

	int i = 0;

	for (auto el : v) {

		string id_s = std::to_string(el.get_id());

		QTableWidgetItem* it1 = new QTableWidgetItem(QString::fromStdString(id_s));

		tabel_normal->setItem(i, 0, it1);

		QTableWidgetItem* it2 = new QTableWidgetItem(QString::fromStdString(el.get_titlu()));

		tabel_normal->setItem(i, 1, it2);

		QTableWidgetItem* it3 = new QTableWidgetItem(QString::fromStdString(el.get_artist()));

		tabel_normal->setItem(i, 2, it3);

		QTableWidgetItem* it4 = new QTableWidgetItem(QString::fromStdString(el.get_gen()));

		tabel_normal->setItem(i, 3, it4);

		i++;
	}
}
