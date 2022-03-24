score = int(input("성적 입력 : "))

if score > 100 :
    print('100점을 초과합니다.')
elif score > 80 :
    print('A 학점 입니다.')
elif score > 60:
    print('B학점 입니다.')
elif score > 40:
    print('C학점 입니다.')
elif score > 20:
    print('D학점 입니다.')
else :
    print('E학점 입니다.')