from datetime import datetime

price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
    print(f'{i} {price_list[i]}')

for i in range(1, len(price_list)):
    print(f'{100+10*(i-1)} {price_list[i]}')

for i in range(2002, 2050):
    if(i%4==2):
        print(i)

a = 0.0
for i in range(0, 10):
    print(round(a,1))
    a += 0.1

ricker = "btc_krw"
print(ricker.upper())

file_name = "보고서.xlsx"

if file_name.endswith('xlsx'):
    print('xlsx로 끝납니다')
else:
    print('xlsx로 끝나지 않습니다')

b = "hello world"
print(b.split())

date = "2020-05-01"
print(date.split("-"))

상장주식수 = "5,969,782,550"
print([int(i) for i in 상장주식수.split(",")])

print(b.split())

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

리스트 = [3, 100, 23, 44]

for i in 리스트:
    if i%3==0:
        print(i)