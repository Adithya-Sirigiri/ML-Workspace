numbers=[10,20,30,40,57,-8]
names=["adithya","Pawan","Jenny","Jonathon"]
mix_list=[1,"Human",1.867]
print(numbers[3])
print(numbers[1:6])
print(numbers[1:5])
print(numbers[1:])
print(numbers[:6])
print(numbers[:])
print(numbers[1:6:2])
print(numbers[-2])
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
numbers.sort()#here we cannot write print(numbers.sort()) as it returns a void or does not return at all
print(numbers)
numbers.reverse()#it is true for all functions
print(numbers)
numbers[3]=88
print(numbers)
numbers.append(55)
print(numbers)
numbers.insert(3,70)
print(numbers)
numbers.remove(57)
print(numbers)
numbers.pop()
print(numbers.pop())#it will give you the last number
print(numbers)