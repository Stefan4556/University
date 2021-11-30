"""
    Acesta este modulul ce realizeaza importurile celorlalte module si pornirea efectiva a aplicatiei
"""

from repository.repository import Repository
from service.service import Service
from console.console import Console

repo = Repository("produse.txt")
srv = Service(repo)
cons = Console(srv)
cons.start()