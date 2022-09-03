# print(True, True, True == (True, True, True))

##time constraints

#warlus operator
# print(a:=10)

#Comprehensions or one-liners

# a= [1,2,3,4,5,6,7]
# b=[]
# for i in a:
#     if i==5:
#         break
#     b.append(i)
    
# print(b)


# b=[i for i in a if i!=5]
# print(b)

# a=input()
# for i in reversed(range(len(a))):
#     print(a[0:i])


#Type Hinting

# def fjjjj11(x:int,y:float) ->float:
#     return x+y

# print(fjjjj11(2,3))


#Classes in Python
# class A:
#     def __init__(self,a,b):
#         self.a=5
#         self.b=6

#     @classmethod
#     def method1(cls):
#         print("fhfhfh")
    
#     def method2(self):
#         print("hfhgfgfgh")

# obj=A()
# obj.method1()
# obj.method2()

#Encapsulation

#Why None came as output at end?
# class harsha:
#     a=10
#     def test(self):
#         print(self.a)


# o=harsha()
# print(o.a)
# print(o.test())



# class harsha:
#     __a=10
#     def test(self):
#         print(self.a)
#     def __has_access(self):
#         print(self.__a)
#     def has_access_inside(self):
#         self.__has_access()



# o=harsha()
# print(o.has_access_inside())

#polymorphism---->Method overloading(doesn't work)
#            ---->Method overriding


#Method overloading
# class A:
#     def m1(self,a):
#         print('m1')
#     def m1(self,a,b):
#         print('m2')

# o=A()
# o.m1(4,5)


# Method overriding

# class A:
#     def __init__(self,a):
#         self.a=40
#     def m1(self,b):
#         print(self.a)

# class B(A):
#     def m1(self,a,b):
#         print(a,b)
#     A.__super__()

# hhgffjjjjuj

































