from repository import Repo_vacante
from service import Service_vacante
from ui import Console
from domain import teste_domain
from repository import teste_repo
from service import teste_service

teste_domain()
teste_repo()
teste_service()

repo = Repo_vacante("vacante.txt")
srv = Service_vacante(repo)
cons = Console(srv)
cons.start()