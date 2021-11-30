#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>
#include <iostream>
#include "Teste.h"
#include "Domain.h"
#include "Repository.h"
#include "Service.h"
#include "Ui.h"
#include "Cos.h"
#include "Repo_lab.h"

int main() {
	{
		Repository_filme repo;	// varianta fara fisiere
		//Repository_filme_file repo("C:/Users/stefan/source/repos/Lab 6-7/Lab 6-7/repository.txt");	// varianta cu fisiere
		//RepoLab repo(0.0001);		// varianta cu probabilitate 
		Validator valid;
		Cos cos;
		Service_filme srv(repo, valid, cos);
		Console cons(srv);

		//ruleaza_teste();
		cons.run();
	}
	_CrtDumpMemoryLeaks();

	return 0;
}