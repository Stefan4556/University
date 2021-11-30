#pragma once

#include "Observer.h"
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QListWidget>
#include <string>
#include <QWidget>
#include "Service.h"

using std::string;

// Aceasta reprezinta sablonul pentru feresterele de la cerinta 4
class Generic_class : public Observer, public QWidget {

private:

	Service& srv;

	QPushButton* open;
	QPushButton* inprogress;
	QPushButton* close;
	QVBoxLayout* lay;
	QListWidget* lista;
	string stare;
	int id_modifica = -1;

	// metoda ce initializeaza GUI
	void initGUI();

	// Metoda ce conecteaza cele 3 butoane de pe ferastra cu codul
	void connectButtons();

	// Metoda ce initializeaza fereastra
	void setInitStateGUI();

public:

	// Aceasta metoda este cosntructorul ce initializeaza campurile clasei
	Generic_class(Service& srv, string stare) : srv{ srv }, stare { stare } {

		this->setWindowTitle(QString::fromStdString(stare));
		srv.addObserver(this);
		initGUI();
		connectButtons();
		setInitStateGUI();
	}

	// aceasta este metoda ce este apelata cand lista de taskuri are modificari
	void update() override;

	// dupa cum ii spune si numele, metoda updateaza lista de taskuri cu starea respectiva
	void load_items_into_list(vector<Task> v);
};