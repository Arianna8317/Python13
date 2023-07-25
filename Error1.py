class NegativeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Cтороны треугольника должны быть положительными числами! Вы указали {self.value}'
    
    
class Square:
    '''
    Класс прямоугольник создает квадрат, в случае, если задается тоько одна сторона 
    '''
    def __init__(self, a, b=None):
        
        if a <= 0:
            raise NegativeError(a)
        elif b <= 0:
            raise NegativeError(b)
        else:   
            self.a = a
            if b:
                self.b = b
            else:
                self.b = a

    def area(self):
        return self.a * self.b
    
    def perimetr(self):
        return 2 * (self.a + self.b)
    
    def __add__(self, other):
        return Square(self.a + other.a, self.b + other.b)
    
    def __sub__(self, other):
        if self.a - other.a < 0 or self.b - other.b < 0:
            raise ValueError
        return Square(self.a - other.a, self.b - other.b)
    
    def __repr__(self):
        return f"Длина = {self.a}, ширина = {self.b}"
    
    def __eq__(self, other):
        return self.area() == other.area()
                
    def __gt__(self, other):
        return self.area() > other.area()  
    
    def __ge__(self, other):
        return self.area() >= other.area()  

    def __lt__(self, other):
        return self.area() < other.area() 

    def __le__(self, other):
        return self.area() < other.area()  
         

print(Square.__doc__)
sq1 = Square(5, 2)
sq2 = Square(6, 4)
sq3 = sq1 + sq2
print(sq3)
print(f"Периметр {sq3.perimetr()}")
sq4 = sq2 - sq1
print(f"Площадь {sq4.area()}")
#print({sq1 - sq2})
print(sq1 == sq2)
print(sq1 > sq2)
print(sq1 < sq2) 
#sq4 = Square(-7)
sq5 = Square(5, -6) 