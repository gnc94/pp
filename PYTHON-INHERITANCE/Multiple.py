class marks1: 
    def m1(self, st1):
        self.st1 = st1

class marks2:
    def m2(self, st2):
        self.st2 = st2

class result(marks1, marks2):
    def r(self, st1, st2):
        self.res = st1 + st2
        print(self.res)

obj = result()
obj.r(72, 77)
