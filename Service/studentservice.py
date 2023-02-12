from Domain.entity import Student
from Repository.studentrepo import StudentRepo


class StudentServices:
    def __init__(self, stud_repo: StudentRepo):
        self.__stud_repository = stud_repo

    def add_student(self, stud_id, name, prezenta, nota):
        new_stud = Student(stud_id, name, prezenta, nota)
        self.__stud_repository.add_stud(new_stud)

    def get_all_studs_from_list(self):
        return self.__stud_repository.get_all_studs_from_list()
