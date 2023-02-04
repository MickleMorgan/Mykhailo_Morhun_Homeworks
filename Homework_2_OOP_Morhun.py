class Person:
    def __init__(self, name, surname, sex, age, nationality):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.nationality = nationality


    def __str__(self):
        if self.nationality.lower() == ('russian'):
            raise TypeError('russian ship go to hell')
        else:
            return f'Name: {self.name} {self.surname}\nSex: {self.sex}\nAge {self.age} years\n' \
                   f'Nationality {self.nationality}'


class Student(Person):
    def __init__(self, name, surname, sex, age, nationality, status):
        super().__init__(name, surname, sex, age, nationality)
        self.status = status

    def __str__(self):
        return f'{super().__str__()}\nStatus:{self.status}\n'


class Group:
    def __init__(self, speciality, group_type, group_size=10):
        self.speciality = speciality
        self.group_type = group_type
        self.__students = []
        self.group_size = group_size

    def add_student(self, student):
        if student not in self.__students and len(self.__students) < self.group_size:
            self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def find_student(self, surname):
        find_student = []
        for person in self.__students:
            if person.surname == surname:
                find_student.append(person)
        return find_student

    def __str__(self):
        return f'Group:{self.speciality}\n{self.group_type}\n\n' + '\n'.join(map(str, self.__students))


x = Group('IT', 'Extramural',  group_size=2)
y = Group('Non_IT', 'full-time', group_size=3)

x.add_student(Student('Andriy1', 'Kovalenko1', 'M', 20, 'Ukrainian', 'Attending'))
x.add_student(Student('Andriy2', 'Kovalenko2', 'M', 20, 'Ukrainian', 'Attending'))
x.add_student(Student('Andriy3', 'Kovalenko3', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy1', 'Kovalenko1', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy2', 'Kovalenko2', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy3', 'Kovalenko3', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy4', 'Kovalenko4', 'M', 20, 'Ukrainian', 'Attending'))

print(y)
print(x)


