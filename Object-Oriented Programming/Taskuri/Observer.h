#pragma once

#include <algorithm>
#include <vector>

using std::vector;

// obiectele ce au o metoda update sunt urmarite de un observer
class Observer {

public:

	// emtoda ce asteapta sa fie suprascrisa
	virtual void update() = 0;
};

// metoda ce se ocupa cu gestiunea observerilor
class Observable {

private:

	vector<Observer*> observers;

public:

	// adauga un observer
	void addObserver(Observer* obs) {

		observers.push_back(obs);
	}

	// sterge un oberserver
	void removeObserver(Observer* obs) {

		observers.erase(std::remove(observers.begin(), observers.end(), obs), observers.end());
	}

	// apeleaza metoda ce se ocupa cu update ul lor
	void notify() {

		for (const auto obs : observers)

			obs->update();
	}
};