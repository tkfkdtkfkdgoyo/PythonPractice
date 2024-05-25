# 반복문으로 팩토리얼 구현하기
def factorial_repeat(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀함수로 팩토리얼 구현하기
def recursive_factorial(n):
    if n == 1:
        return 1
    return n * recursive_factorial(n - 1)

print("반복문으로 팩토리얼")
print("1!: ", factorial_repeat(1))
print("2!: ", factorial_repeat(2))
print("3!: ", factorial_repeat(3))
print("4!: ", factorial_repeat(4))
print("5!: ", factorial_repeat(5))
print("====================================")
print("재귀함수로 팩토리얼")
print("1!: ", factorial_repeat(1))
print("2!: ", factorial_repeat(2))
print("3!: ", factorial_repeat(3))
print("4!: ", factorial_repeat(4))
print("5!: ", factorial_repeat(5))