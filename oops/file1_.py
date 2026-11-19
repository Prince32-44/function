class Money:
    def __init__(self, value):
        self. value = value

    def __add__(self, other):
        return Money(self.value + other.value)
    
    def __sub__(self, other):
        return Money(self.value - other.value)
    
    def __mul__(self, other):
        return Money(self.value * other.value)

    def __truediv__(self, other):
        return Money(self.value / other.value)
    
    def __str__(self):
        return f"Money: {self.value}"


m1 = Money(100)
m2 = Money(200)
m3=Money(300)
print(m1 + m2 + m3)  # This will raise an error because the '+' operator is not defined for Money objects

