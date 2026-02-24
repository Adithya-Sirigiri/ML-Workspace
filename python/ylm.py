def display(year,month):
    if((year%4==0 and (year%100!=0 or year%400==0))and month==2):
        return 29
    else:
        if(month==1):
            return 31
        elif(month==2):
            return 28
        elif(month==3):
            return 31
        elif(month==4):
            return 30
        elif(month==5):
            return 31
        elif(month==6):
            return 30
        elif(month==7):
            return 31
        elif(month==8):
            return 31
        elif(month==9):
            return 30
        elif(month==10):
            return 31
        elif(month==11):
            return 30
        elif(month==12):
            return 31

i=1
while(i==1):
    y=int(input("Please enter year:"))
    m=int(input("Please enter month:"))
    print(display(y,m))    