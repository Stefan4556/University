"""
    In acest modul sunt realizate utltimele importuri si are loc pornirea aplciatiei propriu-zisa
"""

from Domain.domain_word import WordValidator
from Repository.repository_word import Repository
from UI.service_word import SpellCheckerController
from UI.console_word import SpellCheckerUI

from teste import ruleaza_teste

ruleaza_teste()

val = WordValidator()
repo = Repository("dictionar.txt")
srv = SpellCheckerController(repo,val)
cons = SpellCheckerUI(srv)

cons.run()