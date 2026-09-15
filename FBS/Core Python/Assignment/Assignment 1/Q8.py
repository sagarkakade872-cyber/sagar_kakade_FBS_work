#take input
day=int(input('enter the days: '))
years= day//365
day1= day%365
week=day1//7
day2=day1%7
print(f'{years}years,{week}weeks,{day2}days')
