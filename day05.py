#대입 연산자
#x = 10 # 대입
#x += 10 # 더하고 대입(할당) x = x + 10
#x -= 5 # 빼고 대입(할당) x = x - 5
#x *= 3 # 곱하고 대입(할당) x = x * 3
#x /= 2 # 나누고(몫이 실수) 대입(할당) x = x / 2
#x //= 2 # 나누고(몫이 정수) 대입(할당) x = x // 2
#print(x)
from doctest import script_from_examples

# 비교연산자
x = 10
y = 20
z = 10
print(x == y) #같다
print(x != z) #같지 않다
print(x > y) #왼쪽기준 오른쪽보다 크다
print(x < y) #왼쪽기준 오른쪽보다 작다
print(x >= z) #크거나 같다
print(x <= y) #작거나 같다

#논리연산자
# a = True
# b = False
# print(a and b)
# print(a or (a and b))
# print(not a)
# print(not a and b)

#조건연산자 (삼항연산자)
a = 10
b = 20
max_value = a if a > b else b
print(max_value)
if a > b:
    max_value = a
else:
    max_value = b
score = 85
grade = "A" if score >= 90 else ("B" if score >= 80 else "C")
print(grade)
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")