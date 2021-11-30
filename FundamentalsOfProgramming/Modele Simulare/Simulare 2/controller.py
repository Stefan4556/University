from domain import Validator_bicicleta_exception,Bicicleta,ValidatorBicicleta
from repository import Repository

class Controlller():
    """
        Clasa ce realizeaza legatura dintre ui, repo si domain
    """

    def __init__(self,val,rep):
        """
            Realziam legaturile propriu-zise
        """

        self.__val = val
        self.__repo = rep
    
    def getAll(self):
        """
            aceasta metoda comunica cu repo si are rolul de a aduce in ui lista de biciclete
        """

        return self.__repo.get_all()
    
    def delete_tip(self,tip):
        """
            aceasta metoda comunica cu repo si are rolul de sterge din lista toate bicicletele de un anumit tip
        """

        self.__repo.delete_tip(tip)
    
    def delete_max(self):
        """
            aceasta metoda comunica cu repo si are rolul de sterge din lista toate bicicletele cu pretul maxim
        """

        self.__repo.delete_max()
    
    def delete_by_id(self,id):
        """
            aceasta metoda comunica cu repo si are rolul de sterge din lista bicicleta cu id-ul dat
        """

        self.__val.valideaza_bicicleta(Bicicleta(id,"bmx",100))
        self.__repo.delete(id)
    
def test_controler():

    f = open("test2.txt","w")
    f.write("1, bmx, 501.1 \n")
    f.write("2, mountain, 455 \n")
    f.write("3, cross, 456 \n")
    f.close()
    repo = Repository("test2.txt")
    val = ValidatorBicicleta()
    srv = Controlller(val,repo)
    l = srv.getAll()
    assert len(l) == 3
    srv.delete_tip("cross")
    assert len(srv.getAll()) == 2
    srv.delete_max()
    assert len(srv.getAll()) == 1
    srv.delete_by_id(2)
    assert len(srv.getAll()) == 0
    try:
        srv.delete_by_id(-1)
        assert False
    except Validator_bicicleta_exception:
        assert True

test_controler()


