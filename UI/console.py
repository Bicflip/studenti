import Repository.studentrepo
from Service import studentservice
from Repository import studentrepo


class user_interface:
    def __init__(self, stud_services: studentservice.StudentServices):
        self.__stud_services = stud_services

    def menu(self):
        print("Alege o optiune:")
        print("1.Adauga studentii din fisier:")
        print("2.Printeaza lista de studenti.")
        print("3.Adauga bonus 1 punct la nota, la studentii care au peste 10 prezente.")
        print("0.Exit the program")

    def consola(self):
        self.menu()
        lista_studenti = []
        stop = True
        stud_repo = studentrepo.StudentRepo()
        while stop:
            optiune = int(input("Optiune:"))
            if optiune == 1:
                """id_student = int(input("id_student: "))
                nume = input("nume: ")
                prezente = int(input("prezente: "))
                nota = int(input("nota: "))
                student = entity.Student(id_student, nume, prezente, nota)
                stud_repo.add_stud(student)"""
                for stud in stud_repo.get_all_studs_from_list():
                    lista_studenti.append(stud)
                    print(stud)
                self.menu()
            elif optiune == 2:
                for index in range(len(lista_studenti)):
                    print(lista_studenti[index])
                self.menu()
            elif optiune == 3:
                studentrepo.StudentRepo.add_bonus(stud_repo)
                self.menu()
            elif optiune == 0:
                print("Program inchis!")
                stop = False


