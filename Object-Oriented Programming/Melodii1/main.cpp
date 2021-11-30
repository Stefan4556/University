#include "GUI.h"
#include <QtWidgets/QApplication>
#include "Teste.h"

int main(int argc, char *argv[])
{
    ruleaza_teste();    // rulam testele pentru a ne asigura ca am acoperit toate cazurile in care programul poate esua

    Repository repo{ "repository.txt" };
    Service srv(repo);

    QApplication a(argc, argv);
    GUI w(srv);
    w.show();
    return a.exec();
}
