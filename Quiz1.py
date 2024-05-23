user_input = input("계산식을 입력하세요> ")

if '+' in user_input:
    numbers = user_input.split('+')
    answer = float(numbers[0]) + float(numbers[1])

elif '-' in user_input:
    numbers = user_input.split('-')
    answer = float(numbers[0]) - float(numbers[1])

elif '*' in user_input:
    numbers = user_input.split('*')
    answer = float(numbers[0]) * float(numbers[1])

elif '/' in user_input:
    numbers = user_input.split('/')

    if float(numbers[1]) == 0:
        answer = "0으로 나눌 수 없습니다."
        exit()
    answer = float(numbers[0]) / float(numbers[1])

else:
    print("올바른 연산자가 입력되지 않았습니다.")
    exit()

if answer == int(answer):
    print("결과는 {}입니다.".format(int(answer)))
else:
    print("결과는 {:.2f}입니다.".format(answer))