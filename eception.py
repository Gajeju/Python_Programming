#try, except 문
try:
    4/0
except ZeroDivisionError as e:
    print(e)

print()

#ty ..else 문
try:
    f = open('foo.txt', 'r')
except FileExistsError as e:
    print(str(e))
else:
    data = f.read()
    print(data)
    f.close()

print()

#try ..finally
f = open('foo.txt', 'r')
try:
    data1 = f.read()
    print(data1)
finally:
    f.close()

#오류 회피
try:
    f = open("없는파일", 'r')
except FileNotFoundError:
    pass

print()

#오류 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
