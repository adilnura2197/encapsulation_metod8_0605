class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary

    def teacher(self, house):
        self._subject += house

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"Teaching {self._subject} hourse")
        print(f"Salary: {self.__salary}")


t1 = Teacher("Ali", 1, 1000)
t1.teacher(1)
t1.increase_salary(200)
t1.info()
