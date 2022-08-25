class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculation_avg_grade(self):
        strl = []
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len(strl)
            return avg_grade
        return 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if (not isinstance(self, Student)) or (not isinstance(other, Student)):
            return
        elif other.calculation_avg_grade() < self.calculation_avg_grade():
            print(f'Средний балл выше у студента: {self.name}')
        else:
            print(f'Средний балл выше у студента: {other.name}')

    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.calculation_avg_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
"""


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calculation_avg_grade(self):
        strl = []
        for _, grades_list in self.grades.items():
            strl.extend(grades_list)
        if len(strl) != 0:
            avg_grade = sum(strl) / len(strl)
            return avg_grade
        return 0

    def __lt__(self, other):
        if (not isinstance(self, Lecturer)) or (not isinstance(other, Lecturer)):
            return
        elif other.calculation_avg_grade() < self.calculation_avg_grade():
            print(f'Средний балл выше у лектора: {self.name}')
        else:
            print(f'Средний балл выше у лектора: {other.name}')

    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calculation_avg_grade()}
"""


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
"""


# Student's
first_student = Student('Igor', 'Sokolov', 'male')
first_student.add_courses('Программирование')
first_student.courses_in_progress += ['ООП', 'Git']
second_student = Student('Irina', 'Smorodova', 'female')
second_student.add_courses('Программирование')
second_student.courses_in_progress += ['ООП', 'Git']

# Lecturer's
first_lecturer = Lecturer('Alexey', 'Egorov')
first_lecturer.courses_attached += ['ООП', 'Git']
second_lecturer = Lecturer('Irina', 'Kurashova')
second_lecturer.courses_attached += ['ООП', 'Git']

# Reviewer's
first_reviewer = Reviewer('Alexey', 'Egorov')
first_reviewer.courses_attached += ['ООП', 'Git']
second_reviewer = Reviewer('Irina', 'Kurashova')
second_reviewer.courses_attached += ['ООП', 'Git']

# Student's rate hw:
first_student.rate_hw(first_lecturer, 'ООП', 7)
first_student.rate_hw(first_lecturer, 'ООП', 9)
first_student.rate_hw(first_lecturer, 'Git', 4)
first_student.rate_hw(first_lecturer, 'Git', 6)
first_student.rate_hw(second_lecturer, 'ООП', 6)
first_student.rate_hw(second_lecturer, 'ООП', 10)
first_student.rate_hw(second_lecturer, 'Git', 3)
first_student.rate_hw(second_lecturer, 'Git', 7)
second_student.rate_hw(first_lecturer, 'ООП', 2)
second_student.rate_hw(first_lecturer, 'ООП', 5)
second_student.rate_hw(first_lecturer, 'Git', 3)
second_student.rate_hw(first_lecturer, 'Git', 4)
second_student.rate_hw(second_lecturer, 'ООП', 9)
second_student.rate_hw(second_lecturer, 'ООП', 8)
second_student.rate_hw(second_lecturer, 'Git', 5)
second_student.rate_hw(second_lecturer, 'Git', 9)

# Reviewer's rate_hw
first_reviewer.rate_hw(first_student, 'ООП', 6)
first_reviewer.rate_hw(first_student, 'ООП', 10)
first_reviewer.rate_hw(first_student, 'Git', 6)
first_reviewer.rate_hw(first_student, 'Git', 7)
first_reviewer.rate_hw(second_student, 'ООП', 8)
first_reviewer.rate_hw(second_student, 'ООП', 7)
first_reviewer.rate_hw(second_student, 'Git', 5)
first_reviewer.rate_hw(second_student, 'Git', 6)

second_reviewer.rate_hw(first_student, 'ООП', 1)
second_reviewer.rate_hw(first_student, 'ООП', 6)
second_reviewer.rate_hw(first_student, 'Git', 7)
second_reviewer.rate_hw(first_student, 'Git', 8)
second_reviewer.rate_hw(second_student, 'ООП', 10)
second_reviewer.rate_hw(second_student, 'ООП', 3)
second_reviewer.rate_hw(second_student, 'Git', 6)
second_reviewer.rate_hw(second_student, 'Git', 4)

print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)

is_lt = (first_student < second_student)
first_lecturer.__lt__(second_lecturer)

students = [first_student, second_student]
lecturers = [first_lecturer, second_lecturer]

def avg_course_students(students, course):
    sum_ = 0
    res = 0
    grade_list = []
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                grade_list.extend(value)
    sum_ += sum(grade_list)
    res = round(sum_ / len(grade_list), 2)
    print(f"Средняя оценка студентов по курсу {course}: {res}")

def avg_course_lecturers(lecturers, course):
    sum_ = 0
    res = 0
    grade_list = []
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                grade_list.extend(value)
    sum_ += sum(grade_list)
    res = round(sum_ / len(grade_list), 2)
    print(f'Средняя оценка лекторов по курсу {course}: {res}')


avg_course_students(students, 'ООП')
avg_course_students(students, 'Git')

avg_course_lecturers(lecturers, 'ООП')
avg_course_lecturers(lecturers, 'Git')
