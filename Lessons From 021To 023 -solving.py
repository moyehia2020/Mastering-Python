#assignments-Lessons From 021 To 023
#[01]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends[-5])
print(friends[-1])
print(friends[4])

#[02]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])

#[03]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1:4])
print(friends[3:])

#[04]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-2 : ]= "Elzero", "Elzero"
print(friends)

#[05]
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
print(friends)
friends.append("Salem")
print(friends)

#[06]
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
print(friends)
del friends[0:2]
print(friends)
del friends[-2:]
print(friends)

#[07]
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends += employees + school 
print(friends)

#[08]
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.reverse()
print(friends)

#[09]
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

#[10]
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
