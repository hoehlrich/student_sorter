# -----------------------------------------------------------
# seperates students into coureses based off of their preferences
#
# Henry Oehlrich, Raleigh NC, United States
# Still in development
# email henryoeh@gmail.com
# -----------------------------------------------------------

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
        # return wether or not the course is full
        return len(self.students) >= self.maxsize

    def add_student(self, student):
        # add the student to the course if it is not full
        if not self.is_full() and student not in self.students:
            self.students.append(student)
            student.courses.append(self)
            return True
        else:
            return False
    
    def __str__(self):
        # create the string with the students and the name of the course
        string = self.name

        # if there are no students in the course, return the course name
        if self.students == 0:
            return string
        
        for student in self.students:
            string = string + r', ' + student.name
        
        # replace the first comman with a colon
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
    
    def assign_course(self):
        for course in self.course_request:
            if not course.is_full():
                self.course_request.remove(course)
                return self.add_course(course)

        for course in Course.courses:
            if not course.is_full():
                return self.add_course(course)
        
        return False
                

    def __str__(self):
        string = self.name

        if self.courses == 0:
            return string
        
        for course in self.courses:
            string = string + r', ' + course.name
        
        string = string.replace(',', ':', 1)

        return string

chem = Course('chemistry', 3)
hx = Course('history', 3)
sci = Course('science', 3)
ela = Course('english', 3)

s1 = Student('bobo', [ela, hx, sci])
s2 = Student('marvin', [hx, sci, ela])
s3 = Student('henry', [sci, ela, chem])

for i in range(3):
    s1.assign_course()
    s2.assign_course()
    s3.assign_course()

for course in Course.courses:
    print(course)

for student in Student.students:
    print(student)

print()