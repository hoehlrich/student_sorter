# -----------------------------------------------------------
# seperates students into coureses based off of their preferences
#
# Henry Oehlrich, Raleigh NC, United States
# Still in development
# email henryoeh@gmail.com
# -----------------------------------------------------------

import random

class Course:
    '''Course Class'''

    courses = []

    def __init__(self, name, maxsize):
        self.name = name
        self.maxsize = maxsize
        self.students = []
        Course.courses.append(self)
    
    def get_name(self):
        return self.name
    
    def get_maxsize(self):
        return self.maxsize

    def is_full(self):
        return len(self.students) >= self.maxsize

    def add_student(self, student):
        if not self.is_full() and student not in self.students:
            self.students.append(student)
            student.courses.append(self)
            return True
        else:
            return False
    
    def __str__(self):
        string = self.name

        if self.students == 0:
            return string
        
        for student in self.students:
            string = string + r', ' + student.name
        
        string = string.replace(',', ':', 1)

        return string

class Student:
    '''Student Class'''

    students = []
    def __init__(self, name, course_request):
        self.name = name
        self.course_request = course_request
        self.courses = []
        Student.students.append(self)

    def add_course(self, course):
        self.courses.append(course)
        course.students.append(self)
        return self.courses
    
    def get_courses(self):
        return self.courses
    
    def assign_course(self, period):
        for course in self.course_request:
            if len(course.students) < (course.maxsize *(period.period_num/len(Period.periods))) and course in period.courses:
                self.course_request.remove(course)
                return self.add_course(course)

        for course in Course.courses:
            if not course.is_full() and course not in self.courses:
                return self.add_course(course)
        
        return False
                

    def __str__(self):
        string = self.name

        if self.courses == 0:
            return string
        
        for course in self.courses:
            string = string + r', ' + course.name
        
        return string.replace(',', ':', 1)

class Period:
    '''Period Class'''

    periods = []
    def __init__(self, period_num, courses):
        self.period_num = period_num
        self.courses = courses
        Period.periods.append(self)

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        string = str(self.period_num)

        for course in self.courses:
            string = string +r', ' + course.name
        
        return string.replace(',', ':', 1)

class Teacher:
    '''Teacher Class'''

    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    
    def add_course(self, course):
        self.courses.append(course)

chem = Course('chemistry', 3)
hx = Course('history', 3)
sci = Course('science', 3)
ela = Course('english', 3)
ocean = Course('oceanography', 3)

s1 = Student('bobo', [ela, hx, sci])
s2 = Student('marvin', [hx, sci, ela])
s3 = Student('henry', [sci, ela, chem])
s4 = Student('z', [chem, hx, ela])

p1 = Period(1, [ela, hx, chem])
p2 = Period(2, [ela, hx, sci])
p3 = Period(3, [chem, ela, sci])

for student in Student.students:
    for period in Period.periods:
        student.assign_course(period)

for course in Course.courses:
    print(course)

print()

for student in Student.students:
    print(student)

print()

for period in Period.periods:
    print(period)