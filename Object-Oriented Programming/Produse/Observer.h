#pragma once

// Acest modul retine 2 clase, Observer ce reprezinta obiectele ce sunt urmarite si Observable cel care declanseaza toate update-urile

#include <vector>

// Clasa Observer este o clasa pur virtuala ce are o metoda ce asteapta sa fie suprascrisa
class Observer {

public:

	// Metoda update este pur virtual, urmand sa fie suprascrisa
	virtual void update() = 0;
};

// Clasa Observable, cum spuneam si mai devreme, este cea care retine lista de observi si o gestioneaza, inclusiv declanseaza update-ul acestora
class Observable {

private:

	std::vector<Observer*> observers;

public:

	// Aceasta metoda adauga un observer in lista de observeri
	void addObserver(Observer* obs) {

		observers.push_back(obs);
	}

	// Metoda removeObserver se ocupa cu stergerea unui observer, primit ca parametru, din lista de observeri
	void removeObserver(Observer* obs) {

		observers.erase(std::remove(observers.begin(), observers.end(), obs), observers.end());
	}
	
	// Aceasta este metoda ce declanseaza update-ul tuturor observerilor, si e apelata cand lista sufera o modificare
	void notify() {

		for (const auto obs : observers)

			obs->update();
	}
};