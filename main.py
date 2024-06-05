class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def chromosomeNumber(self):
        return (self.x + self.y) / 2

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def childChromoNumber(self):
        return self.chromosomeNumber() / 2
    
John = Parent(23, 23)
Phil = Child(23, 23)
print(John.chromosomeNumber())
print(Phil.childChromoNumber())