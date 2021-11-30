from Domain.domain_word import Word,WordValidator,WordValidatorException
from Repository.repository_word import Repository,RepositoryException
from UI.service_word import SpellCheckerController,SpellCheckerControllerException

# teste pentru domain
def teste_domain():

    w = Word(1,"Ro","Da")

    assert w.getId() == 1
    assert w.getLang() == "Ro"
    assert w.getWord() == "Da"

    val = WordValidator()
    w = Word(1,"da","ok")
    try:
         val.validate(w)
         assert False
    except WordValidatorException:
        assert True
    
    w = Word(1,"En","")
    try:
        val.validate(w)
        assert False
    except WordValidatorException:
        assert True

# teste pentru repository
def teste_repository():
    
    try:
        fisier_test = open("dictionar_test.txt","w")
    except IOError:
        pass
    
    fisier_test.write("1, En, Today\n2, Ro, Cafea\n3, Fr, Baghete\n4, En, mere")
    fisier_test.close()

    repo = Repository("dictionar_test.txt")

    l = repo.getAll()
    assert len(l) == 4

    assert repo.verifica_id(1) == True
    assert repo.verifica_id(100) == False

    assert repo.exista_word("Today") == True
    assert repo.exista_word("hello") == False

    assert repo.exista_word_in_lang("En","Today") != None
    assert repo.exista_word_in_lang("En","Chitara") == None

    repo.adaugare_word(Word(100,"Ro","Bine"))
    l = repo.getAll()
    assert len(l) == 5

    try:
        repo.adaugare_word(Word(1,"Ro","Bine"))
        assert False
    except RepositoryException:
        assert True
    
    try:
        repo.adaugare_word(Word(100,"Ro","Today"))
        assert False
    except RepositoryException:
        assert True

    repo.golire_fisier_output("o.txt")

    repo.citeste_fisier_input_rezolva("i.txt","En","o.txt")

    repo.scrie_fisier_output(["Ana","are","mere"],"En","o.txt")

    repo.verifica_prop_fisier("i.txt","En","o.txt")

# teste pentru service
def teste_service():

    try:
        fisier_test = open("dictionar_test.txt","w")
    except IOError:
        pass
    
    fisier_test.write("1, En, Today\n2, Ro, Cafea\n3, Fr, Baghete\n4, En, mere")
    fisier_test.close()

    repo = Repository("dictionar_test.txt")
    val = WordValidator()

    srv = SpellCheckerController(repo,val)

    srv.addWord(100,"En","Friday")

    l = srv.afisare_cuvinte()
    assert len(l) == 5

    try:
        srv.addWord(100,"Ro","Sticla")
        assert False
    except RepositoryException:
        assert True
    
    try:
        srv.addWord(101,"","")
        assert False
    except WordValidatorException:
        assert True
    
    try:
        l = srv.verifica_propozitie("En","Friday")
        assert False
    except SpellCheckerControllerException:
        assert True
    
    l = srv.verifica_propozitie("Ro","Popa")
    assert len(l) == 1

    srv.verifica_propozitie_fisier("i.txt","En","o.txt")

def ruleaza_teste():

    teste_domain()
    teste_repository()
    teste_service()

ruleaza_teste()