from domain import Carte,ValidatorCarteException,ValdiatorCarte
from repository_carti import Repository,RepositoryException
from service import Service,ServiceException
import unittest

class Teste_domain(unittest.TestCase):

    def setUp(self):

        self.c = Carte(1,"a","a",1)
    
    def tearDown(self):

        self.c = Carte(1,"a","a",1)
    
    def testGetteri(self):

        self.assertEqual(self.c.getId(),1)
        self.assertEqual(self.c.getTitlu(),"a")
        self.assertEqual(self.c.getAutor(),"a")
        self.assertEqual(self.c.getAn_aparitie(),1)
    
    def testSetter(self):

        self.c.setAutor("b")
        self.assertEqual(self.c.getAutor(),"b")
    
    def testValdiator(self):

        v = ValdiatorCarte()
        
        self.assertRaises(ValidatorCarteException,v.validate,Carte(-1,"a","a",1))
        with self.assertRaises(ValidatorCarteException):
            v.validate(Carte(1,"","a",1))
            v.validate(Carte(1,"a","",1))
            v.validate(Carte(1,"a","a",-1))
        
        self.assertIsNone(v.validate(Carte(1,"a","a",1)))

class Teste_repo(unittest.TestCase):

    def setUp(self):

        try:
            f = open("biblioteca_test.txt","w")
        except IOError:
            return
        f.write("1; Harap Alb; dadaaa; 1974\n2; Carte; Autor; 2012\n3; Mov; Hautor; 2013\n10; da; dadaaa; 10\n")
        f.close()
        
        self.repo = Repository("biblioteca_test.txt")
    
    def tearDown(self):

        pass
    
    def test_read_from_file(self):

        l = self.repo.getAll()
        self.assertTrue(len(l) == 4)
        try:
            f = open("biblioteca_test.txt","w")
        except IOError:
            return
        f.write("1; Harap Alb; dadaaa; 1974\n3; Mov; Hautor; 2013\n10; da; dadaaa; 10\n")
        f.close()
        repo = Repository("biblioteca_test.txt")
        l = repo.getAll()
        self.assertTrue((len(l) == 3))
    
    def test_write_to_file(self):

        l = self.repo.getAll()
        self.assertTrue(len(l) == 4)
        self.repo.adaugare_carte(Carte(100,"a","a",100))

        repo = Repository("biblioteca_test.txt")
        l = repo.getAll()
        self.assertTrue((len(l) == 5))