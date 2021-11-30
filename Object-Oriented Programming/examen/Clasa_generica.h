#pragma once

// Modulul Clasa_generica.h se ocupa cu retinerea clasei Clasa_generica ce se ocupa cu initalizarea si formarea unei ferestre corespunzatoare cerintei
// de la punctul 4

#include "Observer.h"
#include "Service.h"
#include <QWidget>
#include <QVBoxLayout>
#include <QListWidget>

// Clasa_generica are ca scop realizarea ferestrei cerute la cerinta a 4-a si mosteneste din Observer, pentru a putea fi actualizata in cazul in care
// lista de carti sufera vreo modificare si din QWidget pentru a o putea-o trata ca pe un widget
class Clasa_generica : public Observer, public QWidget{

private:

	string nume;
	Service& srv;

	QVBoxLayout* lay;
	QListWidget* lista;
	
	// Dupa cum ii spune si numele, metoda initGUI, initializeaza componentele unei clase generice, de la titlul ferestrei pana la widgeturile de pe aceasta
	void initGUI();

	// Aceasta metoda incarca elementele corespunzatoare numelui clasei intr-un QListWidget
	void setInitState();

public:

	// Constructorul Clasei generice primeste ca si parametru referinta la service, pentru a avaea acces la lista de carti si un nume, acela reprezentand
	// de fapt, tipul corespunzator acestei clase
	Clasa_generica(Service& srv, string nume) : srv{ srv }, nume{ nume }{

		initGUI();
		setInitState();
	};

	// Metoda update este mostenita din observer si este apelata automat in momentul in care lista de carti sufera vreo modificare, ea ocupandu-se
	// cu actualizarea listei de carti corespunzatoare tipului nostru
	void update() override;

	// Functia load_items_into_lista, incarca elementele corespunzatoare tipului nostru primit ca si parametru in QListWidget-ul nostru
	void load_items_into_lista();
};