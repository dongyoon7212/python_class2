import random

start = False
start_answer = input("숫자 맞추기 게임을 시작하시겠습니까? Y/N ====== ")

if start_answer == "y" or start_answer == "Y":
    try_count = 0;
    start = True
    print("숫자 맞추기 게임을 시작합니다.")
    secret_number = random.randint(1,100)

    while start:
        guess = input("숫자를 입력해주세요 : ")
        if not guess.isdigit:
            print("숫자로 입력해주세요.")
            continue
            
        guess = int(guess)
        try_count += 1

        if guess > secret_number:
            print("Down")
        elif guess < secret_number:
            print("Up")
        else:
            print(f"정답입니다! {try_count}번 만에 맞췄어요!")
            break


        

    