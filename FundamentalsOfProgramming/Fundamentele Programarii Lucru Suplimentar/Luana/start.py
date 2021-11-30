from domain.domain_snake import Snake
from repository.repo_snake import RepoSnake
from service.service_snake import ServiceSnake
from ui.ui_snake import UISnake
import unittest

#unittest.main(module = "testing",exit=False)

repo = RepoSnake("settings.txt")
srv = ServiceSnake(repo)
cons = UISnake(srv)
cons.run()