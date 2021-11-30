#pragma once

#include <QWidget>
#include <QPainter>
#include "Service.h"
#include <qDebug>
#include <QVBoxLayout>

class Deseneaza : public QWidget {

private:

	int y_init = 10;	// sa plece toate de pe aceeasi linie
	Service& srv;

public:

	Deseneaza(Service& s) : srv{ s } {
	
		this->setFixedSize(150, 60);
		QVBoxLayout* v = new QVBoxLayout;
		this->setLayout(v);
	};

	void paintEvent(QPaintEvent* event) override {

		vector<Melodie> v = srv.get_all();

		QPainter painter{ this };

		int x = 0;
		
		for (int rank = 0; rank <= 10; rank++) {

			int ct_curent = 0;

			for (auto el : v)

				if (el.get_rank() == rank)	// determinam inaltimea dreptunghiului

					ct_curent++;

			painter.drawRect(x, 59 - ct_curent * 10, 5, ct_curent * 10);
			x += 10;
		}
		qDebug() << "sunt in paint\n";
	}
};