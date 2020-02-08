class Employee:

    raiseAmount= 1.04
    numberOfEmployees = 0

    def __init__(self,first,last,pay):
        Employee.numberOfEmployees += 1
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{last.lower()}.{first.lower()}@company.com'
        self.employeeNumber = Employee.numberOfEmployees


    def fullName(self):
        return f'{self.first} {self.last}'

    def payRaise(self):
        self.pay = Employee.raiseAmount * self.pay ## Using 'Employee.raiseAmount' uses the Class set variable as opposed to the instances(employee1) variable, which can be set independently to the Class variable.


    @classmethod
    def changeRaiseAmount(cls,amount):
        cls.raiseAmount = amount

    @classmethod
    def nameFromString(cls,string): ## Takes in a string that is formatted like this: 'Jack-Kibble-50000'
        first, last, pay = string.split('-')
        return cls(first, last, int(pay)) ## It uses the class in the method to create a new employee from a string that is passed to it.
    @staticmethod
    def isWeekDay(day):
        if day.weekday() == 5 or day.weekday() == 6: ## Monday = 0 Tuesday = 1 ect.
            return False
        else:
            return True
employee1 = Employee('Jack','Kibble',50000) ## Can also say first='Jack'
employee2 = Employee('Amy', 'Broad', 50000)

## employee1.raiseAmount = 1.05 ## This does not affect the pay rise amount because the method uses the class set variable and not the instances.
## employeeString = 'Steven-Kibble-50000' ## This is the string format needed for the method to work.
## employee3 = Employee.nameFromString(employeeString)

import datetime
date = datetime.date(2016,12,17)
print(Employee.isWeekDay(date))