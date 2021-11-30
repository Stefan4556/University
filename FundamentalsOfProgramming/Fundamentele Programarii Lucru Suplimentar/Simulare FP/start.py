"""
    Acesta este ultimul modul cu ajutorul caruia pornim aplicatia
"""

from Domain.domain import teste_domain

from repository import Repository
from repository import teste_repository

from service import Service
from service import test_service

from console import Console

teste_domain()
teste_repository()
test_service()

repo = Repository("simulareFP.txt")
srv = Service(repo)
console = Console(srv)

console.start()