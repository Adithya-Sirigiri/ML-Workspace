def days_in_month(year, month):
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year%4==0 and (year%100!=0 or year%400==0)) and month == 2:
        return 29
    else:
        return days_list[month - 1]

i=1
while(i==1):
    year = int(input("Enter a year:"))
    month = int(input("Enter a month:"))
    print(days_in_month(year, month)) 
