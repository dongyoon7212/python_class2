from todo_package.func import *

while True:
    print("=======메뉴======")
    print("""
        1. 할 일 추가
        2. 할 일 조회
        3. 할 일 수정
        4. 할 일 삭제
    """)

    choice = input("메뉴를 선택해 주세요. : ")
    if choice == "1":
        add()
    elif choice == "2":
        check()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    else:
        print("다시 메뉴를 선택해 주세요.")
        continue
