import unittest
from domain_clienti import Client, Validator_client, Validator_client_exception
from domain_carti import Carte, Validator_carte, Validator_carti_exception
from domain_inchirieri import Inchiriere, Validator_inchiriere, Validator_inchirieri_exception

from repository_clienti import Repository_clienti, Exception_Repository_Clienti, Extended_repository_clienti
from repository_carti import Repository_carti, Exception_Repository_Carti, Extended_repository_carti
from repository_inchirieri import Repository_inchirieri, Exception_Repository_Inchirieri, Extended_repository_inchirieri

from service_clienti import Service_client,Exception_service_client
from service_carti import Service_carte,Exception_service_carte
from service_inchirieri import Service_inchirieri,Exception_service_inchirieri

class DomainClientiTestCase(unittest.TestCase):

    def setUp(self):

        self.val = Validator_client()
        self.__client = Client(1, "Dumitru George", 1234567891234)
    
    def tearDown(self):
        
        pass
    
    def test_creare_client(self):

        self.assertEqual(self.__client.getId_client(), 1)
        self.assertEqual(self.__client.getNume(), "Dumitru George")
        self.assertEqual(self.__client.getCnp(), 1234567891234)
        self.assertNotEqual(self.__client.getCnp, 1)
    
    def test_modificare_client(self):

        self.__client.setNume("Haiduc")
        self.assertEqual(self.__client.getNume(),"Haiduc")
        self.__client.setCnp(2131231231131)
        self.assertEqual(self.__client.getCnp(),2131231231131)
    
    def test_valideaza_client(self):

        self.assertIsNone(self.val.valideaza_client(self.__client))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(-1,"Stefan Farcasanu",1234567891234))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(1,"Stefan Farcasanu",123))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(1,"",0))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(1,"",1234567891234))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(-1,"Stefan Farcasanu", 1))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(-1,"123",1234567891234))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(-1,"1a2b",1234567891234))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(-1,"Stefan Farcasanu", -1))
        self.assertRaises(Validator_client_exception,self.val.valideaza_client,Client(20,"Stefan Farcasanu", -123))

class RepositoryClientiTestCase(unittest.TestCase):

    def setUp(self):

        #self.__repo = Repository_clienti()
        self.file = open("repository_clienti_teste.txt","r")
        self.__repo = Extended_repository_clienti("repository_clienti_teste.txt")
        self.__repo.salveaza_client(Client(1,"Stefan",1231231231231))
        self.__repo.salveaza_client(Client(2,"Mihai Eminescu",1234567891234))
    
    def tearDown(self):

        self.file.close()
        self.file = open("repository_clienti_teste.txt","w")
        self.file.write("")
        self.file.close()

    def test_write_to_file_and_store_to_file(self):

        self.file.close()
        self.file = open("repository_clienti_teste.txt","w")
        self.file.write("1,Stefan,1231231231231,\n2,Bogdan,1231231231237\n")
        self.assertEqual(len(self.__repo.afisare_clienti()),2)
        self.assertEqual(self.__repo.cauta_client(1),"Id: 1, Nume: Stefan, CNP: 1231231231231")
        self.__repo.modifica_client_nume(1,"Popa")
        self.assertEqual(self.__repo.cauta_client(1),"Id: 1, Nume: Popa, CNP: 1231231231231")
        self.__repo.salveaza_client(Client(4,"Hei",1111111111111))
        self.assertEqual(len(self.__repo.afisare_clienti()),3)
        self.assertEqual(self.__repo.cauta_client(4),"Id: 4, Nume: Hei, CNP: 1111111111111")

    def test_salveaza_client(self):
        
        self.assertTrue(len(self.__repo.afisare_clienti()) == 2)
        self.__repo.salveaza_client(Client(3,"Popica", 1234567891235))
        self.assertTrue(len(self.__repo.afisare_clienti()) == 3)
        self.assertRaises(Exception_Repository_Clienti,self.__repo.salveaza_client,Client(2,"Dumitru Chirpici", 5234567891234))
        self.assertRaises(Exception_Repository_Clienti,self.__repo.salveaza_client,Client(3,"Dumitru Chirpici", 5234567891234))
        self.__repo.salveaza_client(Client(4,"Dumitru Chirpici", 5234567891234))
        self.assertTrue(len(self.__repo.afisare_clienti()) == 4)
    
    def test_cauta_client_dupa_id(self):

        self.assertIsNone(self.__repo.cauta_client(0))
        self.assertEqual(self.__repo.cauta_client(1),"Id: 1, Nume: Stefan, CNP: 1231231231231")
        self.assertEqual(self.__repo.cauta_client(2),"Id: 2, Nume: Mihai Eminescu, CNP: 1234567891234")
        self.assertIsNone(self.__repo.cauta_client(10))
    
    def test_stergere_client_id(self):

        self.__repo.salveaza_client(Client(3,"Hello",4444444444444))
        self.assertTrue(len(self.__repo.afisare_clienti()) == 3)
        self.__repo.sterge_client_id(3)
        self.assertTrue(len(self.__repo.afisare_clienti()) == 2)
        self.assertRaises(Exception_Repository_Clienti,self.__repo.sterge_client_id,555)
        self.assertRaises(Exception_Repository_Clienti,self.__repo.sterge_client_id,-1)
    
    def test_modifica_client_nume(self):

        self.__repo.salveaza_client(Client(10,"Modifica",2222222222222))
        self.__repo.cauta_client_id_modifica(10,"Popel")
        self.assertEqual(self.__repo.cauta_client(10),"Id: 10, Nume: Popel, CNP: 2222222222222")
        #self.__repo.stergere_client_id(10) - in cazul in care punem cei 2 clienti din setup in fisier
        self.assertRaises(Exception_Repository_Clienti,self.__repo.cauta_client_id_modifica,101,"HG")
        self.assertRaises(Exception_Repository_Clienti,self.__repo.cauta_client_id_modifica,-101,"HG")
    
    def test_returneaza_obiect_id(self):

        self.assertIsNotNone(self.__repo.returneaza_obiect_client(1))
        self.assertIsNotNone(self.__repo.returneaza_obiect_client(2))
        self.assertIsNone(self.__repo.returneaza_obiect_client(888))
        self.assertIsNone(self.__repo.returneaza_obiect_client(555))
    
    def test_cauta_client_id_gasit(self):

        self.assertRaises(Exception_Repository_Clienti,self.__repo.cauta_client_id_gasit,777)
        self.assertIsNotNone(self.__repo.cauta_client_id_gasit(1))
        self.assertIsNotNone(self.__repo.cauta_client_id_gasit(2))
        self.assertRaises(Exception_Repository_Clienti,self.__repo.cauta_client_id_gasit,15)
        self.assertRaises(Exception_Repository_Clienti,self.__repo.cauta_client_id_gasit,-15)

class ServiceClientiTestCase(unittest.TestCase):

    def setUp(self):

        val = Validator_client()
        self.file = open("repository_clienti_teste.txt","r")
        repo = Extended_repository_clienti("repository_clienti_teste.txt")
        self.__srv = Service_client(repo,val)
    
    def tearDown(self):

        self.file.close()
        self.file = open("repository_clienti_teste.txt","w")
        self.file.write("")
        self.file.close()
    
    def test_adauga_client(self):

        self.__srv.adauga_client(1,"Stefan",1231231231231)
        l = self.__srv.afiseaza()
        self.assertTrue(len(l) == 1)
        self.__srv.adauga_client(2,"Popa",1231231231232)
        l = self.__srv.afiseaza()
        self.assertTrue(len(l) == 2)
        self.assertRaises(Exception_Repository_Clienti,self.__srv.adauga_client,1,"Bogdan",1111111111111)
        self.assertRaises(Validator_client_exception,self.__srv.adauga_client,3,"Bogdan",111111111111)
    
    def test_cauta(self):

        self.__srv.adauga_client(1,"Stefan",1231231231231)
        self.assertEqual(self.__srv.cauta(1),"Id: 1, Nume: Stefan, CNP: 1231231231231")
        self.assertIsNone(self.__srv.cauta(2))
        self.assertRaises(Validator_client_exception,self.__srv.cauta,-1)
        self.assertRaises(Validator_client_exception,self.__srv.cauta,1000)
    
    def test_stergere(self):

        self.__srv.adauga_client(1,"Stefan",1231231231231)
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.__srv.adauga_client(2,"Popa",1231231231232)
        self.assertEqual(len(self.__srv.afiseaza()),2)
        self.__srv.stergere(1)
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.assertRaises(Validator_client_exception,self.__srv.stergere,-1)
        self.assertRaises(Exception_Repository_Clienti,self.__srv.stergere,3)
    
    def test_modifica_client(self):

        self.__srv.adauga_client(1,"Stefan",1231231231231)
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.__srv.modifica_client(1,"Popel")
        self.assertEqual(self.__srv.cauta(1),"Id: 1, Nume: Popel, CNP: 1231231231231")
        self.assertRaises(Validator_client_exception,self.__srv.modifica_client,1,"")
        self.assertRaises(Validator_client_exception,self.__srv.modifica_client,-1,"")
        self.assertRaises(Validator_client_exception,self.__srv.modifica_client,-1,"Bogdan")
        self.assertRaises(Exception_Repository_Clienti,self.__srv.modifica_client,3,"Silviu")

########################################################################################################################################

class DomainCartiTestCase(unittest.TestCase):

    def setUp(self):

        self.val = Validator_carte()
        self.__carte = Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki")
    
    def tearDown(self):
        
        pass
    
    def test_creare_client(self):

        self.assertEqual(self.__carte.getId_carte(),1)
        self.assertEqual(self.__carte.getTitlu(),"Tata Bogat Tata Sarac")
        self.assertEqual(self.__carte.getDescriere(),"Educatie financiara")
        self.assertEqual(self.__carte.getAutor(),"Robert Kiyosaki")

    def test_modificare_carte(self):

        self.__carte.setTitlu("Carte Mov")
        self.assertEqual(self.__carte.getTitlu(),"Carte Mov")
        self.__carte.setDescriere("Antreprenoriat")
        self.assertEqual(self.__carte.getDescriere(),"Antreprenoriat")
        self.__carte.setAutor("Robert")
        self.assertEqual(self.__carte.getAutor(),"Robert")

    def test_valideaza_carte(self):
        
        self.assertIsNone(self.val.valideaza_carte(self.__carte))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki1"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat Tata Sarac","Educatie98financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat Tata Sarac","Educat9ie financiara","Rob8ert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat2 Tata Sarac","Educatie financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat2 Tata Sarac","Educatie financiara","Rober2t Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat2 Tata Sarac2","Educatie21 financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"Tata Bogat1 Tata1 Sarac","Educatie2 financiara1","Robert1 Kiyosaki2"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-1,"Tata Bogat Tata Sarac","Educatie financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(10001,"Tata Bogat Tata Sarac","Educatie financiara","Rober2t Kiyosaki21"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-1,"Tata Bogat Tata Sarac","Ed21ucatie financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-1,"Tata Bogat Tata Sarac","Educati21 financiara","Robert Kiyosa123ki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-11,"Tata Bo12gat Tata Sar3ac","Educatie financiara","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-112,"Tata Bog1at Ta2ta Sarac","Educatie financiara","Ro2bert Kiyos3aki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(10001,"Tata1 Bog2at Tata Sarac","Edu2catie financiar2a","Robert Kiyosaki"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-25,"Ta3ta Bog5at Ta1ta Sar2ac","Educ3atie finan3ciara","Rob2ert Kiyosak2i"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"","",""))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(-1,"A","2","-1"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"A","B","-"))
        self.assertRaises(Validator_carti_exception,self.val.valideaza_carte,Carte(1,"1","2","3"))

class RepositoryCartiTestCase(unittest.TestCase):

    def setUp(self):

        self.file = open("repository_carti_teste.txt","r")
        self.__repo = Extended_repository_carti("repository_carti_teste.txt")
        self.__repo.salveaza_carte(Carte(1,"Tata Bogat","Antreprenoriat","Robert Kyiosaki"))
        self.__repo.salveaza_carte(Carte(2,"De la idee la bani","Business","Napoleon Hill"))
    
    def tearDown(self):

        self.file.close()
        self.file = open("repository_carti_teste.txt","w")
        self.file.write("")
        self.file.close()
    
    def test_salveaza_carte(self):

        self.assertTrue(len(self.__repo.afisare_carti()) == 2)
        self.__repo.salveaza_carte(Carte(3,"a","a","a"))
        self.assertTrue(len(self.__repo.afisare_carti()) == 3)
        self.assertRaises(Exception_Repository_Carti,self.__repo.salveaza_carte,Carte(2,"b","b","b"))

    def test_cauta_carte_dupa_id(self):

        self.assertIsNone(self.__repo.cauta_carte(0))
        self.assertEqual(self.__repo.cauta_carte(1),"Id: 1, Titlu: Tata Bogat, Descriere: Antreprenoriat, Autor: Robert Kyiosaki")
        self.assertEqual(self.__repo.cauta_carte(2),"Id: 2, Titlu: De la idee la bani, Descriere: Business, Autor: Napoleon Hill")
    
    def test_stergere_carte_id(self):

        self.__repo.salveaza_carte(Carte(3,"a","a","a"))
        self.assertTrue(len(self.__repo.afisare_carti()) == 3)
        self.__repo.sterge_carte_id(3)
        self.assertTrue(len(self.__repo.afisare_carti()) == 2)
        self.assertRaises(Exception_Repository_Carti,self.__repo.sterge_carte_id,222)
    
    def test_modifica_carte_nume(self):

        self.__repo.salveaza_carte(Carte(4,"Modifica","a","a"))
        self.__repo.cauta_carte_id_modifica(4,"a")
        self.assertEqual(self.__repo.cauta_carte(4), "Id: 4, Titlu: a, Descriere: a, Autor: a")
        #self.__repo.sterge_carte_id(10) - in cazul in care doream sa avem cartile din setup in fisier
        self.assertRaises(Exception_Repository_Carti,self.__repo.cauta_carte_id_modifica,101,"S")

    def test_returneaza_obiect_id(self):

        self.assertIsNotNone(self.__repo.returneaza_obiect_carte(1))
        self.assertIsNotNone(self.__repo.returneaza_obiect_carte(2))
        self.assertIsNone(self.__repo.returneaza_obiect_carte(3))
    
    def test_cauta_carte_id_gasit(self):

        self.assertRaises(Exception_Repository_Carti,self.__repo.cauta_carte_id_gasit,555)
        self.assertIsNotNone(self.__repo.cauta_carte_id_gasit(1))
        self.assertIsNotNone(self.__repo.cauta_carte_id_gasit(2))

class ServiceCartiTestCase(unittest.TestCase):

    def setUp(self):

        val = Validator_carte()
        self.file = open("repository_carti_teste.txt","r")
        repo = Extended_repository_carti("repository_carti_teste.txt")
        self.__srv = Service_carte(repo,val)
    
    def tearDown(self):

        self.file.close()
        self.file = open("repository_carti_teste.txt","w")
        self.file.write("")
        self.file.close()
    
    def test_adauga_carte(self):

        self.__srv.adauga_carte(1,"Tata Bogat","Business","Robert Kyiosaki")
        l = self.__srv.afiseaza()
        self.assertTrue(len(l) == 1)
        self.__srv.adauga_carte(2,"De la idee la bani","Antreprenoriat","Napoleon Hill")
        l = self.__srv.afiseaza()
        self.assertTrue(len(l) == 2)
        self.assertRaises(Exception_Repository_Carti,self.__srv.adauga_carte,1,"Carte Mov","Dezvoltare personala","Robert")
        self.assertRaises(Validator_carti_exception,self.__srv.adauga_carte,2,"","Busit","George")

    def test_cauta(self):

        self.__srv.adauga_carte(1,"Tata Bogat","Business","Robert Kyiosaki")
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.assertEqual(self.__srv.cauta(1),"Id: 1, Titlu: Tata Bogat, Descriere: Business, Autor: Robert Kyiosaki")
        self.assertIsNone(self.__srv.cauta(2))
        self.assertRaises(Validator_carti_exception,self.__srv.cauta,-1)
        self.assertRaises(Validator_carti_exception,self.__srv.cauta,1000)
    
    def test_stergere(self):

        self.__srv.adauga_carte(1,"Tata Bogat","Business","Robert Kyiosaki")
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.__srv.adauga_carte(2,"De la idee la bani","Antreprenoriat","Napoleon Hill")
        self.assertEqual(len(self.__srv.afiseaza()),2)
        self.__srv.stergere(1)
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.assertRaises(Validator_carti_exception,self.__srv.stergere,-1)
        self.assertRaises(Exception_Repository_Carti,self.__srv.stergere,100)
    
    def test_modifica_carte(self):

        self.__srv.adauga_carte(1,"Tata Bogat","Business","Robert Kyiosaki")
        self.assertEqual(len(self.__srv.afiseaza()),1)
        self.__srv.modifica_carte(1,"Carte Mov")
        self.assertEqual(self.__srv.cauta(1),"Id: 1, Titlu: Carte Mov, Descriere: Business, Autor: Robert Kyiosaki")
        self.assertRaises(Validator_carti_exception,self.__srv.modifica_carte,1,"")
        self.assertRaises(Validator_carti_exception,self.__srv.modifica_carte,-11,"")
        self.assertRaises(Validator_carti_exception,self.__srv.modifica_carte,-111,"Cadranul banilor")
        self.assertRaises(Exception_Repository_Carti,self.__srv.modifica_carte,2,"Dezvoltare")

########################################################################################################################################

class DomainInchirieriTestCase(unittest.TestCase):

    def setUp(self):

        self.__inchiriere = Inchiriere(1,2,3)
        self.val = Validator_inchiriere()
    
    def tearDown(self):
        
        pass
    
    def test_creare_inchiriere(self):

        self.assertEqual(self.__inchiriere.getId_inchiriere(),1)
        self.assertEqual(self.__inchiriere.getId_client(),2)
        self.assertEqual(self.__inchiriere.getId_carte(),3)
    
    def test_valideaza_inchiriere(self):

        self.assertIsNone(self.val.valideaza_inchiriere(self.__inchiriere))
        self.assertRaises(Validator_inchirieri_exception,self.val.valideaza_inchiriere,Inchiriere(-1,2,3))
        self.assertRaises(Validator_inchirieri_exception,self.val.valideaza_inchiriere,Inchiriere(1000,2,3))

class RepositoryInchirieriTestCase(unittest.TestCase):

    def setUp(self):

        self.file = open("repository_inchirieri_teste.txt","r")
        self.__repo = Extended_repository_inchirieri("repository_inchirieri_teste.txt")
        self.__repo.salveaza_inchiriere(Inchiriere(1,1,1))
        self.__repo.salveaza_inchiriere(Inchiriere(2,2,2))
    
    def tearDown(self):

        self.file.close()
        self.file = open("repository_inchirieri_teste.txt","w")
        self.file.write("")
        self.file.close()
    
    def test_salveaza_inchiriere(self):

        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.salveaza_inchiriere(Inchiriere(3,3,3,))
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 3)
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.salveaza_inchiriere,Inchiriere(1,1,1))
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.salveaza_inchiriere,Inchiriere(1,4,4))

    def test_cauta_id(self):

        self.assertEqual(self.__repo.cauta_id(1),0)
        self.assertEqual(self.__repo.cauta_id(2),0)
        self.assertEqual(self.__repo.cauta_id(3),1)
    
    def test_cauta_inchiriere(self):

        self.assertEqual(self.__repo.cauta_inchiriere(Inchiriere(1,1,1)),0)
        self.assertEqual(self.__repo.cauta_inchiriere(Inchiriere(2,2,2)),0)
        self.assertEqual(self.__repo.cauta_inchiriere(Inchiriere(3,3,3)),1)
    
    def test_sterge(self):
        
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.salveaza_inchiriere(Inchiriere(3,3,3))
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 3)
        self.__repo.sterge(3,3)
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.sterge,3,3)
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.sterge,1,3)
    
    def test_verifica_id_client_exista(self):

        self.assertIsNone(self.__repo.verifica_id_client_exista(1))
        self.assertIsNone(self.__repo.verifica_id_client_exista(2))
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.verifica_id_client_exista,3)
    
    def test_verifica_id_carte_exista(self):

        self.assertIsNone(self.__repo.verifica_id_carte_exista(1))
        self.assertIsNone(self.__repo.verifica_id_carte_exista(2))
        self.assertRaises(Exception_Repository_Inchirieri,self.__repo.verifica_id_carte_exista,3)

    def test_stergere_id_client(self):

        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.stergere_id_client(3)
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.stergere_id_client(1)
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 1)
    
    def test_stergere_id_carte(self):

        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.stergere_id_carte(3)
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 2)
        self.__repo.stergere_id_carte(1)
        self.assertTrue(len(self.__repo.returneaza_inchirieri()) == 1)

class ServiceInchirieriTestCase(unittest.TestCase):

    def setUp(self):

        val_clienti = Validator_client()
        self.file_clienti = open("repository_clienti_teste.txt","r")
        repo_clienti = Extended_repository_clienti("repository_clienti_teste.txt")
        srv_clienti = Service_client(repo_clienti,val_clienti)

        val_carti = Validator_carte()
        self.file_carti = open("repository_carti_teste.txt","r")
        repo_carti = Extended_repository_carti("repository_carti_teste.txt")
        srv_carti = Service_carte(repo_carti,val_carti)

        val = Validator_inchiriere()
        self.file = open("repository_inchirieri_teste.txt","r")
        repo = Extended_repository_inchirieri("repository_inchirieri_teste.txt")
        self.__srv = Service_inchirieri(repo,val,srv_clienti,srv_carti)

        srv_clienti.adauga_client(1,"Stefan Farcasanu",1234567891234)
        srv_clienti.adauga_client(2,"Andrei Grig",1234567891299)
        srv_clienti.adauga_client(3,"Dumitru Gheorghe",1234327891299)
        srv_clienti.adauga_client(4,"Alex Popescu",2323232323232)
        srv_clienti.adauga_client(5,"Rares Stanga",1212121212121)

        srv_carti.adauga_carte(1,"Tata Bogat","Educatie financiara","Robert Kyiosaki")
        srv_carti.adauga_carte(2,"De la idee la bani","Antreprenoriat","Napoleon Hill")
        srv_carti.adauga_carte(3,"Banii stapaneste jocul","Independenta financiara","Tony Robbins")
        srv_carti.adauga_carte(4,"Secretele succesului","Dezvoltare personala","Carnegie")
        srv_carti.adauga_carte(5,"Unshakeable","Business","Tony Robbins")
    
    def tearDown(self):

        self.file_clienti.close()
        self.file_clienti = open("repository_clienti_teste.txt","w")
        self.file_clienti.write("")
        self.file_clienti.close()

        self.file_carti.close()
        self.file_carti = open("repository_carti_teste.txt","w")
        self.file_carti.write("")
        self.file_carti.close()

        self.file.close()
        self.file = open("repository_inchirieri_teste.txt","w")
        self.file.write("")
        self.file.close()
    
    def test_adaugare_inchiriere(self):

        self.__srv.adauga_inchiriere(1,1,1)
        l = self.__srv.afisare_inchirieri()
        self.assertTrue(len(l) == 1)
        self.__srv.adauga_inchiriere(2,2,2)
        l = self.__srv.afisare_inchirieri()
        self.assertTrue(len(l) == 2)
        self.assertRaises(Exception_Repository_Inchirieri,self.__srv.adauga_inchiriere,1,3,3)
        self.assertRaises(Exception_Repository_Inchirieri,self.__srv.adauga_inchiriere,3,2,2)
        self.assertRaises(Validator_inchirieri_exception,self.__srv.adauga_inchiriere,-1,4,4)
        self.assertRaises(Exception_Repository_Clienti,self.__srv.adauga_inchiriere,3,6,1)
        self.assertRaises(Exception_Repository_Carti,self.__srv.adauga_inchiriere,3,1,6)

    def test_id_to_object_client(self):

        self.assertEqual(str(self.__srv.id_to_object_client(1)),"Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234")
        self.assertEqual(str(self.__srv.id_to_object_client(2)),"Id: 2, Nume: Andrei Grig, CNP: 1234567891299")
        self.assertIsNone(self.__srv.id_to_object_client(6))
    
    def test_id_to_object_carte(self):

        self.assertEqual(str(self.__srv.id_to_object_carte(1)),"Id: 1, Titlu: Tata Bogat, Descriere: Educatie financiara, Autor: Robert Kyiosaki")
        self.assertEqual(str(self.__srv.id_to_object_carte(2)),"Id: 2, Titlu: De la idee la bani, Descriere: Antreprenoriat, Autor: Napoleon Hill")
        self.assertIsNone(self.__srv.id_to_object_carte(6))
    
    def test_stergere_inchiriere(self):

        self.__srv.adauga_inchiriere(1,1,1)
        l = self.__srv.afisare_inchirieri()
        self.assertTrue(len(l) == 1)
        self.__srv.adauga_inchiriere(2,2,2)
        l = self.__srv.afisare_inchirieri()
        self.assertTrue(len(l) == 2)
        self.__srv.stergere_inchiriere(2,2)
        l = self.__srv.afisare_inchirieri()
        self.assertTrue(len(l) == 1)
        self.assertRaises(Exception_Repository_Clienti,self.__srv.stergere_inchiriere,6,1)
        self.assertRaises(Exception_Repository_Carti,self.__srv.stergere_inchiriere,1,6)
        self.assertRaises(Validator_client_exception,self.__srv.stergere_inchiriere,-1,2)
        self.assertRaises(Validator_carti_exception,self.__srv.stergere_inchiriere,1,-5)
    
    def test_stergere_inchiriere_id_client(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 3)
        self.__srv.stergere_inchiriere_id_client(1)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 2)
        self.__srv.stergere_inchiriere_id_client(2)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 1)
        self.__srv.stergere_inchiriere_id_client(6)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 1)
    
    def test_stergere_inchiriere_id_carte(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 3)
        self.__srv.stergere_inchiriere_id_carte(1)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 2)
        self.__srv.stergere_inchiriere_id_carte(2)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 1)
        self.__srv.stergere_inchiriere_id_carte(6)
        self.assertTrue(len(self.__srv.afisare_inchirieri()) == 1)
    
    def test_raport_cele_mai_inchiriate_carti(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        self.__srv.adauga_inchiriere(4,4,1)
        l = self.__srv.rapoarte_cele_mai_inchiriate_carti()
        self.assertEqual(len(l),3)
        self.assertEqual(str(l[0]),"Id: 1, Titlu: Tata Bogat, Descriere: Educatie financiara, Autor: Robert Kyiosaki")
        self.__srv.stergere_inchiriere(1,1)
        self.__srv.adauga_inchiriere(1,1,2)
        l = self.__srv.rapoarte_cele_mai_inchiriate_carti()
        self.assertEqual(str(l[0]),"Id: 2, Titlu: De la idee la bani, Descriere: Antreprenoriat, Autor: Napoleon Hill")

    def test_raport_clienti_carti_ordonat_nume(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        l = self.__srv.raport_clienti_carti_ordonat_nume()
        self.assertEqual(str(l[0]),"Id: 2, Nume: Andrei Grig, CNP: 1234567891299")
        self.__srv.adauga_inchiriere(4,4,4)
        l = self.__srv.raport_clienti_carti_ordonat_nume()
        self.assertEqual(str(l[0]),"Id: 4, Nume: Alex Popescu, CNP: 2323232323232")
    
    def teste_raport_clienti_ordonat_inchirieri(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        self.__srv.adauga_inchiriere(4,1,2)
        l = self.__srv.raport_clienti_carti_ordonat_inchirieri()
        self.assertEqual(str(l[0]),"Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234")
        self.__srv.adauga_inchiriere(5,2,3)
        self.__srv.adauga_inchiriere(6,2,4)
        l = self.__srv.raport_clienti_carti_ordonat_inchirieri()
        self.assertEqual(str(l[0]),"Id: 2, Nume: Andrei Grig, CNP: 1234567891299")
    
    def teste_raport_clienti_activi(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        self.__srv.adauga_inchiriere(3,3,3)
        self.__srv.adauga_inchiriere(4,4,4)
        self.assertRaises(Exception_service_inchirieri,self.__srv.raport_clienti_activi)
        self.__srv.adauga_inchiriere(5,5,5)
        l = self.__srv.raport_clienti_activi()
        self.assertEqual(str(l[0]),"Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234")
        self.__srv.adauga_inchiriere(6,1,2)
        self.__srv.adauga_inchiriere(7,1,3)
        l = self.__srv.raport_clienti_activi()
        self.assertEqual(str(l[0]),"Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234")
    
    def teste_afisare(self):

        self.__srv.adauga_inchiriere(1,1,1)
        self.__srv.adauga_inchiriere(2,2,2)
        l = self.__srv.afisare_inchirieri()
        self.assertEqual(str(l[0]),"{'id_inchiriere': 1, 'client': 'Id: 1, Nume: Stefan Farcasanu, CNP: 1234567891234', 'carte': 'Id: 1, Titlu: Tata Bogat, Descriere: Educatie financiara, Autor: Robert Kyiosaki'}")
        self.assertEqual(str(l[1]),"{'id_inchiriere': 2, 'client': 'Id: 2, Nume: Andrei Grig, CNP: 1234567891299', 'carte': 'Id: 2, Titlu: De la idee la bani, Descriere: Antreprenoriat, Autor: Napoleon Hill'}")