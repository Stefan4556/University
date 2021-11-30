#pragma once

// clasa ce se ocupa cu retinerea interfetei grafice

#include <QtWidgets/QWidget>
#include <QTableWidget>
#include <QTableView>
#include <QVBoxLayout>
#include <QLineEdit>
#include <QSlider>
#include <QPushButton>
#include <QMessageBox>
#include <QLabel>

#include "ui_GUI.h"
#include "Service.h"
#include "TabelView.h"
#include "Desen.h"

// clasa GUI are mai multe campuri private ce consta in elemente ce apartin interfetei grafice si metodele aferente acestora
class GUI : public QWidget{

private:

	Service& srv;
	QTableWidget* tabel_normal;
	QTableView* tabel_view;
	MyTabelView* model_tabel;

	QLineEdit* casuta_titlu;
	QSlider* slider;
	QPushButton* modifica;
	QPushButton* sterge;

	Deseneaza* zona_desen;

	int id_modifica = -1;
	int rank_nou = 0;

	// Rolul acestei metode este de a initializa componenetele interfetei grafice
	void initGUI();

	// Rolul acestei metode este de a conecta butoanele de functiile din spate
	void connectButtons();

	// Rolul acestei metode este de a initializa prima interfata grafica - starea initiala
	void setGUI();

public:

	// constructorul clasei GUI ce initializeaza aplciatia
	GUI(Service& srv1) : srv{ srv1 } {
	
		initGUI();
		connectButtons();
		setGUI();
	};
   
	// metoda ce incarca elementele in lista de melodii
	void load_into_normal_table(vector<Melodie> v);

};
