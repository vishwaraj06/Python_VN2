
print("----Without class variables---------")
class Employee:
    # instance variables - each object has their own data
    # Here problem is comp name is sharable to all employees(objects)
    def __init__(self, eid, name, sal, comp):
        self.eid = eid
        self.name = name
        self.sal = sal
        self.comp = comp

    def get_edata(self):
        print("Employee information :", self.eid, self.name, self.sal, self.comp)

madhu = Employee(100, 'Madhu N', 15000, 'ORACLE SERVICES')
madhu.get_edata()
dilip = Employee(101, 'Dilip B', 25000, 'ORACLE SERVICES')
dilip.get_edata()
'''
A class-level variable (called "static" in other languages) is owned by the class, 
and shared by all instances of the class. 
A instance variable is part of by each distinct instance of the class.
Instance attributes are those attributes that are not shared by objects.
Every object has its own copy of the instance attribute.
'''
print("----With class variables---------")
class Employee:

    comp = 'ORACLE SERVICES'  # class variable, this is sharable to all objects
    dept = 'hr'
    def __init__(self, eid, name, sal):  # local variables
        self.eid = eid   # LHS instance variables
        self.name = name
        self.sal = sal

    def get_edata(self):  # instance method
        print("Employee information :", self.eid, self.name, self.sal, Employee.comp, Employee.dept) # This is correct
        print("Employee information :", self.eid, self.name, self.sal, self.comp, self.dept)


madhu = Employee(100, 'Madhu N', 10000)
madhu.get_edata()  # obj.methodname()  ==> Employee.get_edata(madhu)


akhil = Employee(101, 'Akhil Kumar', 15000)
akhil.get_edata()  # Employee.get_edata(akhil)
