#pragma once

template<typename ElementType>
class IteratorDynamicArray;

template<typename ElementType>
class DynamicArray {

private:

	int capacity, dimens;
	ElementType* elems;

public:

	/*
	*	Acesta reprezinta default constructorul pentru vectorul dinamic in care se initializeaza cele 3 campuri ale acestei clase
	*	Preconditii: nu avem
	*	Param de intrare: nu avem
	*	Param de iesire: un vector dinamic initializat
	*	Postconditii: vectorul sa fie initializat
	*/
	DynamicArray() noexcept {	// default constructor

		this->capacity = 2;
		this->dimens = 0;
		this->elems = new ElementType[this->capacity];
	}

	/*
	*	Acesta reprezinta copy constructor ul pentru vectorul dinamic in care se initializeaza cele 3 campuri ale acestei clase cu valorile altui vector dinamic
	*	Preconditii: d sa fie valid
	*	Param de intrare: d - vector dinamic
	*	Param de iesire: nu avem
	*	Postconditii: sa fie copiat cu succes
	*/
	DynamicArray(const DynamicArray<ElementType>& d) {	// copy constructor

		this->capacity = d.capacity;
		this->dimens = d.dimens;
		this->elems = new ElementType[this->capacity];
		for (int i = 0; i < this->dimens; i++)
			this->elems[i] = d.elems[i];
	}

	/*
	*	Aceasta este metoda ce redefineste operatorul = 
	*	Preconditii: ot sa fie valid
	*	Param de intrare: ot - vector dinamic
	*	Param de iesire: operatorul din stanga este actualizat cu cel din dreapta
	*	Postconditii: nu avem
	*/
	DynamicArray<ElementType>& operator=(const DynamicArray<ElementType>& ot) {	// assignment operator

		if (this == &ot)

			return *this;

		delete[] this->elems;
		this->elems = new ElementType[ot.capacity];
		for (int i = 0; i < ot.dimens; i++)
			this->elems[i] = ot.elems[i];

		this->capacity = ot.capacity;
		this->dimens = ot.dimens;
		return *this;
	}

	/*
	*	Aceasta este metoda ce distruge vectorul dinamic
	*	Preconditii: sa existe parametrul implicit, vectorul
	*	Param de intrare: parametru implicit, vectorul
	*	Param de iesire: nu avem
	*	Postconditii: memoria sa fie eliberata cu succes
	*/
	~DynamicArray() {	// destructor

		delete[] elems;
	}

	/*
	*	Aceasta este metoda ce returneaza marimea vectorului dinamic
	*	Preconditii: sa fie valid vectorul dinamic si creeat
	*	Param de intrare: parametru implicit, vector dinamic
	*	Param de iesire: dimensiune - int 
	*	Postconditii: dimenisunea returnata sa fie >= 0
	*/
	int size() const {

		return this->dimens;
	}

	/*
	*	Aceasta este metoda ce returneaza obiectul ce se afla pe pozitia i in vectorul dinamic
	*	Preconditii: indexul sa fie valid
	*	Param de intrare: index - int
	*	Param de iesire: elementul ce se afla la pozitia respectiva
	*	Postconditii: nu avem
	*/
	ElementType& at(int index) {

		return this->elems[index];
	}

	/*
	*	Aceasta este metoda ce returneaza obiectul ce se afla pe pozitia i in vectorul dinamic
	*	Preconditii: indexul sa fie valid
	*	Param de intrare: index - int
	*	Param de iesire: elementul ce se afla la pozitia respectiva
	*	Postconditii: nu avem
	*/
	const ElementType& at(int index) const {

		return this->elems[index];
	}

	/*
	*	Aceasta este metoda ce adauga la finalul vectorului dinamic un element
	*	Preconditii: f sa fie valid
	*	Param de intrare: f- ElementType
	*	Param de iesire: nu avem
	*	Postconditii: la finalul listei sa fie adaugat elementul primit ca si parametru
	*/
	void push_back(ElementType f) {

		if (this->dimens == this->capacity) {	// verif daca avem destul spatiu alocat

			int new_capacity = 2 * this->capacity;
			ElementType* new_elems = new ElementType[new_capacity];
			for (int i = 0; i < this->dimens; i++) {

				new_elems[i] = this->elems[i];
			}
			delete[] this->elems;
			this->elems = new_elems;
			this->capacity = new_capacity;
		}

		this->elems[this->dimens] = f;
		this->dimens++;
	}

	/*
	*	Aceasta este metoda ce sterge un element aflat pe pozitia i
	*	Preconditii: indexul sa fie valid
	*	Param de intrare: index - int
	*	Param de iesire: nu avem
	*	Postconditii: elementul sa fie sters cu succes
	*/
	void erase(int index) {

		for (int i = index; i < this->dimens - 1; i++)

			this->elems[i] = this->elems[i + 1];

		this->dimens--;

	}

	friend class IteratorDynamicArray<ElementType>;
	IteratorDynamicArray<ElementType> begin();
	IteratorDynamicArray<ElementType> end();
};

template<typename ElementType>
IteratorDynamicArray<ElementType> DynamicArray<ElementType>::begin() {

	return IteratorDynamicArray<ElementType>(*this);
}

template<typename ElementType>
IteratorDynamicArray<ElementType> DynamicArray<ElementType>::end() {

	return IteratorDynamicArray<ElementType>(*this, dimens);
}

/////////// Iterator Dynamic Array
template<typename ElementType>
class IteratorDynamicArray {

private:

	const DynamicArray<ElementType>& v;
	int poz = 0;

public:

	IteratorDynamicArray(const DynamicArray<ElementType>& v) noexcept;
	IteratorDynamicArray(const DynamicArray<ElementType>& v, int poz)noexcept;
	bool valid() const;
	ElementType& element() const;
	void next();
	ElementType& operator*();
	IteratorDynamicArray& operator++();
	bool operator==(const IteratorDynamicArray& ot)noexcept;
	bool operator!=(const IteratorDynamicArray& ot)noexcept;

};

template<typename ElementType>
IteratorDynamicArray<ElementType>::IteratorDynamicArray(const DynamicArray<ElementType>& v) noexcept :v{ v } {}

template<typename ElementType>
IteratorDynamicArray<ElementType>::IteratorDynamicArray(const DynamicArray<ElementType>& v, int poz)noexcept : v{ v }, poz{ poz } {}

template<typename ElementType>
bool IteratorDynamicArray<ElementType>::valid()const {

	return poz < v.dimens;
}

template<typename ElementType>
ElementType& IteratorDynamicArray<ElementType>::element() const {

	return v.elems[poz];
}

template<typename ElementType>
void IteratorDynamicArray<ElementType>::next() {

	poz++;
}

template<typename ElementType>
ElementType& IteratorDynamicArray<ElementType>::operator*() {

	return element();
}

template<typename ElementType>
IteratorDynamicArray<ElementType>& IteratorDynamicArray<ElementType>::operator++() {

	next();
	return *this;
}

template<typename ElementType>
bool IteratorDynamicArray<ElementType>::operator==(const IteratorDynamicArray<ElementType>& ot) noexcept {

	return poz == ot.poz;
}

template<typename ElementType>
bool IteratorDynamicArray<ElementType>::operator!=(const IteratorDynamicArray<ElementType>& ot) noexcept {

	return !(*this == ot);
}
