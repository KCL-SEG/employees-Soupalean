"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    # This is very janky :(
    def __init__(self, name, salary=None, hourly=None, hours=None, bonus=None, commissionRate=None, commissions=None):
        self.name = name
        self.salary = salary
        self.hourly = hourly
        self.hours = hours
        self.bonus = bonus
        self.commissionRate = commissionRate
        self.commissions = commissions
        self.total = 0
        self.description = ''

    def get_pay(self):
        if self.bonus:
            if self.salary:
                self.total = self.bonus + self.salary
                self.description = f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}.  Their total pay is {self.total}."
                return self.total
            else:
                self.total = self.bonus + (self.hours * self.hourly)
                self.description = f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.total}."
                return self.total
        elif self.commissions:
            if self.salary:
                self.total = (self.commissionRate * self.commissions) + self.salary
                self.description = f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.commissions} contract(s) at {self.commissionRate}/contract.  Their total pay is {self.total}."
                return self.total
            else:
                self.total = (self.commissionRate * self.commissions) + (self.hours * self.hourly)
                self.description = f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour and receives a commission for {self.commissions} contract(s) at {self.commissionRate}/contract.  Their total pay is {self.total}."
                return self.total
        else:
            if self.salary:
                self.total = self.salary
                self.description = f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.total}."
                return self.total
            else:
                self.total = (self.hours * self.hourly)
                self.description = f"{self.name} works on a contract of {self.hours} hours at {self.hourly}/hour.  Their total pay is {self.total}."
                return self.total

    def __str__(self):
        return self.description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', None, 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, None, None, None, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', None, 25, 150, None, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, None, None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', None, 30, 120, 600)
