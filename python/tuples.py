tuple_adi=(1,45,18,33,7,10,1)
tuple1=(1,2,"Adithya")
print(tuple1)
data=["Adithya",124,130,"Pawan",1.7]
print(tuple(data))
tuple2=(124,130,"Pawan")
tuple3=tuple1+tuple2#concatation of tuples
print(tuple3)
tuple3=(tuple1,tuple2)
print(tuple3)
print(max(tuple_adi))
print(min(tuple_adi))
print(len(tuple_adi))
tuple4=("Adithya","Pawan","Srinivasa Rao")
print(tuple4.count("a"))
tuple5=(10)#it is considered as int
print(type(tuple5))
tuple6=(10,)                    
print(type(tuple6))
#always do not use variable name as the list or tuple or set it will cause the errors
tuple6=(10,)*5
print(tuple6)