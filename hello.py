class main:
    self.list=[]
    def __init__(self) -> None:
        self.list.append(1)
    def print(self, mes = 'test'):
        print("you used the object")
        return self.list
    

m = main()
print(m.print())

