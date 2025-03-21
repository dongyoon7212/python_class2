# class Car:
#     pass

# a = 10
# if a < 100:
#     pass

# while True:
#     pass

# for i in range(1, 10):
#     pass

# class Car: #클래스 정의
#     def __init__(self, model, price): #생성자
#         self.model = model
#         self.price = price
#         print(f"모델 이름:{self.model} 가격:{self.price} 객체 생성!!")
#
#     def __del__(self): # 소멸자
#         print(f"{self.model}의 객체가 소멸됨!!")
#
#     def drive(self, speed, distance):
#         print(f"{self.model}가 {speed}의 속도로 {distance}km 만큼 전진")
#
# car1 = Car("avante", 2400) #car1 객체 생성
# car1.is_n = "아님" #멤버 변수
# print(car1.is_n)
#
# print(f"car1의 모델명:{car1.model}")
# print(f"car1의 가격:{car1.price}")
# car1.drive(80, 1)
# Car.drive(car1, 80, 2)
# # print(isinstance(car1, Car))
# car2 = Car("santafe", 4000)
# car2.drive(50, 10)

# class Player:
#     def __init__(self, nickname, hp=100, gold=0, level=1):
#         self.nickname = nickname
#         self.hp = hp
#         self.level = level
#         self.gold = gold
#         print(nickname, hp, gold, level)
#
#     def __del__(self):
#         print("저장중")
#         print("저장되었습니다.")
#
#     def change_nickname(self, new_nickname):
#         self.nickname = new_nickname
#
#     def del_player(self):
#         print("케삭되었습니다.")
#
# player1 = Player("yoon", 5000, 10000, 100)
# player1.change_nickname("dong")
# print(player1.nickname)
# player1.del_player()


class Person:
    def __init__(self, age, email, name="홍길동"):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        print(f"이름은 {self.name}이고 나이는{self.age}고 이메일은 {self.email}입니다")

person1 = Person(27, "dongyoon7212@naver.com", "이동윤")
person1.introduce()
person2 = Person(20, "example@gmail.com")
person2.introduce()
person2.address = "부산 진구"
print(person2.address)

