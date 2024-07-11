class Division:
    def __init__(self):
        pass

    def valid_divisor(divisor: int | float) -> bool:
        if divisor == 0:
            return False
        else:
            return True

    @staticmethod
    def division(dividend: int | float, divisor: int | float) -> float:
        if Division.valid_divisor(divisor):
            return dividend / divisor
        else:
            print("Cannot divide by zero")
            return dividend


