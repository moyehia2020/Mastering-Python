#assignments-Lessons From 024 To 025
#[01]
names = "Osama",
print(names[0])
print(type(names))
#[02]
friends = ("Osama", "Ahmed", "Sayed")
friends = list(friends)
friends[0]= "Elzero"
friends = tuple(friends)
print(friends)
print(type(friends))
print(len(friends),"Elements")
#[03]
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(len(nums_and_letters_one),"Elements")
#[04]
my_tuple = (1, 2, 3, 4)
a, b,_,c = my_tuple
print(a)
print(b)
print(c)