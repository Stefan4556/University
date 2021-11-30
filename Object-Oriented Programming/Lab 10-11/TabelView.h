#pragma once

#include <QAbstractTableModel>
#include <QDebug>
#include "Service.h"

class MyTableModel : public QAbstractTableModel {

private:

	vector<Film> v;

public:

	MyTableModel(vector<Film> v) : v{ v } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return v.size();
	}

	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 5;
	}

	QVariant data(const QModelIndex& index, int role) const override {

		int row = index.row();
		int column = index.column();
		qDebug() << "row: " << index.row() << " col: " << index.column();
		if (role == Qt::DisplayRole) {

			Film f = v.at(row);
			string id_s = std::to_string(f.get_id());
			string an_s = std::to_string(f.get_an_aparitie());


			if (column == 0)

				return QString::fromStdString(id_s);

			else if (column == 1)

				return QString::fromStdString(f.get_titlu());

			else if (column == 2)

				return QString::fromStdString(f.get_gen());

			else if (column == 3)

				return QString::fromStdString(an_s);

			else if (column == 4)

				return QString::fromStdString(f.get_actor_principal());

		}

		return QVariant();
	}

	void setFilme(vector<Film> filme) {	// daca vrem sa se actualizeze si tabelul cand e fereastra deschisa trb sa actualizam modelul la fiecare mod

		beginResetModel();
		this->v = filme;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);
		endResetModel();
	}
};