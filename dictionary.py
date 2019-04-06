a = {1:'A', 2:'B', 3:"C"}
print(a)

#요소 추가
a[0] = 'Z'
print(a)

#요소 삭제
del a[2]
print(a)

#요소의 key 값을 이용하여 value 값 리턴
b = a[1]
print(b)

#key 값을 이용하여 리스트 만들기
b = {'name':'Hyun', 'phone':'010', 'birth':'0220'}
keyListObj = b.keys()
print(keyListObj)
for k in b.keys():
    print(k)
keyList = list(b.keys())
print(keyList)

#value 값을 이용하여 리스트 만들기
valueListObj = b.values()
print(valueListObj)
for k in b.values():
    print(k)

#key, value 쌍 얻기
itemList = b.items()
print(itemList)

#요소 모두 지우기
b.clear()
print(b)

#get 을 사용하여 value 값 리턴
b = {'name':'Hyun', 'phone':'010', 'birth':'0220'}
getValue = b.get('name')
getNone = b.get("tall")
print(getValue)
print(getNone)

#key 값 존재여부 조사
inNname = 'name' in b
inTall = "tall" in b
print(inNname,inTall)
