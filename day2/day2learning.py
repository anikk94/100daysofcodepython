# day 2


# task 1

# # subscripting
# print("hello")
# print("hello"[0])

# s = "hello"
# print(s[0])
# print(s[4])

# print(s[-1])
# print(s[-2])


# # concatenation
# print("123" + "345")

# # integer = wholenumber
# print(123 + 345)

# print(123456)
# # if you have commas in your number
# print(123_456)

# # float
# print(3.14159)
# print(123_456.789)

# # bool
# print(True)
# print(False)


# # quiz


# task2

# error -> print(len(12345))
print(len("12345"))
print(len("Hello"))

# checking type of a variable

# primitive datatypes in python
print(type("Hello"))

print(type(123))

print(type(True))

print(type(123_456.789))

# type-casting

int("123")

print("123" + "456")

print(int("123") + int("456"))

# error
# ValueError: invalid literal for int() with base 10: 'abc'
# int("abc")

# challenge
# fix this line

# print("Number of letters in your name: " + len(input("Enter your name")))

# answer

# print("Number of letters in your name: " + str(len(input("Enter your name:\n>> "))))

# name = input("Enter your name:\n>> ")
# name_length = len(name)

# print("name_length", type(name_length))
# print("Number of letters in your name: " + str(name_length))

# task 3

# what is the output of this code

print(3 * 3 + 3 / 3 - 3) # 7

# how to change this line to make the output 3.0

print(3 + 3 * 3 / 3 - 3)

print((3 * (3 + 3) / 3 - 3))

# task 4

# bmi
height = 1.73

weight = 90

bmi = weight / (height ** 2)

print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 2 ))

# assignment operator
# score += 1
# score =-/*= 1


# f-string

score = 0
height = 1.8
is_winning = True

print(f"your score: {score} your height is: {height} you are winning: {is_winning}")

# quiz on numbers and printing