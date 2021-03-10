class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mean_grade(self):
        return sum([sum(x) for x in self.grades.values()]) / len([sum(x) for x in self.grades.values()])


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname},\nСредняя оценка за домашние задания: {self.mean_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Завершенные курсы: {", ".join(map(str, self.finished_courses))}'

    def __lt__(self, other):
        return self.mean_grade() > other.mean_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mean_grade()}'

    def mean_grade(self):
        return sum(self.grades)/len(self.grades)

    def __lt__(self, other):
        return self.mean_grade() < other.mean_grade()



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Math']
best_student.finished_courses += ['Git']

middle_student = Student('Abigail', 'Gibson', 'female')
middle_student.courses_in_progress += ['Python']
middle_student.courses_in_progress += ['Git']
middle_student.finished_courses += ['Math']

worst_student = Student('Mark', 'Goodman', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.courses_in_progress += ['Git']
worst_student.courses_in_progress += ['Math']

python_reviewer = Reviewer('Some', 'Buddy')
python_reviewer.courses_attached += ['Python']
python_reviewer.rate_hw(best_student, 'Python', 10)
python_reviewer.rate_hw(middle_student, 'Python', 7)
python_reviewer.rate_hw(worst_student, 'Python', 4)

git_reviewer = Reviewer('Ronald', 'Barker')
git_reviewer.courses_attached += ['Git']
git_reviewer.rate_hw(middle_student, 'Git', 7)
git_reviewer.rate_hw(worst_student, 'Git', 4)

math_reviewer = Reviewer('Jacob', 'Cooper')
math_reviewer.courses_attached += ['Math']
math_reviewer.rate_hw(best_student, 'Math', 10)
math_reviewer.rate_hw(worst_student, 'Math', 4)

python_lecturer = Lecturer('Tyler', 'Atkinson')
python_lecturer.courses_attached += ['Python']

git_lecturer = Lecturer('Dylan', 'Dennis')
git_lecturer.courses_attached += ['Git']

math_lecturer = Lecturer('Noel', 'Dean')
math_lecturer.courses_attached += ['Math']

best_student.rate_hw(python_lecturer, 'Python', 10)
middle_student.rate_hw(python_lecturer, 'Python', 6)
worst_student.rate_hw(python_lecturer, 'Python', 4)

middle_student.rate_hw(git_lecturer, 'Git', 5)
worst_student.rate_hw(git_lecturer, 'Git', 2)

best_student.rate_hw(math_lecturer, 'Math', 9)
worst_student.rate_hw(math_lecturer, 'Math', 3)

print(f'Оценки полученные python_lecturer - {python_lecturer.name} {python_lecturer.surname}: {python_lecturer.grades}')
print(f'Оценки полученные git_lecturer - {git_lecturer.name} {git_lecturer.surname}: {git_lecturer.grades}')
print(f'Оценки полученные math_lecturer - {math_lecturer.name} {math_lecturer.surname}: {math_lecturer.grades}')

print(f'Оценки полученные студентом best_student - {best_student.name} {best_student.surname}: {best_student.grades}') #{Key = предмет : value = оценка}
print(f'Оценки полученные студентом middle_student - {middle_student.name} {middle_student.surname}: {middle_student.grades}')
print(f'Оценки полученные студентом worst_student - {worst_student.name} {worst_student.surname}: {worst_student.grades}')
print()
print(python_reviewer,'\n')  # print(some_reviewer)
print(math_lecturer,'\n')    # print(some_lecturer)
print(middle_student,'\n')   # print(some_student)
print(worst_student.__lt__(middle_student))       #Сравнение средних оценок студентов
print(git_lecturer.__lt__(math_lecturer))       # Сравнение средних оценок лекторов

