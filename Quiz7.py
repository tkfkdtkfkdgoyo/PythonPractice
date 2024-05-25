print("나눗셈 예외처리")

while True:
    try:
        input_a = input("나눗셈의 분자인 a를 입력하세요 (종료하려면 q를 입력하세요): ")

        if input_a == 'q':
            print("프로그램을 종료합니다.")
            break

        input_a = float(input_a)

        while True:
            try:
                input_b = float(input("나눗셈의 분모인 b를 입력하세요: "))

                if input_b == 0:
                    print("분모에 0을 사용할 수 없습니다. 다시 입력하세요.")
                    continue

                print(f"{input_a} / {input_b} =", int(input_a / input_b))
                break

            except ValueError:
                print("정수 또는 실수만 입력해주세요.")

    except ValueError:
        print("정수 또는 실수만 입력해주세요.")