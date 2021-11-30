#pragma once

// Acest modul retine modelul tabelului

#include <QAbstractTableModel>
#include <vector>
#include <string>
#include<utility>

#include "Domain.h"

using std::vector;
using std::string;
using std::pair;

// clasa retine un camp si metodele aferente view-ului tabelului nostru
class MyTabelView : public QAbstractTableModel {

private:

	vector<Melodie> lista;

public:

	// constructorul actualizeaza singurul camp al nostru
	MyTabelView(vector<Melodie> l) : lista{ l } {};

	// override la rowCount
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return lista.size();
	}

	// override la columnCount
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 5;
	}

	// override la data
	QVariant data(const QModelIndex& index, int role) const override {
	
		int line = index.row();
		int column = index.column();

		if (role == Qt::DisplayRole) {

			Melodie m = lista.at(line);

			if (column == 0) {	// id

				string id_s = std::to_string(m.get_id());

				return QString::fromStdString(id_s);
			}

			if (column == 1) {	// titlu

				return QString::fromStdString(m.get_titlu());
			}

			if (column == 2) {	// artist

				return QString::fromStdString(m.get_artist());
			}

			if (column == 3) {	// rank

				string rank_s = std::to_string(m.get_rank());

				return QString::fromStdString(rank_s);
			}

			if (column == 4) {

				int ct = 0;
				int rank_curent = m.get_rank();

				for (auto el : lista)

					if (el.get_rank() == rank_curent)

						ct++;

				return QString::fromStdString(std::to_string(ct));
			}
		}
		return QVariant();
	}

	// metoda ce este apelata in cazul in care tabelul sufera modificari
	void setTable(vector<Melodie> v) {

		beginResetModel();

		this->lista = v;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);

		endResetModel();
	}
};