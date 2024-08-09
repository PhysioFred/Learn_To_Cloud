#class variables vs instance variables
#__dict__
#vocab: hardcode, namespace, instantiated
#instance amount can change vs class amount is global
#init meth runs everytime you call the class, thus can make counter


#classmethods and staticmethods
#alternative constructor
#

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
        employee_info.set_raise_amt = amount


print(f"employee count = {employee_info.employee_count}") 
print(f"employee standard raise amount {employee_info.raise_amount}")  
print()

emp_1=employee_info("Fred", "Dejrangsi", 66000)
emp_2=employee_info("Matilda", "May", 100000)

emp_1.raise_amount = 1.06

print("--------------------")
print(emp_1.__dict__)
print("--------------------")

print(f"employee 1 raise amount {emp_1.raise_amount}")
print(f"pay before raise {emp_1.pay}")
emp_1.apply_raise()
print(f"pay after a raise {emp_1.pay}")
print()

print(f"employee 1 raise amount {emp_2.raise_amount}")
print(f"pay before raise {emp_2.pay}")
print(f"pay after a raise {emp_2.pay}")


print()
print(f"employee count = {employee_info.employee_count}") 
print()

#used to find more information on instance or class variables

print(employee_info.__dict__)

#trying to use method to make a raise to emp_1
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


            


            