#pragma once

#include <QAbstractListModel>
#include "Service.h"

class MyListModel : public QAbstractListModel {

private:

	vector<Film> v;

public:

	MyListModel(vector<Film> v) : v{ v } {};

	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return v.size();
	}

	QVariant data(const QModelIndex& index, int role) const override {

		if (role == Qt::DisplayRole) {

			Film f = v.at(index.row());
			string id_s = std::to_string(f.get_id());
			string an_s = std::to_string(f.get_an_aparitie());
			auto text = QString::fromStdString("Id: " + id_s + " Titlu: " + f.get_titlu() + " Gen: " + f.get_gen() + " An: " + an_s + " Actor: " + f.get_actor_principal());

			return QString(text);
		}

		return QVariant();
	}

	void setFilme(const vector<Film>& v1) {
		
		this->v = v1;
		auto topLeft = createIndex(0, 0);
		auto bottomR = createIndex(rowCount(), 1);
		emit dataChanged(topLeft, bottomR);
	}
};