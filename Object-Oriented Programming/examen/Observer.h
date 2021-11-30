#pragma once

// Acest modul se ocupa cu retinerea a 2 clase, Observer ce se comporta ca obiectul ce asteapta sa primeasca un semnal ca sa se actualizeze si clasa\
// Observable, ce are o lista de observeri pe care o gestioneaza si trimite semnalul catre acestia in cazul in care lista de carti sufera modificari

#include <vector>
#include <algorithm>

using std::vector;

// Clasa Observer, are o singura metoda virtuala ce asteapta sa fie suprascrisa
class Observer {

public:

	// metoda update, este o metoda virtuala ce asteapta sa fie suprascrisa de catre clasele ce o sa mosteneasca din aceasta
	virtual void update() = 0;
};

// Clasa Observable, se ocupa cu retinerea, gestiunea si notificarea observerilor
class Observable {

private:

	vector<Observer*> observeri;

public:

	// Metoda addObserver, are rolul de a adauga in lista de observeri, un observer primit ca si parametru
	void addObserver(Observer* obs) {

		observeri.push_back(obs);
	}

	// Functia removeObserver, se ocupa cu stergerea unui observer din lista de observeri, acesta fiind primit ca si parametru
	void removeObserver(Observer* obs) {

		observeri.erase(std::remove(observeri.begin(), observeri.end(), obs), observeri.end());
	}

	// Dupa cum ii spune si numele, metoda notify trimite un semnal catre toate clasele ce au mostenit din Observer, pentru a semnala faptul ca 
	// lista noastra de carti a suferit modificari
	void notify() {

		for (auto obs : observeri)

			obs->update();
	}
};