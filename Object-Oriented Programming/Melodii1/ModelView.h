#pragma once

// In acest modul este prezenta clasa ce se ocupa cu creearea modelului pentru tabelul nostru de tipul QTableView

#include <QAbstractTableModel>
#include "Domain.h"
#include <vector>

using std::vector;

// Clasa dupa cum ii spune numele, reprezinta modelul tabelului si suprascrie 3 metode din QAbstracTableModel si mai retine inca o metoda auxiliara

class MyTableModel : public QAbstractTableModel {

private:

	vector<Melodie> lista;

public:

	// Constructorul clasei noastre primeste un vector de melodii ce ii furnizeaza datele suficiente modelului nostru
	MyTableModel(vector<Melodie> s) : lista{ s } {};

	// Aceasta este prima metoda suprascrisa pentru a putea creea un model pentru tabel - numar randuri
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return lista.size();
	}

	// Aceasta este a 2-a metoda suprascrisa pentru a putea creea un model pentru tabel - numar coloane
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 6;
	}

	// Aceasta este a 3-a metoda suprascrisa pentru a putea creea un model pentru tabel - data, ce se ocupa cu cererea datelor
	QVariant data(const QModelIndex& index, int role) const override {

		int line = index.row();
		int col = index.column();

		if (role == Qt::DisplayRole) {

			Melodie m = this->lista.at(line);

			if (col == 0) { // id

				return QString::fromStdString(std::to_string(m.get_id()));
			}

			if (col == 1) { // titlu

				return QString::fromStdString(m.get_titlu());
			}

			if (col == 2) {	// artist

				return QString::fromStdString(m.get_artist());
			}

			if (col == 3) {	// gen

				return QString::fromStdString(m.get_gen());
			}

			if (col == 4) {	// care au acelasi autor

				int ct = 0;
				string autor = m.get_artist();

				for (auto el : this->lista)

					if (el.get_artist() == autor)

						ct++;

				return QString::fromStdString(std::to_string(ct));
			}

			if (col == 5) {	// care au acelasi gen

				int ct = 0;
				string gen = m.get_gen();

				for (auto el : this->lista)

					if (el.get_gen() == gen)

						ct++;

				return QString::fromStdString(std::to_string(ct));
			}
		}
		return QVariant();
	}

	// Aceasta metoda este apelata in momentul in care, lista noastra de melodii sufera modificari
	void setTable(vector<Melodie> v) {

		beginResetModel();

		this->lista = v;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);

		endResetModel();
	}
};