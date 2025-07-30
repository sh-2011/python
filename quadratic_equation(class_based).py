import math as mt
class quadratic_equation:
    def __init__(self,a,b,c):
        self.A = a
        self.B = b
        self.C = c
        self.calculate_delta = (self.B ** 2) - (4*self.A*self.C)
    def review_delta(self):
        self.Vertex = (-self.B) / (self.A * 2)
        if self.calculate_delta == 0:
            self.answer = self.Vertex
        elif self.calculate_delta > 0:
            self.answer = [((-self.B) + (mt.sqrt(self.calculate_delta))) / (self.A * 2) , ((-self.B) - (mt.sqrt(self.calculate_delta))) / (self.A * 2)]
        elif self.calculate_delta < 0:
            self.answer = None
        else:
            print('not found!!!')
    def return_var(self):
        print('Vertex:',self.Vertex,'answer:',self.answer,'delta:',self.calculate_delta)

test = quadratic_equation(7,4,-3)

test.review_delta()
test.return_var()
