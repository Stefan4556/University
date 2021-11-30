
// Acesta este modulul principal ce se ocupa cu apelarea testelor si pornirea aplicatiei

#include "GUI.h"
#include <QtWidgets/QApplication>
#include "Teste.h"

int main(int argc, char *argv[])
{
    ruleaza_teste();
    Repository repo{ "repository.txt" };
    Validator val;
    Service srv(repo, val);
    QApplication a(argc, argv);
    GUI w(srv);
    w.show();
    return a.exec();
}
