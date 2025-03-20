import json
import random

def study(level):
    review_list = []

    with open("./words.json", "r", encoding="utf-8") as file:
        word_list = list(json.load(file))
        filtered_word_list = list(filter(lambda x: x["level"] == level, word_list))

        count = 0

        while count < 10:
            select_index = random.randint(0, len(filtered_word_list))
            print("=======================")
            print(f"{filtered_word_list[select_index]["meaning"]}")

            input_eng = input("단어 : ")
            if input_eng == filtered_word_list[select_index]["word"]:
                print("정답입니다!!!")
            elif input_eng != filtered_word_list[select_index]["word"]:
                print("오답입니다!!!")
                print(f"정답 : {filtered_word_list[select_index]["word"]}")
                review_list.append(filtered_word_list[select_index])

            count += 1

        with open("../review_note.json", "w", encoding="utf-8") as review_file:
            json.dump(review_list, review_file, indent=4, ensure_ascii=False)