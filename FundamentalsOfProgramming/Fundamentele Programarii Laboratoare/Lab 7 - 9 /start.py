"""
    Modulul ce realizeaza ultimul pas, cel de asamblare finala si pornire a programului
"""

from ui_clase import Consola

from service_clienti import Service_client
from service_carti import Service_carte
from service_inchirieri import Service_inchirieri

from repository_clienti import Repository_clienti
from repository_clienti import Extended_repository_clienti
from repository_carti import Repository_carti
from repository_carti import Extended_repository_carti
from repository_inchirieri import Repository_inchirieri
from repository_inchirieri import Extended_repository_inchirieri

from domain_clienti import Validator_client
from domain_carti import Validator_carte
from domain_inchirieri import Validator_inchiriere

from domain_clienti import Ruleaza_teste_domain_clienti
from domain_carti import Ruleaza_teste_domain_carte
from domain_inchirieri import Ruleaza_teste_domain_inchirieri

from repository_clienti import Teste_repository_clienti
from repository_carti import Teste_repository_carti
from repository_inchirieri import Teste_repository_inchirieri

from service_clienti import Teste_service_clienti
from service_carti import Teste_service_carti
from service_inchirieri import Teste_service_inchirieri
from sortari import Test_sortari

from teste import DomainClientiTestCase
import unittest
from repository_clienti import RepoNouClienti

Ruleaza_teste_domain_clienti()
Ruleaza_teste_domain_carte()
Ruleaza_teste_domain_inchirieri()

Teste_repository_clienti()
Teste_repository_carti()
Teste_repository_inchirieri()

Teste_service_clienti()
Teste_service_carti()
Teste_service_inchirieri()

Test_sortari()

unittest.main(module="teste",exit=False)

#repo_clienti = Repository_clienti()
repo_clienti = Extended_repository_clienti("repository_clienti.txt")
#repo = RepoNouClienti("repo_clienti.txt")
val_clienti = Validator_client()
srv_clienti = Service_client(repo_clienti,val_clienti)
#srv_clienti = Service_client(repo,val_clienti)

#repo_carti = Repository_carti()
repo_carti = Extended_repository_carti("repository_carti.txt")
val_carti = Validator_carte()
srv_carti = Service_carte(repo_carti,val_carti)

#repo_inchirieri = Repository_inchirieri()
repo_inchirieri = Extended_repository_inchirieri("repository_inchirieri.txt")
val_inchirieri = Validator_inchiriere()
srv_inchirieri = Service_inchirieri(repo_inchirieri,val_inchirieri,srv_clienti,srv_carti)

ui = Consola(srv_clienti,srv_carti,srv_inchirieri)
ui.run() 
