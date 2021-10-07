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
    course_names = []

    def __init__(self, name, maxsize):
        self.name = name
        self.maxsize = maxsize
        self.students = []
        Course.courses.append(self)
        Course.course_names.append(name)
    
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
        self.courses = []
        Student.students.append(self)
        self.course_request_orig = course_request
        for course in course_request:
            course_request[course_request.index(course)] = Course.courses[Course.course_names.index(course)]
        self.course_request = course_request

    def add_course(self, course):
        self.courses.append(course)
        course.students.append(self)
        return self.courses
    
    def get_courses(self):
        courses = []
        for course in self.courses:
            courses.append(course.name)
        return courses
    
    def assign_course(self, period):
        for course in self.course_request:
            if len(course.students) < (course.maxsize * (period.period_num/len(Period.periods))) and course in period.courses and course not in self.courses:
                self.course_request.remove(course)
                return self.add_course(course)

        for course in Course.courses:
            if len(course.students) < (course.maxsize * (period.period_num/len(Period.periods))) and course in period.courses and course not in self.courses:
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
        Period.periods.append(self)
        for course in courses:
            courses[courses.index(course)] = Course.courses[Course.course_names.index(course)]
        self.courses = courses

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        string = str(self.period_num)

        for course in self.courses:
            string = string +r', ' + course.name
        
        return string.replace(',', ':', 1)

# Read from file
courses = open('courses.txt', 'r')

courses = courses.read()  # Read the file as a string

courses = courses.split('\n')   # Split the file at every line

for i in range(len(courses)):
    courses[i] = courses[i].split(' ')
    courses[i][1] = int(courses[i][1])

students = open('students.txt', 'r')

students = students.read()  # Read the file as a string

students = students.split('\n')

for i in range(len(students)):
    students[i] = str(students[i]).split('\t')

for i in range(len(students)):
    students[i] = [students[i][0], students[i][1:len(students[i])]]
    random.shuffle(students[i][1])

periods = open('periods.txt', 'r')

periods = periods.read()  # Read the file as a string

periods = periods.split('\n')

for i in range(len(periods)):
    periods[i] = str(periods[i]).split('\t')

for i in range(len(periods)):
    periods[i] = [int(periods[i][0]), periods[i][1:len(periods[i])]]

# Define objs
for course in courses:
    Course(course[0], course[1])

for student in students:
    Student(student[0], student[1])

for period in periods:
    Period(period[0], period[1])

# main

# Assign courses
for period in Period.periods:
    students = Student.students
    random.shuffle(students)
    for student in students:
        student.assign_course(period)

# Print courses and the students in them
for course in Course.courses:
    print(course)

print()

# Print students and the courses they have as well as how many courses they got that they asked for
for student in Student.students:
    print(student, len(Period.periods) - len(student.course_request))

print()

# Print period and all classes assigned in that period
for i in range(len(Period.periods)):
    period_classes = []
    for student in Student.students:
        period_classes.append(student.get_courses()[i])
    print('Period', (str(i + 1) + ':'), period_classes)