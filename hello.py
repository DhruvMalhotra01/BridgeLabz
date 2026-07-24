# class Student:

#     def __init__(self,name):
#         self.name=name

#     def display(self):
#         print(self.name)

# s=Student("Dhruv")
# s.display()


# nums = [1, 2, 3, 4, 5]

# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1


# for num in nums:
#     print(num)

# for i in range(len(nums)):
#     print(i , nums[i])

# for i , num in enumerate(nums):
#     print(i , num)

# square = []
# for i in range(5):
#     square.append(i**2)

# square = [i**2 for i in range(5)]

# print(square)

a = 10
b  = 20
# temp = a
# a = b 
# b = temp

# a, b = b , a

# print(a,b)

x = 4

# if x == 1 or x == 2 or x == 3:

# if x in [1,3,2]:
#     print("find the number")
# else:
#     print("not found")

def my_func(x):
    def wrapper():
        print("BEFORe")
        x()
        print("AFTER")
    return wrapper

@my_func
def greet():
    print("hello")

greet()
