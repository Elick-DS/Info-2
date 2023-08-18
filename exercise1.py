class Person:
    def __init__(self, name, id:int, gender):
        self._name = name
        self._id = id
        self.gender = gender

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"ID: {self._id}")
        print(f"Gender: {self.gender}")

class Medical_staff(Person):
    def __init__(self, name, id, gender, turn, position):
        super().__init__(name, id, gender)
        self._turn = turn
        self._position = position

    def display_info(self):
        super().display_info()
        print(f"Turn: {self._turn}")
        print(f"Position: {self._position}")

class Doctor(Medical_staff):
    def __init__(self, name, id, gender, turn, position, specialty):
        super().__init__(name, id, gender, turn, position)
        self.specialty = specialty

    def display_info(self):
        super().display_info()
        print(f"Specialty: {self.specialty}")

class Nurse(Medical_staff):
    def __init__(self, name, id, gender, turn, position, rank):
        super().__init__(name, id, gender, turn, position)
        self._rank = rank

    def display_info(self):
        super().display_info()
        print(f"Rank: {self._rank}")

class Patient(Person):
    def __init__(self, name, id, gender, service):
        super().__init__(name, id, gender)
        self._service = service

    def display_info(self):
        super().display_info()
        print(f"Service: {self._service}")

print("------------------------------------------")
a = Person("Andres", 1000321321, "Masculino")
a.display_info()
print("------------------------------------------")
b = Doctor("Camilo", 1000654212, "Masculino", "Diurno", "Jefe", "Cirujano")
b.display_info()
print("------------------------------------------")
c = Nurse("Natalia", 123689653, "Femenina", "Nocturno", "Enfermera", "Jefe de enfermería")
c.display_info()