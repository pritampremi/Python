class Chocolate:
    def __init__(self,b,cp,sp):
        self.brand=b
        self.cocoa_percentage=cp
        self.sugar_percentage=sp
        
    def display(self):
        print('Brand Name:',self.brand)
        print('Cocoa Percentage:',self.cocoa_percentage)
        print('Sugar Percentage:',self.sugar_percentage)

class DarkChocolate(Chocolate):
    def __init__(self,b,cp,sp,bl):
        super().__init__(b,cp,sp)
        self.bitterness_level=bl

    def display(self):
        print('Dark Chocolate:')
        super().display()
        print('Bitterness Level:',self.bitterness_level)

class MilkChocolate(Chocolate):
    def __init__(self,b,cp,sp,ms):
        super().__init__(b,cp,sp)
        self.milk_solids=ms

    def display(self):
        print('Milk Chocolate:')
        super().display()
        print('Milk Content:',self.milk_solids)

amul=DarkChocolate('Amul',84,2,72)
amul.display()
print()
cadbury=MilkChocolate('Cadbury Dairy Milk',65,24,25)
cadbury.display()

    
