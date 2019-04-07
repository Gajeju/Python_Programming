#불러올 모듈
def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
        return result

#import시 바로 print문이 출력되는 것을 방지
if __name__ == "__main__":
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10,10.4))