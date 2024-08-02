#Student information using OOP

class student:
    def __init__(self, subject, grade, first, last, parents):
        self.subject = subject
        self.grade = grade
        self.first = first
        self.last = last
        self.email = first + "." + last + "@chesterhillschool.com"
        self.parents = parents

    def fullname(self):
        return "{} {}".format(self.first, self.last)


student1=student("Art", "D", "Billy", "Eilish", "Mark Zucky")
student2=student("PDHPE", "C-", "Mark", "Wahlberg", "Elon Musky")

print(f"{student1.first} received a grade of {student1.grade} which was emailed to {student1.email}. There full name is {student1.fullname()} and parents {student1.parents}")