#pragma once

#include "Domain.h"
#include <vector>
#include <QAbstractTableModel>

using std::vector;

class MyTableModel : public QAbstractTableModel {

private:

	vector<Joc> lista;

public:

	MyTableModel(vector<Joc> l) : lista{ l } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return lista.size();
	}

	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 5;
	}

	QVariant data(const QModelIndex& index, int role) const override {

		int line = index.row();
		int col = index.column();

		if (role == Qt::DisplayRole) {

			Joc j = this->lista.at(line);

			if (col == 0)

				return QString::fromStdString(std::to_string(j.get_id()));

			if (col == 1)

				return QString::fromStdString(std::to_string(j.get_dim()));

			if (col == 2)

				return QString::fromStdString(j.get_tabla());

			if (col == 3)

				return QString::fromStdString(j.get_jucator());

			if (col == 4)

				return QString::fromStdString(j.get_stare());
		}

		return QVariant();
	}

	void setTabel(vector<Joc> v) {

		beginResetModel();

		this->lista = v;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());

		endResetModel();
	}
};