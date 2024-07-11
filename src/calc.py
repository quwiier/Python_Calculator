from logic import addition, subtraction, multiplication, division


class Calc:
    def __init__(self):
        self.total_expression = 0

    def run(self):
        print(self.total_expression)
        user_input = input()
        while user_input != "exit":
            match user_input:
                case "+":
                    self.total_expression = addition.Addiction.add(self.total_expression, int(input()))
                case "-":
                    self.total_expression = subtraction.Subtraction.sub(self.total_expression, int(input()))
                case "*":
                    self.total_expression = multiplication.Multiplication.multiply(self.total_expression,
                                                                                   int(input()))
                case "/":
                    self.total_expression = division.Division.division(self.total_expression, int(input()))
                case "c":
                    self.total_expression = 0
            print(self.total_expression)
            user_input = input()
