class Course:
    def __init__(self, name, maxSize):
        self.name = name
        self.maxSize = maxSize
        self.students = []
    
    def isFull(self):
        return len(self.students) >= self.maxSize

    def addStudent(self, student):
        if not self.isFull():
            self.students.append(student)
            return True
        else:
            return False
    
    def __str__(self):
        string = self.name
        if self.students == 0:
            return string
        
        for student in self.students:
            string = string + r', ' + student
        
        return string

chem = Course('chemistry', 2)

chem.addStudent('bobo')
chem.addStudent('gary')


print(chem)