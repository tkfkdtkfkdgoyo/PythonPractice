def factorial_repeat(n):
    res = 1
    for i in range(1, n+1):
        res *=i
    return res

def factorial_recursion(n):
    if n == 0 :
        return 1
    else:
        return n*factorial_recursion(n-1)

print('반복문으로 팩토리얼')
print("1!:", factorial_repeat(1))
print("2!:", factorial_repeat(2))
print("3!:", factorial_repeat(3))
print("4!:", factorial_repeat(4))
print("5!:", factorial_repeat(5))

print('\n\n재귀함수로 팩토리얼')
print("1!:", factorial_recursion(1))
print("2!:", factorial_recursion(2))
print("3!:", factorial_recursion(3))
print("4!:", factorial_recursion(4))
print("5!:", factorial_recursion(5))