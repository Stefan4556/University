from domain.domain import Bicicleta

from repository.repository import Repository,RepositoryException

from service.service import Service

# teste pentru domain
def teste_domain():

    b = Bicicleta(1,"bmx",500.5)
    assert b.getId() == 1
    assert b.getPret() == 500.5
    assert b.getTip() == "bmx"

# teste pentru repository
def teste_repository():

    try:
        f = open("produse_test.txt","w")
    except IOError:
        pass
    
    f.write("100, road, 400.5\n200, road, 400\n300, mountain, 500\n400, bmx, 500\n")
    f.close()
    
    repo = Repository("produse_test.txt")

    l = repo.getAll()
    assert len(l) == 4

    assert repo.cauta_id(100) == 0
    assert repo.cauta_id(1000) == None

    repo.delete(100)
    l = repo.getAll()
    assert len(l) == 3

    assert repo.pret_maxim() == 500
    repo.sterge_biciclete_pret_maxim()
    l = repo.getAll()
    assert len(l) == 1

    try:
        repo.sterge_tip("bicicleta")
        assert False
    except RepositoryException:
        assert True
    
    repo.sterge_tip("road")
    l = repo.getAll()
    assert len(l) == 0
 
# teste pentru service
def teste_service():

    try:
        f = open("produse_test.txt","w")
    except IOError:
        pass
    
    f.write("100, road, 400.5\n200, road, 400\n300, mountain, 500\n400, bmx, 500\n")
    f.close()
    
    repo = Repository("produse_test.txt")
    
    srv = Service(repo)

    l = srv.afisare_bicicelte()
    assert len(l) == 4

    srv.stergere_max()
    l = srv.afisare_bicicelte()
    assert len(l) == 2

    try:
        srv.stergere_tip("dada")
        assert False
    except RepositoryException:
        assert True
    
    srv.stergere_tip("road")
    l = srv.afisare_bicicelte()
    assert len(l) == 0

def ruleaza_teste():

    teste_domain()
    teste_repository()
    teste_service()

ruleaza_teste()