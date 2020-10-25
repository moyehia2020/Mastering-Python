#Lessons 024 - 025
#---------------------------
#[01] Create Tuple Contain One Element Without Using The Parentheses
#---------------------------
names = ("yehia",)

#---------------------------
#[02] Print The Type To Be Sure Its Tuple
#---------------------------
print(type(names))

#---------------------------
#[03] Create Tuple Contains 5 Friends Name The First Is "Osama"
#---------------------------
names = ("Osama", "Yehia", "Mohamed", "Ali", "Ahmed")

#---------------------------
#[04] Use Your Knowledge To Change The First Name From "Osama" To "Elzero"
#---------------------------
names = ("Osama", "Yehia", "Mohamed", "Ali", "Ahmed")
names = list(names)
names[0] = "Elzero"
names = tuple(names)

#---------------------------
#[05] Print The Tuple With The New Name
#---------------------------
print(names)
print(type(names))

#---------------------------
#[06] Create Tuple Contain Numbers From 1 To 3 
#---------------------------
n = (1, 2, 3)

#---------------------------
#[07] Create Tuple Contain Letters From A To C
#---------------------------
l = ("A", "B", "C")

#---------------------------
#[08] Concatenate The Two Tuples
#---------------------------
x = n + l

#---------------------------
#[09] Create New Tuple With This Result From Old Tuples (1, "A", 2, "B", 3, "C")
#---------------------------
n = (1, 2, 3)
l = ("A", "B", "C")
for l1, l2 in zip(n,l):
    print(l1, l2, end=" ")

#---------------------------
#[10] Get Number Of Elements Inside The New Tuple With 2 Methods
#---------------------------
print(len(x))
#-----
index = 0
for i in x:
    index += 1
print (index)

#---------------------------
#[11] Create Tuple Contain 4 Elements ( With Any Data )
#---------------------------
num = ("mohamed", "yehia", "ali", "zero")

#---------------------------
#[12] Destruct The Tuple By Assigning Element One To Variable a And Element Two To Variable b And Element Four To Variable c
#---------------------------
a, b, _, c = num
#[13] Print Variables a, b And c
print(a)
print(b)
print(c)
