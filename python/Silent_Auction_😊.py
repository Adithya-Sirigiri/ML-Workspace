print("*****Welcome to silent Auction program*****")
dict={}
name=input("What is your name:")
bid=input("Enter your Bid:")
dict[name]=bid
nor=int(input("Are there any other bidders in the auction?: yes(1) or no(2)"))
while(nor == 1):
    name=input("What is your name:")
    bid=input("Enter your Bid:")
    dict[name]=bid
    nor=int(input("Are there any other bidders in the auction?: yes(1) or no(2)"))
l=len(dict)
var=max(dict())
print(var)