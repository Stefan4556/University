#pragma once

//#include <vector>
//#include <algorithm>

#include <vector>
#include <algorithm>

/*
*	Clasa Observer este o clasa pur virtuala ce are o metoda numita update, metoda ce este
*	suprascrisa de fiecare clasa ce mosteneste o suprascrie
*/
class Observer {

public:

	// Aceasta este o metoda pur virtuala
	virtual void update() = 0;

	//virtual ~Observer();
};

/*
*	Clasa observable se ocupa cu retinerea unui vector de obiecte ce mostenesc observer
*		
*	Aceasta contine 3 metode: addObserver, removeObserver si notify
*/
class Observable {

private:

	std::vector<Observer*> observers;

public:

	/*
	*	Aceasta metoda are rolul de a adauga in lista de observers unu observer
	*/
	void addObserver(Observer* obs) {

		observers.push_back(obs);
	}

	/*
	*	Rolul acestei metode este de a sterge din lista de observers un observer trimis ca si parametru
	*/
	void removeObserver(Observer* obs) {

		observers.erase(std::remove(observers.begin(), observers.end(), obs), observers.end());
	}

	/*
	*	Rolul acestei metode este de a se asigura ca ca fiecare observer este actualizat in momentul in care cosul sufera o modificare
	*/
	void notify() {

		for (const auto obs : observers) {

			obs->update();
		}
	}

	//virtual ~Observable();
};
