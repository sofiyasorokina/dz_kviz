class Student:
    def __init__(self, name, surname, gender): 
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Введение в програмирование"]
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашнее задание: {sum(self.grades["Python"]) / len(self.grades["Python"])}\n\
Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grade:
                lecturer.lecturer_grade[course] += [grade]
            else:
                lecturer.lecturer_grade[course] = [grade]
        else:
            return 'Ошибка'
    def __eq__(self, __value: object) -> bool:
        return sum(self.grades["Python"]) / len(self.grades["Python"]) == sum(__value.grades["Python"]) / len(__value.grades["Python"])
    
    def __lt__(self, __value: object) -> bool:
        return sum(self.grades["Python"]) / len(self.grades["Python"]) < sum(__value.grades["Python"]) / len(__value.grades["Python"])
    
    def __qt__(self, __value: object) -> bool:
        return sum(self.grades["Python"]) / len(self.grades["Python"]) > sum(__value.grades["Python"]) / len(__value.grades["Python"])

    def __ne__(self, __value: object) -> bool:
        return sum(self.grades["Python"]) / len(self.grades["Python"]) != sum(__value.grades["Python"]) / len(__value.grades["Python"])
    
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grade = {}
    def __str__(self) -> str:
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашнее задание: {sum(self.lecturer_grade["C++"]) / len(self.lecturer_grade["C++"])}\n'

    def __eq__(self, __value: object) -> bool:
        return sum(self.lecturer_grade["C++"]) / len(self.lecturer_grade["C++"]) == sum(__value.lecturer_grade["C++"]) / len(__value.lecturer_grade["C++"])
    
    def __lt__(self, __value: object) -> bool:
        return sum(self.lecturer_grade["C++"]) / len(self.lecturer_grade["C++"]) < sum(__value.lecturer_grade["C++"]) / len(__value.lecturer_grade["C++"])
    
    def __qt__(self, __value: object) -> bool:
        return sum(self.lecturer_grade["C++"]) / len(self.lecturer_grade["C++"]) > sum(__value.lecturer_grade["C++"]) / len(__value.lecturer_grade["C++"])
    
    def __ne__(self, __value: object) -> bool:
        return sum(self.lecturer_grade["C++"]) / len(self.lecturer_grade["C++"]) != sum(__value.lecturer_grade["C++"]) / len(__value.lecturer_grade["C++"])
    

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def survivors(students, course):
    srednya_grades = 0
    for i in students:
        srednya_grades += sum(i.grades[course]) / len(i.grades[course])
    return srednya_grades

def nadzirateli(lecturers, course):
    srednya_grades = 0
    for i in lecturers:
        srednya_grades += sum(i.lecturer_grade[course]) / len(i.lecturer_grade[course])
    return srednya_grades
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', "C++"]
student_bedolaga = Student('Anton', 'Fantikov', 'your_gender')
student_bedolaga.courses_in_progress += ['Python', "C++"]

cool__lecturer = Lecturer("Andre", "Rublev")
cool__lecturer.courses_attached.append("C++")
lecturer_diktator = Lecturer("Green", "Peace")
lecturer_diktator.courses_attached.append("C++")

cool_reviewer = Reviewer("Daniil", "Medwedev")
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(best_student, "Python", 10)
cool_reviewer.rate_hw(student_bedolaga, "Python", 3)
cool_reviewer.rate_hw(student_bedolaga, "Python", 3)
reviewer_armenin = Reviewer("Karen", "Khahanov")
reviewer_armenin.rate_hw(best_student, "Python", 10)
reviewer_armenin.rate_hw(best_student, "Python", 10)
reviewer_armenin.rate_hw(student_bedolaga, "Python", 3)
reviewer_armenin.rate_hw(student_bedolaga, "Python", 3)

best_student.rate_hw(cool__lecturer, "C++", 10)
best_student.rate_hw(lecturer_diktator, "C++", 7)

print(best_student.grades)
print(cool__lecturer.lecturer_grade)
print(lecturer_diktator.lecturer_grade)

print(cool_reviewer)

print(cool__lecturer)

print(best_student, "\n")

print(best_student == student_bedolaga)
print(best_student < student_bedolaga)
print(best_student > student_bedolaga)
print(best_student != student_bedolaga, "\n")

print(cool__lecturer == lecturer_diktator)
print(cool__lecturer < lecturer_diktator)
print(cool__lecturer > lecturer_diktator)
print(cool__lecturer != lecturer_diktator, "\n")

print(survivors([best_student, student_bedolaga], "Python"), "\n")

print(nadzirateli([cool__lecturer, lecturer_diktator], "C++"))