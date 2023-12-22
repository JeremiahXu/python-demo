#!/usr/bin/env python3

# -*- coding: utf-8 -*-



# class Animal(object):
#     def run(self):
#         print('Animal is running...')



# class Dog(Animal):

#     def run(self):

#         print('Dog is running...')



# class Cat(Animal):

#     def run(self):

#         print('Cat is running...')


# # Here is important point.
# def run_twice(animal):

#     animal.run()

#     animal.run()



# a = Animal()

# d = Dog()

# c = Cat()



# print('a is Animal?', isinstance(a, Animal))

# print('a is Dog?', isinstance(a, Dog))

# print('a is Cat?', isinstance(a, Cat))



# print('d is Animal?', isinstance(d, Animal))

# print('d is Dog?', isinstance(d, Dog))

# print('d is Cat?', isinstance(d, Cat))




# # Here is important point.
# def BiteBone(Dog):
#     print(Dog.__str__(),' is biting bone...')


# 只需要保证传入的对象有一个run()方法就可以了。
# class Timer(object):
#     def run(self):
#         print('Start...')

# Another instance
class Duck:
    def quack(self): 
        print("呱呱呱！")
    def feathers(self): 
        print("这个鸭子拥有灰白灰白的羽毛。")
 
class Person:
    def quack(self):
        print("你才是鸭子你们全家人是鸭子！")
    def feathers(self): 
        print("这个人穿着一件鸭绒大衣。")
 
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
 
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
 
game()

    