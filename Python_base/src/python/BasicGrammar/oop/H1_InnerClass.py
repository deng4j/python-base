"""
内部类
"""


class Person:
    name = '张三'

    def work1(self):
        Person.__Leg().work()

    class __Leg:

        def work(self):
            print('__Leg 私有类')

    @classmethod
    def work(self):
        print(' Person work ')

    class Hand:

        def work(self):
            print(Person.name + ' Hand work ')
            Person.work()


Person.Hand().work()

person = Person()
person.Hand().work()

person.work1()
