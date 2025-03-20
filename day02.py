# print("Hello World")
#
name = "이동윤"
age = 27.15
#
# "제 이름은 ____ 입니다."
# print("제 이름은" + name + "입니다.") #띄어쓰기 X
# print("제 이름은", name, "입니다.") #띄어쓰기 O
#
# "제 나이는 __ 입니다."
print("제 나이는", age, "입니다.")
print("제 나이는 {} 이고 이름은 {} 입니다.".format(age, name))
print("제 나이는 {a} 이고 이름은 {b} 입니다.".format(a=27, b="이동윤"))
print(f"제 나이는 {age} 이고 이름은 {name} 입니다.") #f-string 방식
print("제 나이는 %s 입니다." % age) # 문자열로 들어간다
print("제 나이는 %d 입니다." % age) # 모든 숫자가 정수로 들어간다
print(f"제 나이는 %d 이고 이름은 %s 입니다." % (age, name)) #f-string 방식
print("제 지분은 %d%% 입니다." % 2)
#
# print("%10.2f" % 3.141565) #%"자릿수"."몇번째소수점"f
#
#
#입력
#input()
email = input("이메일 : ")
hobby = input("취미 : ")
age = int(float(input("나이 : ")))
#
# print(f"제 이메일은 {email}, 제 취미는  {hobby}, 나이는 {age}")
from curses.ascii import isupper

a = "Life is too short, You need Python"
print(a[2:10:2])

# date = "20250218sunny"
# date2 = "20260505cloudy"

#연도, 월, 일, 날씨
#연도는 2025, 월은 02 일은 18 날씨는 sunny
#print(f"연도는 {date2[:4]}, 월은 {date2[4:6]}, 일은 {date2[6:8]}, 날씨는 {date2[8:]}")

a = "Life is too short, You need Python"
print(len(a))#문자열 길이
print(a.count("t",5,10)) #문자가 몇개 있는지
#print(a.index("x")) #앞에서 부터 찾는데 해당 문자의 인덱스 번호
#index는 없으면 오류를 낸다.
print(a.find("x")) # 문자열에만 사용가능
#find는 없으면 -1을 출력한다.
#print(a.lower()) #upper 소문자/대문자
#print(a[0].isupper())
print(a.replace("short", "long"))