#Part 1
#class Student:
    ######def __init__(self, name, age):
        #####self.name = name
        ####self.age = age
###student1 = Student("Yuki", 15)
##student2 = Student("Satoshi", 10)

#print(student1.age)

# Part 2
class Student:
    def __init__(self,name, age, class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_
    def grade_average(self, score_1, score_2,score_3):
        x = (score_1+score_2+score_3) / 300 * 100
        return f"{self.name} : grade_average is {x}"
                
student1 = Student("Yu", 15, )

print(student1.grade_average(50,50,50))

# Part3
class Bird:

    num_of_birds = 0

    def __init__(self, name, wingspan):
        self.name = name  
        self.wingspan = wingspan 
        Bird.num_of_birds +=1

    def fly(self):
        print(f"{self.name} has a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"
    
class Owl(Bird):
    def __init__(self, name, wingspan, habitat):
        super().__init__(name,wingspan)
        self.habitat = habitat
    def hoot(self):
        print(f"{self.name}is hooting")
    def __str__(self):
        return super().__str__() + f"Habitat: {self.habitat}"    
class Dodo(Bird):
    def __init__(self, name, wingspan, extinct = True):
        super().__init__(name, wingspan)
        self.extinct = extinct
    def fly(self):
        print("Dodo's can't fly")
    def __str__(self):
        return super().__str__()+ f"Extinct = {self.extinct}"
    
bird1 = Bird("sparrow", 5)
owl1 = Owl("Barn Owl", 90, "Barn")
dodo1 = Dodo("Dodo",25)

bird1.fly()
print(bird1)

owl1.fly()
owl1.hoot()
print(owl1)

dodo1.fly()
print(dodo1)

