#include "GUI.h"
#include <QtWidgets/QApplication>
#include "Teste.h"
#include "Service.h"

int main(int argc, char *argv[])
{

    ruleaza_teste();

    Repository_carti repo("repository.txt");
    Service_carti srv(repo);

    QApplication a(argc, argv);
    GUI w(srv);
    w.show();
    return a.exec();
}
