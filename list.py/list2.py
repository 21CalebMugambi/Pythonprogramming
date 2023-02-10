#shows the list
numbers=[10,11,31]
for i in range(len(numbers)):
    print(numbers[i])

#to know the index
numbers=[10,11,31]
print(numbers.index(11))
names=("java", "python","C++")
print(names.index("java"))

#appending
numbers.append(35)
for i in range(len(numbers)):
    print(numbers[i])

# show list after appending
for i in range(len(numbers)):
    print(numbers[i])