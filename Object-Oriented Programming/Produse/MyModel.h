#pragma once

// In acest modul este retinut modelul pentru tabelul nostru din GUI

#include <QAbstractTableModel>
#include "Domain.h"
#include <vector>
#include <cstring>
#include <QBrush>

using std::vector;

// Clasa MyTableModel, are ca parametrii privati o lista de produse si un filtru ce este dat de catre slider
class MyTableModel : public QAbstractTableModel {

private:

	vector<Produs> lista;
	int filtru_pret = -1;

public:

	// Constructorul functiei noastre primeste doar lista de produse, filtrul urmand sa fie actualizat doar in anumite situatii
	MyTableModel(vector<Produs> l) : lista{ l } {};

	// Aceasta metoda are scopul de a fi apelata dupa ce se efectueaza o miscare la nivelul slider-ului
	void set_filtru(int filtru_nou) {

		this->filtru_pret = filtru_nou;
	}

	// Aceasta este metoda ce retunreaza numarul de linii din tabelul nostru
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {

		return lista.size();
	}

	// Aceasta este metoda ce retunreaza numarul de coloane din tabelul nostru
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {

		return 5;
	}

	// Aceasta este metoda ce se ocupa cu cererea deatelor de care tabelul nostru are nevoie
	QVariant data(const QModelIndex& index, int role) const override {

		int line = index.row();
		int col = index.column();

		if (role == Qt::DisplayRole) {

			Produs p = this->lista.at(line);

			if (col == 0) {	// id
			
				return QString::fromStdString(std::to_string(p.get_id()));
			}

			if (col == 1) {	// nume

				return QString::fromStdString(p.get_nume());
			}

			if (col == 2) {	// tip

				return QString::fromStdString(p.get_tip());
			}

			if (col == 3) {	// pret

				return QString::fromStdString(std::to_string(p.get_pret()));
			}

			if (col == 4) {	// numar vocale din nume

				string nume = p.get_nume();
				int ct = 0;
				for (int i = 0; i < nume.length(); i++)

					if (nume[i] == 'a' || nume[i] == 'A')

						ct++;

					else if (nume[i] == 'e' || nume[i] == 'E')

						ct++;

					else if (nume[i] == 'i' || nume[i] == 'I')

						ct++;

					else if (nume[i] == 'o' || nume[i] == 'O')

						ct++;

					else if (nume[i] == 'u' || nume[i] == 'U')

						ct++;

				return QString::fromStdString(std::to_string(ct));

			}
		}

		if (role == Qt::BackgroundRole) {

			Produs p = this->lista.at(line);

			if (p.get_pret() <= filtru_pret)

				return QBrush(Qt::red);

			else

				return QBrush(Qt::white);
		}

		return QVariant();
	}

	// Aceasta metoda este apelata doar in cazul in care lista noastra de produse sufera modificari
	void setTable(vector<Produs> l) {

		beginResetModel();

		this->lista = l;
		QModelIndex topLeft = createIndex(0, 0);
		QModelIndex bottomRight = createIndex(rowCount(), columnCount());
		emit dataChanged(topLeft, bottomRight);

		endResetModel();
	}
};