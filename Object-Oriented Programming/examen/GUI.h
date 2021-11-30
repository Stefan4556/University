#pragma once

// Modulul GUI.h se ocupa cu retinerea componentelor interfetei grafice si cu definitiile functiilor noastre

#include <QtWidgets/QWidget>
#include <QTableView>
#include <QVBoxLayout>
#include <QSlider>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QMessageBox>

#include "ui_GUI.h"
#include "Service.h"
#include "TabelModel.h"

// Clasa GUI este singura clasa ce se regaseste in acest modul si are rolul de a gestiona interfata grafica 
//si apelurile functiilor dupa actiunea utilizatorului
class GUI : public QWidget{
    
private:

    Service& srv;

    QTableView* tabel_view;
    MyTableModel* model_tabel;

    QSlider* slider;

    QLabel* id_lab;
    QLineEdit* id_l;
    QLabel* titlu_lab;
    QLineEdit* titlu_l;
    QLabel* tip_lab;
    QLineEdit* tip_l;
    QLabel* pret_lab;
    QLineEdit* pret_l;
    QPushButton* adauga;

    // Metoda initGUI se ocupa cu initializarea componentelor interfetei grafice si adaugarea acestora
    void initGUI();

    // Dupa cum ii spune si numele, aceasta metoda realizeaza legatura dintre actiunile utilizatorului si codul din spatele aplicatiei
    void connectButtons();

    // Functia setInitGUI se ocupa cu gestionarea ferestrelor ce se creeaza pentru cerinta a 4-a
    void setInitGUI();

public:

    // Constructorul clasei GUI, primeste ca si parametru referinta la service si apeleaza cele 3 metode ce se ocupa cu initializarea si rularea aplicatiei
    GUI(Service& srv) : srv{ srv } {

        initGUI();
        connectButtons();
        setInitGUI();
    }
};
