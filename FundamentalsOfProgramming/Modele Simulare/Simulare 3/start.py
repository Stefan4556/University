from domain import Validator_arta
from repository import Repo_arta
from service import Service_arta
from ui import Console
from domain import teste_domain
from repository import teste_repo
from service import teste_service

teste_domain()
teste_repo()
teste_service()

repo = Repo_arta("simulare3.txt")
val = Validator_arta()
serv = Service_arta(repo,val)
cons = Console(serv)
cons.run()