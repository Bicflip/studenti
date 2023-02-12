from Domain.entity import Student


class StudentRepo:
    def __init__(self, filename= "studenti.txt"):
        self.__studenti = []
        self.__filename = filename
        self.load_file()

    def load_file(self):
        """
        incarca fisierul si citeste din el toti studentii din lista, dupa care adauga in lista_studenti pe fiecare.
        Split desparte fiecare element al obiectului student daca are ", " dupa el, astfel se stie de unde incepe
        urmatorul element adica nota/prezenta, etc.
        :return: adauga in lista de studenti, studentii din fisier
        """
        deschide = open(self.__filename, 'rt')
        lines = deschide.readlines()
        for student in lines:
            student_info = student.split(", ")
            id_s = student_info[0]
            name = student_info[1]
            attendance = student_info[2]
            grade = student_info[3]
            stud = Student(int(id_s), str(name), int(attendance), int(grade))
            self.add_stud(stud)
        deschide.close()

    def find(self, stud_id):
        """
        cauta in lista de studenti id-ul pe care il vom introduce
        :param stud_id: id student
        :return: studentul daca exista deja id-ul si NONE daca id-ul e inexistent
        """
        for student in self.__studenti:
            if stud_id == student.stud_id:
                return student
        return None

    def add_stud(self, new_stud: Student):
        """
        Functia adauga un student in lista daca id-ul introdus nu exista deja
        :param new_stud: studentul pe care vrem sa il adaugam in lista
        :return: adauga in lista de studenti noul obiect
        """
        if self.find(new_stud.stud_id) is not None:
            print("Studentul cu ID-ul: " + str(new_stud.stud_id) + " este deja in lista!")
        self.__studenti.append(new_stud)

    def add_bonus(self):
        for student in self.__studenti:
            if student.prezenta >= 10:
                if student.nota <= 9:
                    student.nota = student.nota + 1
                else:
                    student.nota = 10


    def get_all_studs_from_list(self):
        """
        :return: toata lista de studenti
        """
        return self.__studenti

    def __len__(self):
        return len(self.__studenti)

    def __str__(self):
        list_of_students = ""
        for stud in self.__studenti:
            list_of_students += stud
            list_of_students += "\n"
        return list_of_students

