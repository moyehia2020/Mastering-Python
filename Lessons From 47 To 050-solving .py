#assignments-Lessons From 047 To 050
#[01]
num = int(input("Add a Number Greater Than Zero : "))
list_A = []
if type(num) == int and num > 0:
    for x in range(num, 1, -1):
        if (x-1) == 6:
            continue
        print(x-1)
        list_A.append(x-1)
    print("Done") 
    print(f"{len(list_A)} Numbers Printed Successfully.")

else:
    print(f"Number {num} Is Not Larger Than 0" )

#[02]    
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
lower_list=[]
for x in friends:
    if x == x.capitalize():
        print(x)
    elif x == x.lower():
        lower_list.append(x)

print(len(lower_list))

#[03]
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
while skills:
    print(skills.pop(0))

#[04]
my_friends = []
x = 4
for name in range(4):
    name = input("Add the Name :").strip()
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        my_friends.append((name).capitalize())
        x -= 1 
        print(f"Friend {name.capitalize()} Added => 1st Letter '{name[0]}' Become Capital '{name[0].capitalize()}'")
        print(f"Names Left in List Is {x}")
    elif name == name.capitalize():
        my_friends.append(name.strip())
        x -= 1
        print(f"Friend {name.capitalize()} Added")
        print(f"Names Left in List Is {x}")
print(my_friends,x)
