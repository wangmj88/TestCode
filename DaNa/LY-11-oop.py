class Teacher():
    name = 'dana'
    age = 19

    def say(self):
        self.name = 'yaona'
        self.age = 17
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))

    def sayAgain(self):
        print(__class__.age)
        print(__class__.name)
        print("Hello,nice to see you again")

yueyue = Teacher()
yueyue.say()
print('*'*100)
yueyue.sayAgain()
'''
    My name is yaona
    My age is 17
    ****************************************************************************************************
    19
    dana
    Hello,nice to see you again
'''

class A():
    name ='liuying'
    age = 18

    def __init__(self):
        self.name ='aaaa'
        self.age = 20

    def say(self):
        print(self.name)
        print(self.age)

    def sayAgain(self):
        print(__class__.name)
        print(__class__.age)
a = A()
a.say()
print('*'*100)
a.sayAgain()