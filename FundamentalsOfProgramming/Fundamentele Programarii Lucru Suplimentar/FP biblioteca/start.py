"""
    Acest modul reprezinta modulul final, modul in care sunt realizate importurile si este pornita aplicatia
"""

from domain import ValdiatorCarte
from service import Service
from repository_carti import Repository
from console import Console
from lista_globala import lista_undo

from domain import teste_domain
from repository_carti import teste_repo
from service import teste_service
import unittest

""" lista_undo = []
teste_domain()

lista_undo = []
teste_repo()

lista_undo = []
teste_service() """

unittest.main(module="teste",exit=False)

lista_undo = []
val = ValdiatorCarte()
repo = Repository("biblioteca.txt")
srv = Service(repo,val)
cons = Console(srv)
cons.run()