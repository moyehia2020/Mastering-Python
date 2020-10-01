# Assignment_4 (From lesson 21 to 23)
# [01] Create A List Contains Your Friends Names (Minimum 8 Friends)
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
# [02] Print First Name In The List ( With 2 Methods )
print(names[0])
print(names[-8])
print(names[-0])
print(names[0:1])
# [03] Print Last Name In The List ( With 2 Methods )
print(names[-1])
print(names[-1:])
# [04] Print The Even Names Only
print(names[1::2])
# [05] Print The Odd Names Only
print(names[::2])
# [06] Print The 2, 3, 4 Names
print(names[1:4])
# [07] Update The 5, 6, 7 Names With The Name "Elzero"
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names[4:7] = ["Elzero"]
print(names)
# [08] Append Two Names To The Main List
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names.append("Samir")
names.append("Gamal")
print(names)
# [09] Create Another 2 Lists With 2 Friends And Add All This Lists To The Main List
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names2 = ["Rami", "Adel"]
names3 = ["Samah", "moaz"]
names4 = names2 + names3
names.extend(names4)
print(names)
# [10] Remove The First Friend From The List
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names.remove("Mohamed")
print(names)
# [11] Remove The Last Friend From The List
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names.remove("Fawzi")
print(names)
# [12] Sort The List From A To Z
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names.sort()
print(names)
# [13] Sort The List From Z To A
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
names.sort()
names.reverse()
print(names)
# [14] Count Number Of Friends in The List ( With 2 Methods )
names = ["Mohamed","Yehia","Ali","Osama","Ahmed","Karim","Alaa","Fawzi"]
print(len(names))
# [15] Add A New Friend in The First Place
names.insert(0,"koko")
print(names)
# [16] Create A Main List For You Programming Skills And Nested List From Framework
main_list = ["HTML", "CSS", "JS",["Vuejs", "React", "Angular"],"Gulpjs"]
# [17] Loop on The Skills And Nested List
for x in main_list:
    print(x)
# [18] Access The Last Skill in List ( Create Condition To Check If Its Not A List )
if main_list[0] is "HTML":
    print("yes, The Last Skill is 'JS'")
else:
    print("Sorry, The Skill Not Fond")
# [19] Access The First Framework in The Nested List ( Create Condition To Check If Its A List First )
if main_list[3][0] is "Vuejs":
    print("yes, The First Framework in The Nested List 'Vuejs'")
else:
    print("Sorry, It's Not")
