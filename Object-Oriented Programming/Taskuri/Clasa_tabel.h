#pragma once
#include "Service.h"
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QVBoxLayout>

// Clasa pentru tabelul din aplicatia mare
class Tabel : public QWidget, public Observer {

private:

	Service& srv;
	QTableWidget* tabel;
	QVBoxLayout* lay;
	bool update_filtru = false;
	string filtru = "";

	// initializam componenetele aceste clase
	void initGUI();

	// dupa cum ii spune si numele, incarcam elemnte in tabel
	void load_items_into_table();

public:

	// constructorul clasei initializeaza clasa si legaturile
	Tabel(Service& srv) : srv{ srv } {

		srv.addObserver(this);
		initGUI();
	}

	// metoda ce se ocupa cu un update mai special
	void set_update_filtru(string fil) {

		update_filtru = true;
		filtru = fil;
	}

	// metoda suprascrisa ce e apelata cand lista are modificari
	void update() override;
};