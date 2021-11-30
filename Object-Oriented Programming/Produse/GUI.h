#pragma once

// Rolul acestei metode este de a initializa componentele interfetei grafice si de a le lega de codul din spate

#include <QtWidgets/QWidget>
#include <QTableView>
#include <QVBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>

#include "ui_GUI.h"
#include "Service.h"
#include "MyModel.h"

// Clasa GUI, are ca si campuri private elementele interfetei grafice si legatura catre Service + alte metode aferente
class GUI : public QWidget{

private:

	Service& srv;

	QTableView* tabel_view;
	MyTableModel* model_tabel;

	QLabel* id;
	QLineEdit* id_l;
	QLabel* nume;
	QLineEdit* nume_l;
	QLabel* tip;
	QLineEdit* tip_l;
	QLabel* pret;
	QLineEdit* pret_l;
	QPushButton* adauga;

	QSlider* slider;

	// Rolul acestei metode este de a initializa si combina toate elementele interfetei grafice
	void initGUI();

	// Dupa cum ii spune si numele, aceasta metoda conecteaza butoanele de codul din spate
	void connectButtons();

	// Aceasta metoda deschide in alte ferestre acele window-uri ce contorizeaza numarul de apariii al fiecarui tip
	void setInitGUI();

public:

	// Rolul acestei metode este de a realiza legatura dintre GUI si service si a apela functiile definite mai sus, pe scurt, initializeaza si porneste aplicatia
	GUI(Service& srv) : srv{ srv } {

		initGUI();
		connectButtons();
		setInitGUI();
	};
};
