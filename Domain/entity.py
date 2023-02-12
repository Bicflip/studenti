class Student:
    def __init__(self, stud_id: int, name: str, prezenta: int, nota: int):
        self.__stud_id = stud_id
        self.__name = name
        self.__prezenta = prezenta
        self.__nota = nota

    @property
    def stud_id(self):
        return self.__stud_id

    @property
    def name(self):
        return self.__name

    @property
    def prezenta(self):
        return self.__prezenta

    @property
    def nota(self):
        return self.__nota

    @stud_id.setter
    def stud_id(self, new_id):
        self.__stud_id = new_id

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @prezenta.setter
    def prezenta(self, new_prez):
        self.__prezenta = new_prez

    @nota.setter
    def nota(self,new_nota):
        self.__nota = new_nota

    def add_bonus(self, student,  ):
        pass

    def __str__(self):
        return f"ID Student: {self.__stud_id}, Nume: {self.__name}, Prezente: {self.__prezenta}, Nota: {self.__nota}"



class StudentValidator:
    def __init__(self, student: Student):
        self.__student = student

    def validate(self, student: Student):
        if isinstance(student, Student):
            pass
        else:
            raise ValueError("Student instance incorrect!")





