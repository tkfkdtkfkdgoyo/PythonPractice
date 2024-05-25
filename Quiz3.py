student = {"name": ["철수", "영희", "민수", "길동"], "age" : [21, 16, 24, 29], "score" : [4.3, 3.1, 3.9, 4.1]}
new_student = {} #한 학생 조회 시 나오는 딕셔너리

print("간단한 데이터베이스 검색 기능 구현")
print("[데이터 검색]")

input_name = input("검색할 데이터의 이름을 입력하세요 > ")

if input_name in student["name"]:
    name_index = student["name"].index(input_name) # name 키에 매칭되는 value 리스트에서 입력한 이름이 몇 번째 인덱스에 있는지 찾기
    search = {"name": student["name"][name_index], "age": student["age"][name_index], "score": student["score"][name_index]}
    print(search)


