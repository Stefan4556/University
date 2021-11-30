#pragma once

#include <QtWidgets/QMainWindow>
#include <QLineEdit>
#include <QLabel>
#include <QListWidget>
#include <QHBoxLayout>
#include <QPushButton>
#include <QFormLayout>
#include <QTextBlock>
#include <QTextEdit>
#include <QMessageBox>
#include <QTableWidget>
#include <QPalette>
#include <QColor>
#include <QTableView>
#include <QListView>
#include <vector>
#include <string>
#include <map>
#include "ui_GUI.h"
#include "Service.h"
#include "Cos.h"
#include "TabelView.h"
#include "ListView.h"

using std::vector;
using std::string;
using std::map;

class GUI : public QWidget{

public:
    
    /*
    *   Aceasta metoda reprezinta constructorul clasei GUI, clasa ce se ocupa cu interfata grafica a aplicatiei
    *   Preconditii: srv-ul primit ca parametru sa fie valid
    *   Param de intrare: srv - Service_filme
    *   Param de iesire: un obiect de tipul GUI
    *   Postconditii: nu avem
    */
    GUI(Service_filme& srv) : srv{ srv } {

        initGUIDesg();
        connectButtons();
        setInitialGUIState();
    }

    /*
    *   Aceasta metoda se ocupa cu actualizarea casetei de tipul QListWidget, caseta in care se afiseaza filmele
    *   Preconditii: lista de filme sa fie valida si nevida
    *   Param de intrare: filme - vector<Film>
    *   Param de iesire: este actualizat QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    //void loadFilmeIntoList(const vector<Film>& filme);

    /*
    *   Aceasta metoda se ocupa cu afisarea filmelor
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void afisare_filme();

    /*
    *   Aceasta metoda se ocupa cu adaugarea unui film in lista si cu actualizarea QListWidget-ului 
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void adauga_film();

    /*
    *   Aceasta metoda se ocupa cu stergerea unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void sterge_film();

    /*
    *   Aceasta metoda se ocupa cu cautarea unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void cauta_film();

    /*
    *   Aceasta metoda se ocupa cu modificarea titlului unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void modifica_titlu_film();

    /*
    *   Aceasta metoda se ocupa cu modificarea genului unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void modifica_gen_film();

    /*
    *   Aceasta metoda se ocupa cu modificarea anului unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void modifica_an_film();

    /*
    *   Aceasta metoda se ocupa cu modificarea actorului unui film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void modifica_actor_film();

    /*
    *   Aceasta metoda se ocupa cu realizarea undo-ului
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void undo_film();

    /*
    *   Aceasta metoda se ocupa cu filtrarea filmelor dupa titlu
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void filterbytitle();

    /*
    *   Aceasta metoda se ocupa cu filtrarea filmelor dupa an
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void filterbyan();

    /*
    *   Cerinta lab trecut cu dictionar
    */
    void raport_filme();

    /*
    *   Aceasta metoda se ocupa cu adaugarea unui film in cos
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza cosul
    *   Postconditii: nu avem
    */
    void adauga_film_cos();

    /*
    *   Aceasta metoda se ocupa cu adaugarea mai multor filme random in cos
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza cosul
    *   Postconditii: nu avem
    */
    void adauga_film_cos_random();

    /*
    *   Aceasta metoda se ocupa cu golirea cosului din film
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza cosul
    *   Postconditii: nu avem
    */
    void goleste_cos();

    /*
    *   Aceasta metoda se ocupa cu afisarea filmelor din cos
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se afiseaza pe ecran filmele din cos
    *   Postconditii: nu avem
    */
    void afiseaza_filme_cos();

    /*
    *   Aceasta metoda se ocupa cu exportul filmelor din cos intr-un fisier introdus de utilizator
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se afiseaza pe ecran filmele din cos
    *   Postconditii: nu avem
    */
    void exporta_cos();

    /*
    *   Aceasta metoda se ocupa cu sortarea dupa titluri a filmelor
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void sortare_filme_titlu();

    /*
    *   Aceasta metoda se ocupa cu sortarea dupa actor a filmelor
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void sortare_filme_actor();

    /*
    *   Aceasta metoda se ocupa cu sortarea dupa an si gen a filmelor
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: se actualizeaza QListWidget-ul
    *   Postconditii: sa se observe aceste lucru la nivelul aplicatiei
    */
    void sortare_filme_an_gen();

    /*
    *   Cerinta lab
    */
    void afisare_filme_tabel();

    /*
    *   Aceasta metoda se ocupa cu afisarea obiectului selectat
    */
    void afisare_obiect_selectat();

    /*
    *   Rolul acestei metode este de a lega codul de butonul ce porneste fereastra in
    *   care se afiseaza cosul de filme
    */
    void CosCRUDGUI_functie();

    /*
    *   Rolul acestei metode este de a lega codul de butonul ce porneste fereastra in 
    *   care se deseneaza
    */
    void CosReadOnlyGUI_functie();

private:

    Service_filme& srv;

    /*
    *   Aceasta metoda se ocupa cu initializarea butoanelor si realizarea interfetei grafice
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: interfata grafica
    *   Postconditii: nu avem
    */
    void initGUIDesg();

    /*
    *   Aceasta metoda se ocupa cu conectarea butoanelor de metodele din spate
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: nu avem
    *   Postconditii: sa fie realizate legaturile cu succes
    */
    void connectButtons();

    /*
    *   Aceasta metoda se ocupa cu initializarea obiectului de tipul QListWidget
    *   Preconditii: nu avem
    *   Param de intrare: nu avem
    *   Param de iesire: nu avem
    *   Postconditii: nu avem
    */
    void setInitialGUIState();

    QListWidget* lista_filme; 

    QPushButton* sortare_actor;
    QPushButton* sortare_titlu;
    QPushButton* sortare_an_gen;
    QPushButton* filtru_an;
    QPushButton* filtru_titlu;
    QPushButton* raport;
    QPushButton* exit;     

    QPushButton* adauga;   
    QPushButton* sterge;  
    QPushButton* cauta;
    QPushButton* undo;
    QPushButton* modifica_titlu;
    QPushButton* modifica_gen;
    QPushButton* modifica_an;
    QPushButton* modifica_actor;
    QPushButton* afiseaza;  
    QPushButton* afiseaza_tabel;
    QPushButton* adauga_cos;    
    QPushButton* genereaza_cos;
    QPushButton* export_fis;
    QPushButton* golire_cos;
    QPushButton* afisare_cos;
    QPushButton* CosCRUDGUI;
    QPushButton* CosReadOnlyGUI;

    QLineEdit* txtID;
    QLineEdit* txtTITLU;
    QLineEdit* txtGEN;
    QLineEdit* txtAN;
    QLineEdit* txtACTOR;

    QLineEdit* txtNUMAR;
    QLineEdit* txtTITLU_COS;
    QLineEdit* txtFISIER;

    QTableView* table_view;
    MyTableModel* table_model;

    QListView* list_view;
    MyListModel* list_model;
};
