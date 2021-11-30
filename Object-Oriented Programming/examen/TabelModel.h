#pragma once

// Acest modul se ocupa cu retinerea clasei MyTableModel ce reprezinta modelul tabelului din aplicatiei

#include <QAbstractTableModel>
#include "Domain.h"
#include <vector>
#include <QBrush>

using std::vector;

// Clasa MyTableModel, are 2 campuri private si anume lista de carti si un filtru ce se aplica mereu si este modificat de catre slider
class MyTableModel : public QAbstractTableModel {

private:

	vector<Carte> lista;
	int filtru = 0;

public:

	// Constructorul clasei primeste o lista cu carti pentru a incarca elementele pe care le solicita utilizatorul
	MyTableModel(vector<Carte> l) : lista{ l } {};

	// Metoda set_filtru, dupa cum spuneam si mai devreme, seteaza filtrul ce este aplicat mereu
	void set_filtru(int filtru_nou) {

		filtru = filtru_nou;
	}

	// Aceasta este prima metoda ce trebuie suprascrisa pentru a putea realiza modelul tabelului nostru, aceasta ocupandu-se cu returnarea numarului
	// de linii ale tabelului
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return lista.size();
	}

	// Aceasta este cea de-a doua metoda pe care trebuie sa o suprascriem, aceasta ocupandu-se cu returnarea numarului de coloane ale tabelului
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 5;
	}

	// Metoda data este ultima metoda ce trebuie suprascrisa si se ocupa cu incarcarea elementelor cerute de catre utlizator in modelul nostru
	// pentru a fi afisate ulterior in tabel
	QVariant data(const QModelIndex& index, int role) const override{

		int line = index.row();
		int col = index.column();

		if (role == Qt::DisplayRole) {

			Carte c = lista.at(line);

			if (col == 0) // id

				return QString::fromStdString(std::to_string(c.get_id()));

			if (col == 1) // titlu

				return QString::fromStdString(c.get_titlu());

			if (col == 2)	// tip

				return QString::fromStdString(c.get_tip());

			if (col == 3)	// pret

				return QString::fromStdString(std::to_string(c.get_pret()));

			if (col == 4)	// nr litere titlu

				return QString::fromStdString(std::to_string(c.get_titlu().size()));
		}

		if (role == Qt::BackgroundRole) {

			Carte c = lista.at(line);

			if (c.get_pret() <= filtru)

				return QBrush(Qt::red);

			else

				return QBrush(Qt::white);

		}

		return QVariant();
	}

	// Metoda setTable este apelata in momentul in care lista noastra de carti sufera modificari si reincarca elementele in tabel, aceasta primind
	// ca si parametru, lista noua de carti
	void setTabel(vector<Carte> v) {

		beginResetModel();

		this->lista = v;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);

		endResetModel();
	}
};