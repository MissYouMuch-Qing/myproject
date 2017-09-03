class Student(object):
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def abs(self,a):
        if a=='c':
            print(self.name)
        elif a=='score':
            print(self.score)
        else:
            print("no params")


bart = Student('Bart Simpson', 59)
bart.abs('q')
print(bart.score)

hama = Student('hama', 0)
hama.abs('c')
print(hama.score)
