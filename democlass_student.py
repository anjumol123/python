class student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark
    def printname(self):
        print(self.name,self.age,self.mark)
x=student("a","15",50)
x.printname()


