#slicing a list
numbers=(74,3,21,1)
print(numbers[2:])

#a list of even numbers 
even_num=[]
for num in range (20):
    if(num%2==0):
        even_num.append(num)
for i in range(len(even_num)):
    print(even_num[i])

for i in range(10):
  numbers.append(i)
  for i in range(len(even_num)):
    print(numbers[i])