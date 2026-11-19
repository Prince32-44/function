class Money:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Money(self.value + other.value)

    def __str__(self):
        return f"Money: {self.value}"
print(5.__add__(10))  # This will print 15, as it uses the built-in __add__ method for integers
m1 = Money(100)
m2 = Money(200)
print(m1 + m2)  # This will print "Money: 300", as it uses the __add__ method for Money objects