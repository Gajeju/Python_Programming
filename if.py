money = [1, 0]
for k in money:
    if k:
        print("택시를 타고가라.")
    else:
        print("걸어서 가라.")

# 비교 연산자 사용
a = 3
b = 5

if a > b:
    print ("a가 크다")
else:
    print("b가 크다")

# 논리 연산자
money = 2000
card = 1
if money >= 3000 or card:
    print("택시 타고가라")
else:
    print("걸어서 가라")

#요소 in 리스트
a = ['a', 'b', 'c']
if 'a' in a :
    print("a가 리스트에 존재")
else:
    print("a가 리스트에 없음")
a.remove('a')
if 'a' not in a :
    print("a가 리스트에 없음")
else:
    print("a가 리스트에 존재")

#조건을 만족하면 넘기기
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다중 조건
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걸어서")