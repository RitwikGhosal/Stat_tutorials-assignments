class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay): #when we create a method in a class they receive the instance as the first argument automatically that is the self here
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod #decorator here it is used to convert a regular method to classmethod taking the class as the first argument   
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last,pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in  self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

#class is a blue print for the instances
#emp_1 = Employee() is an instance of the class, that is employee object

#see about method resolution order

dev_1 = Developer('Corey','Schafer',50000,'python')
dev_2 = Developer('Test','User',60000,'Java')

mgr_1 = Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.email)

mgr_1.print_emps()
#print(dev_1.email)
#print(dev_1.prog_lang)


'''
import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

Employee.set_raise_amt(1.05)

#print(Employee.num_of_emps)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-40000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee.from_string(emp_str_1)
#new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)
'''