class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Zero division error"
        else:
            return x / y


print(Calculator.add(1, 2))  # 3
print(Calculator.subtract(1, 2))  # -1
print(Calculator.multiply(1, 2))  # 2
print(Calculator.divide(1, 2))  # 0.5
