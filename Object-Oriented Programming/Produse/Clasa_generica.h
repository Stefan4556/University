#pragma once

// In acest modul am definit clasa generica pe care o folosim la cerinta 4

#include <QWidget>
#include <QLabel>
#include "Observer.h"
#include <string>
#include <QVBoxLayout>
#include "Service.h"

// Aceasta clasa retina un QLabel in care e afisat numarul de aparitii al tipului, tipul, referinta catre service si layout-ul acesteia + metodele aferente
class Generic_class : public QWidget, public Observer {

private:

	QLabel* numar_elemente = new QLabel;
	std::string tipul;
	Service& srv;
	QVBoxLayout* lay = new QVBoxLayout;

public:

	// In constructor sunt initializate campurile clasei si este pregatita fereastra
	Generic_class(Service& sr, std::string tip) : srv{ sr }, tipul{ tip }{
	
		srv.addObserver(this);
		setWindowTitle(QString::fromStdString(tipul));
		this->setLayout(lay);
		lay->addWidget(numar_elemente);
		update();
	};

	// Aceasta metoda este mostenita din Observer si trebuie suprascrisa pentru cazul in care lista noastra de produse sufera modificari
	void update() override {

		vector<Produs> v = srv.get_all();

		int ct = 0;

		for (auto el : v)

			if (el.get_tip() == tipul)

				ct++;

		numar_elemente->setText(QString::fromStdString(std::to_string(ct)));
	}
};