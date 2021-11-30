#pragma once

#include <QtWidgets/QWidget>
#include <QTableView>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QLineEdit>
#include <QLabel>
#include <QPushButton>
#include <QMessageBox>
#include "ui_GUI.h"
#include "Service.h"
#include "TabelModel.h"

class GUI : public QWidget{

private:

	Service& srv;

	QVBoxLayout* lay;

	QTableView* tabel_view;
	MyTableModel* model_tabel;

	QLabel* dim_lab;
	QLineEdit* dim_l;
	QLabel* tabla_lab;
	QLineEdit* tabla_l;
	QLabel* jucator_lab;
	QLineEdit* jucator_l;
	QPushButton* adauga;

	QLabel* stare_lab;
	QLineEdit* stare_l;
	QPushButton* modifica;
	int id_modifica = -1;

	QWidget* butoane_multe;

	void initGUI();
	void connectButtons();

public:

	GUI(Service& srv) : srv{ srv } {

		initGUI();
		connectButtons();
	}

	void modifica_butoane_widget();

};
