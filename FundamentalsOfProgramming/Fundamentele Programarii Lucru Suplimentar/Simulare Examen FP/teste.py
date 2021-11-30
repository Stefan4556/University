from domain.lab import Lab,ValidatorLabException,ValidatorLab
from domain.student import Student,ValidatorStudentException,ValidatorStudent

from repository.labrepository import LabRepository,LabRepositoryException
from repository.studentrepository import StudentRepository

from ui.labcontroller import LabController,LabControllerException

# teste pentru domain lab
def teste_domain_lab():
    
    l = Lab(1,1,"1")
    assert l.getIdStudent() == 1
    assert l.getLabNr() == 1
    assert l.getProblemNr() == "1"
    v = ValidatorLab()
    l = Lab(0,1,"1")
    try:
        v.validate(l)
        assert False
    except ValidatorLabException:
        assert True
    l = Lab(1,0,"1")
    try:
        v.validate(l)
        assert False
    except ValidatorLabException:
        assert True
    l = Lab(1,1,"-1")
    try:
        v.validate(l)
        assert False
    except ValidatorLabException:
        assert True
    l = Lab(1,1,"1")
    try:
        v.validate(l)
        assert True
    except ValidatorLabException:
        assert False

# teste pentru domain student
def teste_domain_student():
    
    s = Student(1,"Stefan")
    assert s.getId() == 1
    assert s.getNume() == "Stefan"
    v = ValidatorStudent()
    
    s = Student(-1,"Stefan")
    try:
        v.validate(s)
        assert False
    except ValidatorStudentException:
        assert True
    
    s = Student(1,"")
    try:
        v.validate(s)
        assert False
    except ValidatorStudentException:
        assert True
    
    s = Student(1,"Stefan")
    try:
        v.validate(s)
        assert True
    except ValidatorStudentException:
        assert False
    
    s = Student(-1,"")
    try:
        v.validate(s)
        assert False
    except ValidatorStudentException:
        assert True

# teste pentru repo lab
def teste_repo_lab():
    
    try:
        f = open("labs_test.txt","w")
    except IOError:
        pass
    f.write("1, 1, 1\n2, 2, 2\n3, 3, 3\n")
    f.close()

    repo = LabRepository("labs_test.txt")

    l = repo.getAll()
    assert len(l) == 3

    assert repo.cauta_nr_lab(1,"1") == True
    assert repo.cauta_nr_lab(1,"3") == False

    repo.add(Lab(1,4,"4"))
    l = repo.getAll()
    assert len(l) == 4

    try:
        repo.add(Lab(1,3,"1"))
        assert False
    except LabRepositoryException:
        assert True

# teste pentru repo studenti
def teste_repo_student():

    try:
        f = open("student_test.txt","w")
    except IOError:
        pass
    f.write("1, Stefan\n2, Radu\n3, Andrei\n")
    f.close()

    repo = StudentRepository("student_test.txt")

    l = repo.getAll()
    assert len(l) == 3

    assert str(repo.findById(1)) == "Id: 1 Nume: Stefan"
    assert repo.findById(20) == None

    assert str(repo.id_to_obj_st(1)) == "Id: 1 Nume: Stefan"

# teste lab controller
def teste_lab_controller():

    try:
        f = open("labs_test.txt","w")
    except IOError:
        pass
    f.write("1, 1, 1\n2, 2, 2\n3, 3, 3\n")
    f.close()

    repo_lab = LabRepository("labs_test.txt")
    val_lab = ValidatorLab()

    try:
        f = open("student_test.txt","w")
    except IOError:
        pass
    f.write("1, Stefan\n2, Radu\n3, Andrei\n")
    f.close()

    repo_stud = StudentRepository("student_test.txt")
    val_stud = ValidatorStudent()

    srv = LabController(repo_stud,repo_lab,val_stud,val_lab)

    try:
        srv.addLab(1,3,"1")
        assert False
    except LabRepositoryException:
        assert True

    srv.addLab(1,5,"5")

    l = srv.getLabsByStudentId(1)
    assert len(l) == 2

    try:
        srv.getLabsByStudentId(20)
        assert False
    except LabControllerException:
        assert True
    
    assert str(srv.getStudentById(1)) == "Id: 1 Nume: Stefan"

    try:
        srv.getStudentById(20)
        assert False
    except LabControllerException:
        assert True
    
    l = srv.vizualizare_lista_studenti()
    assert len(l) == 3

    l = srv.vizualizare_st_pb_nr_lab(1)
    assert len(l) == 1

    try:
        l = srv.vizualizare_st_pb_nr_lab(20)
        assert False
    except LabControllerException:
        assert True

# rulam toate testele
def ruleaza_teste():
    
    teste_domain_lab()
    teste_domain_student()
    teste_repo_lab()
    teste_repo_student()
    teste_lab_controller()

ruleaza_teste()