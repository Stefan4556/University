from domain import Validator
from repository import Repo_muzica
from service import Service_muzica
from console import Console

from domain import teste_domain
from repository import teste_repo
from service import teste_service

teste_domain()
teste_repo()
teste_service()

val = Validator()
repo = Repo_muzica("simulare5.txt")
srv = Service_muzica(repo,val)
cons = Console(srv)
cons.start()