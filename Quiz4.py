print("간단한 데이터 베이스 만들기")
print("메뉴")
print("1. 데이터 추가")
print("2. 데이터 검색")
print("3. 데이터 삭제")

# 데이터베이스를 루프 밖에 선언하여 초기화합니다.
student = {"name": ["철수", "영희", "민수", "길동"], "age": [21, 16, 24, 29], "score": [4.3, 3.1, 3.9, 4.1]}

while True:
    menu = int(input("메뉴를 선택하세요 > "))

    if menu == 1:
        print("[데이터 추가]")
        input_name = input("추가할 데이터의 이름을 입력하세요 > ")
        input_age = int(input("추가할 데이터의 나이를 입력하세요 > "))
        input_score = float(input("추가할 데이터의 점수를 입력하세요 > "))
        student["name"].append(input_name)
        student["age"].append(input_age)
        student["score"].append(input_score)
        print("추가됨.")

    elif menu == 2:
        print("[데이터 검색]")
        search_input = input("검색할 데이터의 키와 값을 입력하세요 (예: name:인하) > ")
        if ":" in search_input:
            key, value = search_input.split(":")
            if key in student:
                if key == "age" or key == "score":
                    value = float(value) if "." in value else int(value)
                if value in student[key]:
                    index = student[key].index(value)
                    search_result = {key: student[key][index] for key in student}
                    print(search_result)
                else:
                    print("해당하는 값이 없습니다.")
            else:
                print("입력이 잘못되었습니다. 형식에 맞게 다시 입력하세요 (예:name:인하)")

    #코드에서 첫 번째 if문에서 value를 변환한 후, 두 번째 if문은 이미 변환된 value를 사용하여 조건을 검사하기 때문에 연속적으로 실행될 수 있음

    elif menu == 3:
        print("[데이터 삭제]")
        input_name = input("삭제할 데이터의 이름을 입력하세요 > ")
        if input_name in student["name"]:
            name_index = student["name"].index(input_name)
            student["name"].pop(name_index)
            student["age"].pop(name_index)
            student["score"].pop(name_index)
            print("삭제됨.")
        else:
            print("해당 이름의 데이터가 없습니다.")
    else:
        print("올바른 메뉴를 선택하세요.")
        break
