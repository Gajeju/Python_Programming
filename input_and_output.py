#프롬프트 입력
'''
number = int(input("숫자를 입력하시오 : "))
if number % 2 == 0:
    print("숫자는 짝수")
else:
    print("숫자는 홀수")

print()
'''

#한 줄에 이어 쓰기
for i in range(10):
    print(i, end=' ')
print()

print()

# 파일 생성
f = open("새파일.txt",'w')
f.close()

# 파일 쓰기 모드
f = open("새파일.txt",'w')
for i in range(1,11):
    data= "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

# 파일 읽기
f = open("새파일.txt","r")
line = f.readline()
print(line)
f.close()

#모든 줄을 읽어 리스트로 리턴
f = open("새파일.txt",'r')
lines = f.readlines()
print(lines)
f.close()

print()

#모든 내용을 문자열로 리턴
f = open("새파일.txt","r")
data = f.read()
print(data)
f.close()

# 파일 내용 추가
f = open("새파일.txt","a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

#파일 자동 close
with open("foo.txt","w") as f:
    f.write("Life is short, you need Python")
