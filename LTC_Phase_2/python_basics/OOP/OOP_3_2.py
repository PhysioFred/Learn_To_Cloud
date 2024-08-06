#class variables vs instance variables
#__dict__
#vocab: hardcode, namespace, instantiated
#instance amount can change vs class amount is global
#init meth runs everytime you call the class, thus can make counter


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
        self.pay = int(self.pay * employee_info.raise_amount)
    
    # #hardcoded the raise amount, which is not what we want.
    # def apply_raise(self):
    #     self.pay = int(self.pay * 1.04)


print(f"employee count = {employee_info.employee_count}")   
print()

emp_1=employee_info("Fred", "Dejrangsi", 66000)
emp_2=employee_info("Matilda", "May", 100000)

print(f"pay before raise {emp_1.pay}")
emp_1.apply_raise()
print(f"pay after a raise {emp_1.pay}")


print()
print(f"employee count = {employee_info.employee_count}") 
print()

#used to find more information on instance or class variables
print("--------------------")
print(emp_1.__dict__)
print("--------------------")
print(employee_info.__dict__)

#trying to use method to make a raise to emp_1
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


            