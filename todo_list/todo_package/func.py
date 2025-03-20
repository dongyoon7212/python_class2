import json

def save_todo(todo_list):
    with open("../todo.json", "w", encoding="utf-8") as file:
        json.dump(todo_list, file, indent=4, ensure_ascii=False)

    print("저장되었습니다!")

def add():
    todo_list = []
    while True:
        todo_name = input("할 일(그만하려면 종료입력) : ")
        todo_complete = False
        if todo_name == "종료":
            save_todo(todo_list)
            break

        todo_list.append(
            {
                "todo_name": todo_name,
                "todo_complete" : todo_complete
            }
        )

def check():
    with open("../todo.json", "r", encoding="utf-8") as file:
        todo_list = list(json.load(file))

    for i in range(0, len(todo_list)):
        print(f"{i + 1}. 할 일 : {todo_list[i]["todo_name"]}")
        print(f"완료 상태 : {"완료" if todo_list[i]["todo_complete"] else "미완료"}")

    return todo_list
def update():
    todo_list = check()
    while True:
        choice_todo = int(input("몇 번째 Todo?"))
        todo = todo_list[choice_todo - 1]

        todo["todo_name"] = input("할 일 수정 : ")
        choice_complete = input("할 일 완료(y/n) : ")
        if choice_complete == "y":
            todo["todo_complete"] = True
        elif choice_complete == "n":
            todo["todo_complete"] = False


        continue_choice = input("또 수정하시겠습니까?(y/n)")
        if continue_choice == "y":
            continue
        elif continue_choice == "n":
            save_todo(todo_list)
            break

def delete():
    todo_list = check()
    if len(todo_list) == 0:
        print("삭제할게 없음")
    else:
        choice_todo = int(input("몇 번째 할 일을 삭제할거?"))
        del todo_list[choice_todo - 1]

        save_todo(todo_list)