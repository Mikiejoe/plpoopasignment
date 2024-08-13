class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f'Hello, my name is {self.name}, I am a {self.gender} aged {self.age} nice to meet you..')
        

person = Person("Michael", 22,"male")
person.introduce()