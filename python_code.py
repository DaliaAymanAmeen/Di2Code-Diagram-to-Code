class Person:
   def __init__(self):
       self.age = 0

   def get_age(self):
       # please note that the return value is int
       pass

class Student(Person):
   def __init__(self):
       self.id = ""

   def get_gpa(self):
       # please note that the return value is float
       pass

class Professor(Person):
   def __init__(self):
       self.title = ""

   def teach(self):
       # please note that the return value is void
       pass
