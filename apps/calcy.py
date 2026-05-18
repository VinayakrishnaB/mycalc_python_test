class calcy:
    def add(self, a, b):
        return (a + b)
    
    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        if (b == 0):
            raise ValueError("cannot divide by zero")
        
        return a / b
    
if __name__ == "__main__":
    calc = calcy()
    print("Additions is: ", calc.add(5,10))
    print(f"Substraction is: ", calc.sub(20, 10))    
    print(f"multiplicaion is: ", calc.multiply(20, 10))
    print(f"Division is: ", calc.divide(20, 4))


