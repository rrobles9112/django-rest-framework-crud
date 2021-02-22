from django.db import models


class MetaCount(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super(MetaCount, cls).__new__(cls, name, bases, attrs)
        new_cls.count = 0
        return new_cls


class Person(metaclass=MetaCount):

    def __init__(self, name, lastname, age, address):
        self.__name = name
        self.age = age
        self.address = address
        self.__lastname = lastname
        type(self).count += 1
        # self.count += 2 creates an *instance* variable

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newvalue):
        self.__name = newvalue

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, newvalue):
        self.__lastname = newvalue

    def get_fullname(self):
        return f"{self.__lastname} {self.__name}"


class Employee(Person, metaclass=MetaCount):
    employee_code = models.CharField(max_length=100)
    salary_per_hour = models.CharField(max_length=100)
    start_data = models.IntegerField()
    departament = models.DateTimeField(auto_now_add=True)  # When it was create
    updated_at = models.DateTimeField(auto_now=True)  # When i was update

    def __init__(self, employee_code, salary_per_hour, start_data, departament):
        Person.__base__.__init__(self)
        self.employee_code = employee_code
        self.salary_per_hour = salary_per_hour
        self.start_data = start_data
        self.departament = departament
        type(self).count += 1
