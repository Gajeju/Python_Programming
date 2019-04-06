#리스트를 출력
test_list = ['one', 'two', 'tree']
for i in test_list:
    print(i)

print()

# 튜플 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
print()

#for문 응용
marks = [90, 25, 67, 45, 80]
number = 0
for a in marks:
    number += 1
    if a >= 60:
        print("%d번째 학생은 합격입니다" % number)
    else:
        print("%d번째 학생은 불합격입니다" % number)
print()

# continue문
number = 0
for mark in marks:
    number += 1
    if mark < 60: continue
    print("%d번 학생 축하합니다 합격입니다" % number)
print()

# range함수 사용
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)
print()

#2중 for문 (구구단 출력)
for i in range(2, 10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()

#리스트 안에 for문 포함하기
a = [1, 2, 3, 4]
result = [num*3 for num in a]