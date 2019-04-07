#abs() : 절댓값
print(abs(3))
print(abs(-3))
print(abs(-1.2))

print()

#all : 모두 참일경우 True 리턴
print(all([1,2,3]))
print(all([1,2,0]))

#any : 하나라도 참일경우 True 리턴
print(any([1,0,0]))
print(any(['',0]))

print()

#dir : 객체가 자체적으로 가지고 있는 변수 또는 함수 리턴
print(dir([1,2,3]))
print(dir({'1':'a'}))

print()

#chr : 아스키 코드값을 입력으로 받아 해당하는 문자 리턴
print(chr(97))
print(chr(48))

print()

#divmod : 두 수를 나누어 몫과 나머지 튜플로 리턴
print(divmod(2,1))
print(divmod(1.3,0.2))

print()

#enumerate : 인덱스값을 포함하는 객체 리턴
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

print()

#eval : 실행가능한 문자열을 입력받아 결과 리턴
print(eval('2+3'))
print(eval("'hi'+'a'"))
print(eval('divmod(1,2)'))

print()

#