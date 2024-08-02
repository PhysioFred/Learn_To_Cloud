
class employee_info:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first  + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = employee_info("Fred", "Dejrangsi", 66000)
emp_2 = employee_info("Matilda", "May", 100000)


print(emp_2.email)
print()
print(emp_1.fullname())
            