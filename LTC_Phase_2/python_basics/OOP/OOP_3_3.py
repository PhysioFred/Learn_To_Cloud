#classmethods and staticmethods
#alternative constructor

class employee_info:
    #class variable
    raise_amount = 1.04
    employee_count = 0

    def __init__(self, first, last, pay): #runs everytime we make a new employee
        #instance varialbe
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first  + "." + last + "@company.com"
        
        employee_info.employee_count += 1
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #changed self.raise_amount (instance) from employee_info.raise_amount (class)
    
    # #hardcoded the raise amount, which is not what we want.
    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)

    @classmethod
    def set_raise_amt(cls, amount):
        employee_info.raise_amount = amount

#employee count and set raise amount 
print(f"employee count = {employee_info.employee_count}") 
print(f"before employee standard raise amount {employee_info.raise_amount}")  
print()

#employee list and initialization
emp_1=employee_info("Fred", "Dejrangsi", 66000)
emp_2=employee_info("Matilda", "May", 100000)

#peak into class attritbutes
print("--------------------")
print(emp_1.__dict__)
print(emp_2.__dict__)
print("--------------------")

#spacing
print(""" 
      BEFORE RAISE AMOUNT""")

#employee 1 pre raise
print(f"employee 1 raise amount {emp_1.raise_amount}")
print(f"pay before raise {emp_1.pay}")

#employee 2 pre raise
print(f"employee 2 raise amount {emp_2.raise_amount}")
print(f"pay before raise {emp_2.pay}")


#increase pay
emp_1.raise_amount = 1.06
employee_info.set_raise_amt(1.07)


#spacing
print("""
      AFTER RAISE AMOUNT""")

#employee 1 after raise
print(f"employee 1 raise amount after raise {emp_1.raise_amount}")
print(f"pay after raise {emp_1.pay}")

#employee 2 after raise
print(f"employee 2 raise amount after raise {emp_2.raise_amount}")
print(f"pay after raise {emp_2.pay}")

#spacing
print("""
      """)

#peak into class attritbutes
print("--------------------")
print(emp_1.__dict__)
print(emp_2.__dict__)
print("--------------------")

#no. of emplyoees after being instantiated
print()
print(f"employee count = {employee_info.employee_count}") 
