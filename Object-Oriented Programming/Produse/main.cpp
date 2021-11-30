#include "GUI.h"
#include <QtWidgets/QApplication>
#include "Teste.h"

// Acest modul este main-ul, cel ce se ocupa cu rularea testelor si pornirea aplicatiei

int main(int argc, char *argv[]){

    ruleaza_teste();
    Repository repo{ "repository.txt" };
    Validator val;
    Service srv(repo, val);
    QApplication a(argc, argv);
    GUI w(srv);
    w.show();
    return a.exec();
}
