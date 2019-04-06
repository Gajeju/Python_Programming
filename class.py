#계산기 클래스
class calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1 = calculator()
cal2 = calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))

print()

#self / __init__ 이해
class Service:
    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s 입니다" % (self.name, a, b, result))

pey = Service("김동현")
pey.sum(1,2)

print()

#사칙연산
class FourCal():
    def setdata(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

test = FourCal()
test.setdata(3,2)
print(test.sum())
print(test.mul())
print(test.sub())
print(test.div())

print()

#박씨네 집 self / __init__ 함수 / 클래스의 상속 / 메서드 오버라이딩 / 연산자 오버로딩
class House_Park:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, place):
        print("%s, %s여행을 가다" %(self.fullname, place))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

a = House_Park("응용")
print(a.fullname)
a.travel("부산")

print()

class House_Kim(House_Park):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %s일 가네" %(self.fullname, where, day))

juliet = House_Kim("줄리엣")
juliet.travel("독도",3)

print()

a.love(juliet)
a + juliet
a.fight(juliet)
a - juliet