import logging
logger = logging.getLogger('simple_example')
ch = logging.FileHandler(__name__)
ch.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class TooMuchStudents(Exception):
    def __init__(self, max_group: int):
        self.max_group = max_group

    def __str__(self):
        return f'You can\'t add more than {self.max_group} students'


class StudentAlreadyExist(Exception):
    def __init__(self, student, group_name):
        self.student = student
        self.group_name = group_name

    def __str__(self):
        return f'{self.student} is already in group {self.group_name}'


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
        self.students = []
        self.group_size = group_size

    def add_student(self, student):
        if len(self.students) > self.group_size:
            raise TooMuchStudents(self.group_size)
        if student in self.students:
            raise StudentAlreadyExist(student, self.speciality)
        self.students.append(student)
        logger.info('Student added')


    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_student(self, surname):
        find_student = []
        for person in self.students:
            if person.surname == surname:
                find_student.append(person)
        return find_student

    def __str__(self):
        return f'Group:{self.speciality}\n{self.group_type}\n\n' + '\n'.join(map(str, self.students))


x = Group('IT', 'Extramural', group_size=3)
y = Group('Non_IT', 'full-time', group_size=3)

st1 = Student('1', '1', 'M', 20, 'Ukrainian', 'Attending')
x.add_student(st1)
x.add_student(Student('1', '1', 'M', 20, 'Ukrainian', 'Attending'))
x.add_student(Student('Andriy', 'Kovalenko', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy1', 'Kovalenko1', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy2', 'Kovalenko2', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy3', 'Kovalenko3', 'M', 20, 'Ukrainian', 'Attending'))
y.add_student(Student('Andriy4', 'Kovalenko4', 'M', 20, 'Ukrainian', 'Attending'))


print(x)
