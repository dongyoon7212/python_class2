# fruits = ["orange", "apple", "banana"] # 문자열 리스트
# numbers = [6, 3, 1, 5] #숫자 리스트
# bools = [True, False, True, True] #불리언 리스트
#
# mixed_list = ["안녕하세요", 12, True]

# print(fruits[2][1])
# print(fruits[-2])
#
# fruits[1] = "cherry"
# print(fruits)

# numbers.append("hi") #마지막 자리에 요소 추가
# print(numbers)
# numbers.insert(1, 2) #특정 자리에 요소 추가
# print(numbers)

#print(numbers.pop())#리스트의 마지막 요소가 리턴된다.
#numbers.remove("hi")
# print(numbers)
#
# del numbers[4] #삭제
# print(numbers)
#
# print(len(mixed_list)) #리스트의 길이

#numbers.sort(reverse=True) #sort()작은순 옵션 reverse=True 큰순

# numbers.reverse() # 그냥 순서를 거꾸로
# print(numbers)

# fruits = "-".join(fruits)
# print(fruits)
#
# cart = []
#
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
# cart.append(input("추가할 상품 : "))
#
# print(cart)

#튜플
colors = ("red", "green", "black", "yellow") #변경 불가능
numbers = (1, 5, 3, 9, 1, 2)
bools = (True, False, True)
mixed_tuple = ("red", 1, True)

#a = ("first", ) #요소가 하나일때는 마지막 쉼표!!

print(colors[1])

#colors[1] = "yellow" #튜플은 변경불가능
print(numbers[0:2]) #슬라이싱 가능
print(numbers.count(1))
print(numbers.index(3))

a, b, c, d = colors
print(d)