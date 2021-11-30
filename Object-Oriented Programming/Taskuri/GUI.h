#pragma once

#include <QtWidgets/QWidget>
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QVBoxLayout>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>

#include "ui_GUI.h"
#include "Service.h"
#include "Clasa_tabel.h"

// clasa gui se ocupa cu realizarea interfetei grafice
class GUI : public QWidget{
    
private:

    Service& srv;

    //QTableWidget* tabel;
    Tabel* tabel;

    QLabel* id_lab;
    QLineEdit* id_l;
    QLabel* descriere_lab;
    QLineEdit* descriere_l;
    QLabel* programatori_lab;
    QLineEdit* programatori_l;
    QLabel* stare_lab;
    QLineEdit* stare_l;
    QPushButton* adauga;

    QLabel* search;
    QLineEdit* nume_search;

    // aceasta metoda initializeaza componentele clasei tabel
    void initGUI();

    // aceasta metoda se ocupa cu conectarea butoanelor de codul din spate
    void connectButtons();

    // aceasta metoda initializeaza aplicatia inainte de a porni o
    void initStateGui();

    //void load_items_into_table(vector<Task> v);

public:

    // constructorul clasei ce apeleaza cele 3 metode pentru a porni aplicatia cu succes
    GUI(Service& srv) : srv{ srv } {

        initGUI();
        connectButtons();
        initStateGui();
    }
};
