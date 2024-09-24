class Defence:
    def type(self):
        print('Security')

class Army(Defence):
    def head(self):
        print('Chief of Army Staff')

class General(Army):
    def commands(self):
        print('Armed force')

obj = General()
obj.type()
obj.head()
obj.commands()
