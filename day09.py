#사용자 정의 함수

#기본적인 사용자 정의 함수
# def func1():
#     print("Hello World")
#
# func1()
# func1()
# func1()

# def plus():
#     a = 2
#     b = 3
#     print(a + b)
#
# plus()

#매개변수가 있는 사용자 정의 함수
# def hello(name):
#     print(f"안녕하세요 {name}입니다.")
#
# hello("홍길동")
#
# def plus(x, y):
#     print(x + y)
#
# plus(5, 6)

# def hello(name="홍길동"):
#     print(f"안녕하세요 {name}입니다.")
#
# hello()
# hello("이동윤")

# def introduce(name, age):
#     print(f"제 이름은 {name}이고 나이는 {age}입니다.")
#
# # introduce(27, "이동윤")
# introduce(age=27, name="이동윤")

#리턴값이 있는 사용자 정의 함수

def plus(x, y):
    return x + y

result = plus(1, 2)
print(result)
print(plus(1, 2))

# def multiple_seven(num):
#     return num * 7
#
# print(multiple_seven(3))
# print(multiple_seven(100))

# def check_divide_seven(num):
#     if num % 7 == 0:
#         return True
#     else:
#         return False
#
# print(check_divide_seven(14))
# print(check_divide_seven(15))

# def factorial(num):
#     sum = 1
#
#     for n in range(num):
#         print(f"n = {n}")
#         sum = sum * (n + 1)
#         print(f"sum = {sum}")
#     return sum
#
# print(factorial(7))

# def cal_average(scores):
#     sum = 0
#
#     for score in scores:
#         sum += score
#
#     return sum / len(scores)
#
# score_list1 = [55, 70, 100]
# score_list2 = [100, 99, 88]
# score_list3 = [80, 70, 60]
#
# print(cal_average(score_list1))
# print(cal_average(score_list2))
# print(cal_average(score_list3))

#콜백함수
#함수를 매개변수로 전달하여 필요할 때 호출하도록 하는 개념
#어떤 함수가 실행되는 동안 미리 정의된 다른 함수를 호출하여 실행하는 역할

def calculator(x, y, operation):
    return operation(x, y)

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    return x / y

print(calculator(8, 4, plus))
print(calculator(8, 4, minus))
print(calculator(8, 4, multiple))
print(calculator(8, 4, divide))
# import time
#
# def timer(pause_second, callback):
#     print(f"{pause_second}초 타이머가 시작되었습니다")
#     print(f"{pause_second}초 뒤에 함수가 실행됩니다.")
#
#     time.sleep(pause_second)
#
#     callback()
#     print("타이머가 종료되었습니다.")
#
# def hello():
#     print("안녕")
#
# timer(5, hello)
#

#lambda함수(익명함수, 미시함수)
#특정 범위 내에서만 사용되거나 호출되는 횟수가 한 번인 경우에 매우 유용
#lambda 매개변수1, 매개변수2, ...: 함수 내부 코드

def plus(x, y):
    return x + y

print(plus(4, 5))

add_lambda = lambda x, y: x + y
print(add_lambda(4, 5))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map_result = map(lambda x: x * 2, numbers)
# list_result = list(map_result)
# print(list_result)

parity = lambda x: "짝수" if x % 2 == 0 else "홀수"

print(parity(2))

#1.두 수를 입력받고 두 수의 합을 출력하는 함수
# a = int(input("첫번째 숫자 : "))
# b = int(input("두번째 숫자 : "))
#
# def add_func(x, y):
#     print(x + y)
#
# add_func(a, b)

#숫자 하나를 입력받고 해당 숫자가 짝수이면
#짝수를 출력하고 홀수이면 홀수를 출력하는 함수
# a = int(input("숫자 : "))
#
# def 홀짝(아무숫자):
#     if 아무숫자 % 2 ==0 :
#         print("짝수")
#     else:
#         print("홀수")
#
# 홀짝(a)



