class Multiplication:
    def __init__(self):
        pass

    def valid_factor1(factor: int | float) -> bool:
        if factor == 0:
            return False
        else:
            return True

    @staticmethod
    def multiply(factor1: int | float, factor2: int | float) -> int | float:
        if Multiplication.valid_factor1(factor1):
            return factor1 * factor2
        else:
            return factor2
