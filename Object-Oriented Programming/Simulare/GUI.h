#pragma once

#include "ui_GUI.h"
#include <QTableWidget>
#include <QLineEdit>
#include <QPushButton>
#include "Service.h"
#include <QVBoxLayout>

class GUI : public QWidget
{
private:

	Service_carti& srv;

	QTableWidget* tabel;
	QLineEdit* culoare;
	QPushButton* sortare_grosime;
	QPushButton* sortare_titlu;
	QPushButton* nesortat;

	void initGuiDesign();
	void connectButtons();
	void initApp();

public:

	GUI(Service_carti& srv) : srv{ srv } {
	
		initGuiDesign();
		connectButtons();
		initApp();
	};


};
