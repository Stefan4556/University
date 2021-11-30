from repository import Repo_spa
from service import Service_spa
from ui import Console

repo = Repo_spa("simulare4.txt")
srv = Service_spa(repo)
cons = Console(srv)
cons.start()