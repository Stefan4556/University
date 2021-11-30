#pragma once

// In acest modul este definita clasa ce se ocupa cu desenerea cercurilor in colturile aplicatiei

#include <QWidget>
#include "Service.h"
#include <QPainter>
#include <QHBoxLayout>
#include <qDebug>

// Rolul acestei clase este de a creea un obiect ce se gestioneaza cercurile din coltul aplicatiei
class Deseneaza : public QWidget {

private:

	Service& srv;

	int x = 10;
	int y = 10;

	string ok = "sus"; // suntem in partea de sus

	// pop - st sus
	// rock - dr sus
	// folk - st jos
	// disco - dr sus

public:

	// Constructorul clasei noastre primeste ca si parametru service-ul pentru a putea urmari activ schimbarile ce se pot efectua la nivelul acestuia
	// si un parametru ok care este egal cu sus sau jos, ce spune daca ne aflam in partea de sus sau jos
	Deseneaza(Service& srv, string ok) : srv{ srv }, ok{ ok } {

		QHBoxLayout* l = new QHBoxLayout;
		this->setFixedSize(280, 60);
		this->setLayout(l);
	};

	// suprascriem metoda paintEvent pentru a putea desena in unul dintre cele 4 colturi cand lista noastra sufera modificari
	void paintEvent(QPaintEvent* event) override {

		qDebug() << "sunt in painter";

		QPainter painter{ this };

		QPoint centru1 = QPoint(x + 15, y + 20);
		QPoint centru2 = QPoint(x + 240, y + 20);

		if (ok == "sus") {

			int ct_pop = 0, ct_rock = 0;

			for (auto el : this->srv.get_all())

				if (el.get_gen() == "pop")

					ct_pop++;

				else if (el.get_gen() == "rock")

					ct_rock++;

			int r = 5;
			painter.drawEllipse(centru1, 5, 5);
			r += 5;

			for (int i = 0; i < ct_pop; i++) {

				painter.drawEllipse(centru1, r, r);
				r += 5;
			}

			r = 5;
			painter.drawEllipse(centru2, 5, 5);
			r += 5;

			for (int i = 0; i < ct_rock; i++) {

				painter.drawEllipse(centru2, r, r);
				r += 5;
			}
			
		}
		else {

			int ct_folk = 0, ct_disco = 0;

			for (auto el : this->srv.get_all())

				if (el.get_gen() == "folk")

					ct_folk++;

				else if (el.get_gen() == "disco")

					ct_disco++;

			int r = 5;
			painter.drawEllipse(centru1, 5, 5);
			r += 5;

			for (int i = 0; i < ct_folk; i++) {

				painter.drawEllipse(centru1, r, r);
				r += 5;
			}

			r = 5;
			painter.drawEllipse(centru2, 5, 5);
			r += 5;

			for (int i = 0; i < ct_disco; i++) {

				painter.drawEllipse(centru2, r, r);
				r += 5;
			}

		}

	}
};