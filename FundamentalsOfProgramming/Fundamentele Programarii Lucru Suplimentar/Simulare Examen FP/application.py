"""
    In modulul application.py sunt facute toate importurile si este pornita aplicatia
"""

from domain.student import Student,ValidatorStudent
from domain.lab import Lab,ValidatorLab

from repository.studentrepository import StudentRepository
from repository.labrepository import LabRepository

from ui.labcontroller import LabController
from ui.labui import LabUI

from teste import ruleaza_teste

ruleaza_teste()

student_val = ValidatorStudent()
lab_val = ValidatorLab()

repo_student = StudentRepository("student.txt")
repo_lab = LabRepository("labs.txt")

srv = LabController(repo_student,repo_lab,student_val,lab_val)

console = LabUI(srv)

console.run()