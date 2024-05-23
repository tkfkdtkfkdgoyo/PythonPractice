print("계산기 시작")

# 변수 초기화
result = None
operator = None

for i in range(7):
    user_input = input("> ").strip() # 입력값 양쪽 공백 제거
    if not user_input:
        print("계산기 종료")
        break

    # 입력값이 연산자일 경우
    if user_input in "+-*/":
        operator = user_input

    else:
        if result is None:
            result = float(user_input)
        else:
            if operator == "+":
                result += float(user_input)
            elif operator == "-":
                result -= float(user_input)
            elif operator == "*":
                result *= float(user_input)
            elif operator == "/":
                if float(user_input) == 0:
                    print("0으로 나눌 수 없습니다.")
                    break
                result /= float(user_input)
            else:
                print("올바른 연산자가 입력되지 않았습니다.")
                break

if result is not None:
    if result == int(result):
        print("결과는 {}입니다.".format(int(result)))
    else:
        print("결과는 {:.2f}입니다.".format(result))