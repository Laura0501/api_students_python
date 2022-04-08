from model.student import Student
from model.list_se import ListSE

class ListSE_service:
    cities = ["Manizales", "Pereira", "Chinchina", "Armenia"]

    def __init__(self):
        self.students=ListSE()

        """camilo=Student("1053807435", 1, 3540899, True, "Camilo Villegas", 26, "Urbana", self.cities[1])


      gloria=Student({"identification":"30318536", "name": "Gloria Cuellar", "gender": 2, "salary":1250678,
                        "job":True, "age": 35, "zone":"Urbana", "city":self.cities[0]})

        self.students.add(gloria)

        self.students.add({"identification":"1053802424", "name": "Felipe Alvaran", "gender": 1, "salary":1178000,
                        "job":True, "age": 28, "zone":"Urbana", "city":self.cities[1]})"""


    #Agregar el estudiante a la cabeza

    def get_all_students(self):
        return self.students.head

    #Agregar un estudiante desde postman

    def add_student(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add(student)
        else:
            raise Exception("La ciudad no está en el listado")


    #Invertir la lista
    def reversed_list(self):
        head=self.students.head
        while head!=None:
            temp=head.next
            head.next=previous
            previous=head
            head = temp
        self.head=previous
        return previous




