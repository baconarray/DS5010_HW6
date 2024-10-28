'''
Tyler Beaulieu
DS5010, Fall 2023
Homework 6, Problem 2
October 24, 2024
'''

class Animal:
    ''' Class: Animal
        Attributes: age, gender
        Methods: isMammal(), mate()'''
    
    def __init__(self, age: int, gender: str):
        self.age = age
        self.gender = gender

    def isMammal(self):
        print("It is a mammal.")

    def mate(self):
        print("Has no mate.")