warn_investment_list = ["Microsoft","Google","Naver","kakao","SAMSUNG","LG"]

a = input("투자종목을 입력 받으세요 : ")

if a in warn_investment_list :
    print('위험종목입니다')
else :
    print('투자하시겠습니까?')