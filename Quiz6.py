def load_file(): # 파일을 읽어서 리스트로 반환
    students = []
    try:
        with open('student.txt') as file:
            for line in file:
                name, age, score = line.strip().split(',')
                students.append({'name' : name, 'age' : int(age), 'score' : float(score)})
    except FileNotFoundError:
        print('File not found')

    return students

def save_file(students): # 리스트를 파일에 저장
    with open('student.txt', 'w') as file:
        for student in students:
            file.write(f"{student['name']},{student['age']},{student['score']}\n")
def add(students):
    load_file()
    new_name = input('추가할 데이터의 이름을 입력하세요: ')
    new_age = int(input('추가할 데이터의 나이를 입력하세요: '))
    new_score = float(input('추가할 데이터의 점수를 입력하세요: '))

    if type(new_age) != int or type(new_score) != float:
        print('잘못된 입력입니다.')
        return

    students.append({'name' : new_name, 'age' : new_age, 'score' : new_score})
    print('추가됨')
    save_file(students)

def search(students):
    load_file()
    search_input = input('검색할 데이터의 키와 값을 key:value 형태로 입력하세요: ')
    try:
        key, value = search_input.split(':')
        for student in students:
            if student[key] == value:
                print(student)
                return
        print('데이터를 찾을 수 없습니다.')
    except ValueError:
        print('잘못된 입력입니다.')

def delete(students):
    load_file()
    delete_input = input('삭제할 데이터의 이름을 입력하세요: ')
    for student in students:
        if student['name'] == delete_input:
            students.remove(student)
            print('삭제됨')
            save_file(students)
            return
    print('데이터를 찾을 수 없습니다.')


def main():
    students = load_file()

    while True:
        print("간단한 데이터 베이스 구현")
        print("1. 데이터 추가")
        print("2. 데이터 검색")
        print("3. 데이터 삭제")
        print("4. 종료")
        user_input = int(input("메뉴를 선택하세요 > "))

        if user_input == 1:
            add(students)
        elif user_input == 2:
            search(students)
        elif user_input == 3:
            delete(students)
        elif user_input == 4:
            print('프로그램을 종료합니다.')
            break
        else:
            print('잘못된 입력입니다.')

main()
