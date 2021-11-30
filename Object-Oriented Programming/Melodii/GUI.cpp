#include "GUI.h"

void GUI::initGUI(){

	QVBoxLayout* lay_vertical = new QVBoxLayout;
	this->setLayout(lay_vertical);
	
	tabel_normal = new QTableWidget;
	lay_vertical->addWidget(tabel_normal);

	tabel_view = new QTableView;
	model_tabel = new MyTabelView(this->srv.get_all());
	tabel_view->setModel(model_tabel);
	lay_vertical->addWidget(tabel_view);

	casuta_titlu = new QLineEdit;
	lay_vertical->addWidget(casuta_titlu);
	slider = new QSlider;
	slider->setOrientation(Qt::Horizontal);
	slider->setMinimum(0);
	slider->setMaximum(10);
	lay_vertical->addWidget(slider);
	modifica = new QPushButton("Modifica");
	lay_vertical->addWidget(modifica);
	sterge = new QPushButton("Sterge");
	lay_vertical->addWidget(sterge);

	zona_desen = new Deseneaza(this->srv);
	lay_vertical->addWidget(zona_desen);
}

void GUI::connectButtons(){

	QObject::connect(tabel_view->selectionModel(), &QItemSelectionModel::selectionChanged, this, [this]() {

		if (tabel_view->selectionModel()->selectedIndexes().isEmpty())

			return;

		auto ind = tabel_view->selectionModel()->selectedIndexes().at(0).row();
		auto titlu = tabel_view->model()->index(ind, 1);
		auto id = tabel_view->model()->index(ind, 0);
		auto cel0 = tabel_view->model()->data(id, Qt::DisplayRole).toString();
		auto cel1 = tabel_view->model()->data(titlu, Qt::DisplayRole).toString();
		this->casuta_titlu->setText(cel1);
		this->id_modifica = cel0.toInt();
	});

	QObject::connect(slider, &QSlider::valueChanged, this, [this]() {

		int val = slider->value();
		this->rank_nou = val;
	});

	QObject::connect(modifica, &QPushButton::clicked, this, [this]() {

		auto titlu = casuta_titlu->text();
		casuta_titlu->clear();
		string titlu_s = titlu.toStdString();

		this->srv.modifica_titlu_rank(id_modifica, titlu_s, rank_nou);
		id_modifica = -1;
		rank_nou = 0;
		load_into_normal_table(this->srv.sortare_rank());
		model_tabel->setTable(this->srv.get_all());
		zona_desen->repaint();
	});

	QObject::connect(sterge, &QPushButton::clicked, this, [this]() {

		auto titlu = casuta_titlu->text();
		casuta_titlu->clear();
		id_modifica = -1;
		rank_nou = 0;

		try {
			this->srv.sterge_melodie(titlu.toStdString());
			load_into_normal_table(this->srv.sortare_rank());
			model_tabel->setTable(this->srv.get_all());
			zona_desen->repaint();
		}
		catch (std::exception) {

			QMessageBox::warning(nullptr, "Eroare la stergere", "Aceasta este ultima melodie a artistului si nu poate fi stearsa!");
		}
	});
}

void GUI::setGUI(){

	load_into_normal_table(this->srv.sortare_rank());
}

void GUI::load_into_normal_table(vector<Melodie> v){

	int i = 0;
	this->tabel_normal->setColumnCount(4);
	this->tabel_normal->setRowCount(v.size());

	for (auto el : v) {

		string id_s = std::to_string(el.get_id());
		string rank_s = std::to_string(el.get_rank());

		QTableWidgetItem* item1 = new QTableWidgetItem(QString::fromStdString(id_s));
		this->tabel_normal->setItem(i, 0, item1);

		QTableWidgetItem* item2 = new QTableWidgetItem(QString::fromStdString(el.get_titlu()));
		this->tabel_normal->setItem(i, 1, item2);

		QTableWidgetItem* item3 = new QTableWidgetItem(QString::fromStdString(el.get_artist()));
		this->tabel_normal->setItem(i, 2, item3);

		QTableWidgetItem* item4 = new QTableWidgetItem(QString::fromStdString(rank_s));
		this->tabel_normal->setItem(i, 3, item4);

		i++;
	}
}
