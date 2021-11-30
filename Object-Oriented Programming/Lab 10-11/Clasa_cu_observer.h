#pragma once

#include <QWidget>
#include <QListWidget>
#include <QPushButton>
#include <QLineEdit>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QFormLayout>
#include <QLabel>
#include <QPaintEvent>
#include <QPainter>
#include "Cos.h"
#include "Observer.h"

/*
*	Aceasta reprezinta clasa CosCRUDGUI_Window ce mosteneste din QWidget si Observer
*/
class CosCRUDGUI_Window : public QWidget, public Observer {

private:

	Cos& cos_filme;
	QListWidget* lista_cos;
	QPushButton* buton_golire;
	QPushButton* buton_generare;
	QLineEdit* input_generare;
	
	/*
	*	Rolul acestei metode este de a incarca filmele dintr un vector primit ca si parametru
	*	in obiectul QListWidget
	*/
	void loadIntoList(std::vector<Film>& v) {

		lista_cos->clear();
		for (auto& f : v)
			lista_cos->addItem(QString::fromStdString(f.get_titlu()));
	}

	/*
	*	Rolul acestei metode este de a initializa interfata grafica a aplicatiei si obiectele
	*	ce apartin acestei clase
	*/
	void initGUI() {

		QVBoxLayout* V_Lay = new QVBoxLayout;

		this->setLayout(V_Lay);

		lista_cos = new QListWidget;

		V_Lay->addWidget(lista_cos);

		QFormLayout* text = new QFormLayout;
		QLabel* inp_gen = new QLabel("Genereaza");
		input_generare = new QLineEdit;
		text->addRow(inp_gen, input_generare);

		V_Lay->addLayout(text);

		QHBoxLayout* H_Lay = new QHBoxLayout;
		buton_generare = new QPushButton("Genereaza filme");
		buton_golire = new QPushButton("Goleste cosul");
		H_Lay->addWidget(buton_golire);
		H_Lay->addWidget(buton_generare);

		V_Lay->addLayout(H_Lay);

	}

	/*
	*	Rolul acestei clase este de a lega interfata grafica de partea din spate de cod
	*/
	void connectButtons() {

		cos_filme.addObserver(this);

		QObject::connect(buton_generare, &QPushButton::clicked, [&]() {

			QString inp = input_generare->text();
			cos_filme.genereaza_cos(inp.toInt());
			input_generare->clear();
		});

		QObject::connect(buton_golire, &QPushButton::clicked, [&]() {

			cos_filme.goleste_cos();
			loadIntoList(cos_filme.get_cos());
		});
	}
	
public:
	
	/*
	*	Aceasta este constructorul clasei ce primeste ca si parametru referinta la cos
	*	si apeleaza metodele ce initalizeaza interfata grafica, leaga butoanele si initializeaza aplicatia
	*/
	CosCRUDGUI_Window(Cos& cos) : cos_filme{ cos } {

		initGUI();
		connectButtons();
		loadIntoList(cos_filme.get_cos());
	};

	/*
	*	Aceasta este metoda suprascrisa pentru ca este mostenita din clasa Observer
	*/
	void update() override {

		loadIntoList(cos_filme.get_cos());
	}

	// Constructorul clasei Observer
	~CosCRUDGUI_Window() {

		cos_filme.removeObserver(this);
	}
};

/*
*	Aceasta reprezinta clasa CosReadOnlyGUI_Window ce mosteneste din QWidget si Observer
*/
class CosReadOnlyGUI_Window : public QWidget, public Observer {

private:

	Cos& cos_filme;

public:

	/*
	*	Acesta este constructorul acestei clase ce primeste ca si parametru referinta la cos
	*	si adauga acest obiect in lista de observers
	*/
	CosReadOnlyGUI_Window(Cos& cos) : cos_filme{ cos } {

		cos_filme.addObserver(this);
	};

	// Aceasta este metoda ce se ocupa cu redesenarea in aceasta fereastra
	void update() override {

		repaint();// trb apelat paint ul
	}

	// suprascriem metoda paintEvent pentru a desena ceea ce dorim noi
	void paintEvent(QPaintEvent* ev) override {

		QPainter p{ this };

		int x = 10;
		int y = 10;

		for (const auto& f : cos_filme.get_cos()) {

			//p.drawRect(x, 100, 20, 10);
			int xx = rand() % x;
			int yy = rand() % y;
			p.drawImage(xx, yy, QImage("icon3.png"));
			x += 100;
			y += 100;
		}

		//p.drawLine(0, 0, 5, 5);
	}
};