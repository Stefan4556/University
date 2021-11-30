#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include "Cos.h"
#include "Repo_lab.h"
#include "GUI.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	//Repository_filme repo;	// varianta fara fisiere
	Repository_filme_file repo("C:/Users/stefa/source/repos/Lab 10-11/Lab 10-11/repository.txt");	// varianta cu fisiere
	//RepoLab repo(0.0001);		// varianta cu probabilitate 
	Validator valid;
	Cos cos(repo);
	Service_filme srv(repo, valid, cos);
	ruleaza_teste();
    QApplication a(argc, argv);
	a.setWindowIcon(QIcon("icon.png"));
    GUI w(srv);
    w.show();
    return a.exec();
}
