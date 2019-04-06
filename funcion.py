# a+b 리턴
def sum(a,b):
    return a + b

a = 3
b = 4
c = sum(a, b)
print(c)

print()

# 입력값이 정해지지 않은 함수
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1,2,3)
print(result)
result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

print()

# 여러 자료형의 인수 받기
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

print()

# 여러개의 리턴값
def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)
(sum, mul) = sum_and_mul(3,4)
print("sum = : %d, mul = %d" % (sum, mul))

print()

# 전역변수를 함수 내에서 사용
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)
