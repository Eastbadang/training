# text 변환 예
setBrick1 = """
With Brick
     .Reset 
     .Name "Shielding Sheet" 
     .Component "component1" 
     .Material "Ferrite" 
     .Xrange "-ss_x/2", "ss_x/2" 
     .Yrange "-ss_y/2", "ss_y/2" 
     .Zrange "-ss_z", "0" 
     .Create
End With
"""
setBrick1 = setBrick1.replace('ss_x', 'sx_2')
print(setBrick1)

# 문자열 바꾸기
s = 'Hello, world!'.replace('world', 'Python')
print(s)

s = 'Hello, world!'
s = s.replace('world!', 'Python')
s

# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
s = 'apple'.translate(table)
print(s)

# 문자열 분리하기
s = 'apple pear grape pineapple orange'.split()
print(s)

# 구분자 문자열과 문자열 리스트 연결하기
s = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(s)

s = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(s)

# 소문자를 대문자로 바꾸기
s = 'python'.upper()
print(s)

# 대문자를 소문자로 바꾸기
s = 'PYTHON'.lower()
print(s)

# 왼쪽 공백 삭제하기
s = '   Python   '.lstrip()
print(s)

# 오른쪽 공백 삭제하기
s = '   Python   '.rstrip()
print(s)

# 양쪽 공백 삭제하기
s = '   Python   '.strip()
print(s)

# 왼쪽의 특정 문자 삭제하기
s = ', python.'.lstrip(',.')
print(s)

# 오른쪽의 특정 문자 삭제하기
s = ', python.'.rstrip(',.')
print(s)

# 양쪽의 특정 문자 삭제하기
s = ', python.'.strip(',.')
print(s)

import string
s = ', python.'.strip(string.punctuation)
print(s)

string.punctuation
s = ', python.'.strip(string.punctuation + ' ')
print(s)

s = ', python.'.strip(string.punctuation).strip()
print(s)

# 문자열을 왼쪽 정렬하기
s = 'python'.ljust(10)
print(s)

# 문자열을 오른쪽 정렬하기
s = 'python'.rjust(10)
print(s)

# 문자열을 가운데 정렬하기
s = 'python'.center(10)
print(s)

# 메서드 체이닝
s = 'python'.rjust(10).upper()
print(s)

# 문자열 왼쪽에 0 채우기
s = '35'.zfill(4)        # 숫자 앞에 0을 채움
#s = '3.5'.zfill(6)       # 숫자 앞에 0을 채움
#s = 'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음
print(s)

# 문자열 위치 찾기
s = 'apple pineapple'.find('pl')
# s = 'apple pineapple'.find('xy')
print(s)

# 오른쪽에서부터 문자열 위치 찾기
s = 'apple pineapple'.rfind('pl')
# s = 'apple pineapple'.rfind('xy')
print(s)

# 문자열 위치 찾기
s = 'apple pineapple'.index('pl')
print(s)

# 오른쪽에서부터 문자열 위치 찾기
s = 'apple pineapple'.rindex('pl')
print(s)

# 문자열 개수 세기
s = 'apple pineapple'.count('pl')
print(s)