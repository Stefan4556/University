#pragma once

// Rolul acestui modul este de a retine reprezentarea GUI

#include <QtWidgets/QWidget>
#include "ui_GUI.h"
#include "Service.h"
#include "ModelView.h"
#include "Deseneaza.h"

#include <QTableWidget>
#include <QVBoxLayout>
#include <QTableView>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>

// Clasa GUI se ocupa cu retinerea componentelor interfetei grafice si cu metodele aferente acestora
class GUI : public QWidget{

private:

	Service& srv;
	QTableWidget* tabel_normal;

	QTableView* tabel_view;
	MyTableModel* model_tabel;

	QLabel* titlu;
	QLineEdit* titlu_l;
	QLabel* artist;
	QLineEdit* artist_l;
	QLabel* gen;
	QLineEdit* gen_l;
	QPushButton* adauga;

	QPushButton* sterge;
	int id_sterge = -1;

	Deseneaza* desen_jos;
	Deseneaza* desen_sus;

	// Rolul acestei metode este de a creea elementele interfetei grafice si de a le lega
	void initGUI();

	// Dupa cum spune si numele functiei, aceasta are scopul de a lega butoanele de functiile din spate
	void connectButtons();

	// Aceasta metoda este apelata la inceputul aplicatiei cu scopul de a initializa tabelul aplicatiei
	void setInitGUI();

public:

	// Constructorul clasei noastre primeste referinta la Service si apeleaza ulterior cele 3 functii ce se ocupa de interfata grafica
	GUI(Service& sr) : srv{ sr } {
		
		initGUI();
		connectButtons();
		setInitGUI();
	};

	// Aceasta este metoda ce o apeleaza setInitGUI, cea care incarca elementele primite ca si parametru in vector in tabelul nostru
	void load_into_table(vector<Melodie> v);
};
