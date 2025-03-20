from mypackage.review.review import review
from mypackage.study.study import study

while True:
    print("========메뉴=======")
    print("""
        1. 초등
        2. 중고
        3. 전문
        4. 오답노트
        5. 종료
    """)

    choice = input("메뉴를 선택하세요 : ")
    if choice == "1":
        study("초등")
    elif choice == "2":
        study("중고")
    elif choice == "3":
        study("전문")
    elif choice == "4":
        review()
    elif choice == "5":
        break
    else:
        print("다시 선택해 주세요.")
        continue