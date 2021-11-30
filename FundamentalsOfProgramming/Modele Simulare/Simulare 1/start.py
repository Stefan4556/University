from domain import Validator_movie
from repository import MovieRepository
from service import MovieControler
from ui import MoviesUI

repo = MovieRepository("simulare1.txt")
val = Validator_movie()
srv = MovieControler(repo,val)
UI = MoviesUI(srv)
UI.showUI()
