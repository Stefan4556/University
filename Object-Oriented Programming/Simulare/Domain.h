#pragma once

#include <string>

using std::string;

class Carte {

private:

	string titlu;
	string autor;
	string culoare;
	int grosime;

public:

	Carte(string titlu, string autor, string culoare, int grosime) : titlu{ titlu }, autor{ autor }, culoare{ culoare }, grosime{ grosime }{

	};

	string get_titlu();

	string get_autor();

	string get_culoare();

	int get_grosime();
};