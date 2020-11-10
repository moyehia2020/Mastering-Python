#From Lessons 26 To 32

#[01] Create A List Contains 1, 2, 3, 3, 4, 5, 1
A = [1, 2, 3, 3, 4, 5, 1]

#[02] Loop on List And Return The Unique Values Only ( We Need TO Use Set )
A = [1, 2, 3, 3, 4, 5, 1]
for i in set(A):
    print(i)

#[03] Convert The Result To Set And Loop on This Set And Exclude The Last Element From Loop
A = [1, 2, 3, 4, 5]
for i in (A[0:-1]):
    print(i)

#[04] Create Two Sets Contains 1, 2, 3, 4 And Second One A, B, C, D
B = {1, 2, 3, 4}
C = {"A", "B", "C", "D"}

#[05] Merge The Two Sets With 4 Methods
#---1---
print(B.union(C))
#---2---
B.update(C)
print(B)
#---3---
B |= C
print(B)
#---4---
print(B | C)

#[06] Create Set Contains 1, 2, 3, 4 And Add List Contains A, B, C To It
#---1---
B = {1, 2, 3, 4}
C = ["A", "B", "C"]
C = tuple(C)
B.add(C)
print(B)
#---2---
B = {1, 2, 3, 4}
C = ["A", "B", "C"]
B.update(C)
print(B)

#[07] Create Set Contains 1, 2, A, B And Other Set Contains 1, 2
Z = {1, 2, "A", "B"}
X = {1, 2}

#[08] Check if All Elements in Set Two Is Found in Set One Or No
print(X.issubset(V))

#[09] Create Multi-Dimensional Dictionary Contains Your 4 Skills With Name And Progress
Employee = {"Name": "Yehia", "Age": 30, "Job": , "City": "Cairo"}

#[10] Loop on The Keys Of The Dictionary And Count Number Of Elements Inside It

for x in Employee.keys():
    print(x)
#------------------
print(len(Employee))
#------------------
Keys = 0
for x in Employee:
    Keys+=1
print(Keys)

#[11] Loop on The Values Of The Dictionary And Count Number Of Elements Inside It
for x in Employee.Values():
    print(x)
#------------------
print(len(Employee))
#------------------
Values = 0
for x in Employee:
    Values+=1
print(Values)

#[12] Loop on The Keys + Value in The Same Time And Add ( - ) Between Them
Employee = {"Name": "Yehia", "Age": 30, "Job": "Accountant", "City": "Cairo"}
for x,y in Employee.items():
    print(x,"-",y)
#--------
x = Employee.keys()
m = Employee.values()
for i1, i2 in zip(x, m):
    print(i1,"-", i2)

#[13] Get All Items Inside Dictionary Without Using Loop
Employee = Employee.items()
print(Employee)


#[14] Add New Skill To The Dictionary And Be Sure Previous Step Get And New Skill You Add
Employee = {"Name": "Yehia", "Age": 30, "Job": "Accountant", "City": "Cairo"}
Employee["Experience"] = 10
print(Employee)

#[15] Create List Contains Your 5 Skills Names
K = ["HTML", "CSS", "PHP", "JS", "PYTHON" ]

#[16] Create Tuple Contains Your 5 Skills Progress 
V = (90, 80, 50, 70, 60)

#[17] Create Multi-Dimensional Dictionary From The List + Tuple You've Created 
Z = dict(zip(K,V)) #{'HTML': 90, 'CSS': 80, 'PHP': 50, 'JS': 70, 'PYTHON': 60}

#[18] Make One Of The Skills Progress Less Than 50%
Z["JS"]="45"
print(Z) # {'HTML': 90, 'CSS': 80, 'PHP': 50, 'JS': 45, 'PYTHON': 60}

#[19] Loop on All Skills And Exclude Any Skill Less Than 50%
for x ,y in Z.items():
    if y >= 50:
        print(x,":",y)

#[20] Create Dictionary Contains Numbers Between 1 And Given Number => { Number: Number * Number }
num = int(input("Add num :"))
D = {}
for i in range(1, num+1):
    D[i]=i*i
print(D) 
#------------------
def Dict_1 (num):
    D = {i:i*i for i in range(1, num+1)}
    return(D)
print(Dict_1 (10)) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


#-----------------------------

#[21] Create Dictionary Contains Skills ( HTML, CSS, JS ) And Nother One Contains ( PHP, Python )
Skills1 ={'HTML': 90, 'CSS': 80, 'JS': 50}
Skills2 ={'PHP': 90, 'PYTHON': 60}

#[22] Merge The Two Dictionaries And Sort The Skills Reversed Then Loop on All Skills
Skills1.update(Skills2)


#[23] Create Dictionary Contains Random Numbers From 1 To 20 
import random
dict_1 = dict()
for x in range(random.randint(1, 20)):
    dict_1[x] = x+1
print(dict_1)

#[24] Return The Maximum Value And Minimum Value in The Dictionary Value
d = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20}
def Max_min_num (d):
    Maximum_Value = max(d.values())
    Minimum_Value = min(d.values())
    d = {Maximum_Value : Minimum_Value}
    return d
print(Max_min_num (d))


#[25] Create Dictionary With Values 1, 2, 2, 2, 3, 3, 5, A, B, C 
v = [1, 2, 2, 2, 3, 3, 5, "A", "B", "C"]
k = range(1,len(v))
n = {}
for i1 in k:
    n[i1] = v[i1]
print(n) # {1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 5, 7: 'A', 8: 'B', 9: 'C'}

#[26] Loop On Dictionary And Return Unique Values Only

n = {0: 1, 1: 2, 2: 2, 3: 2, 4: 3, 5: 3, 6: 5, 7: 'A', 8: 'B', 9: 'C'}
for x in n:
    Unique_Values = set(n.values())
print(Unique_Values) # {1, 2, 3, 5, 'C', 'A', 'B'}
