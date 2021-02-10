numbers = [15.60, 2, 2, 2, 4, 5, True, True, 7, "A", 2, False, 2, 8, 9]
new_numbers = []
new_numbers2 = []
for x in numbers:
    if x not in new_numbers:
        new_numbers.append(x)
for x in new_numbers: 
    if x == str(x):
        continue
    elif x == float(x):
        x = int(x)
    elif x == True :
        x = 1
    elif x == False :
        x = 0
    new_numbers2.append(x)
new_numbers2.sort()
new_numbers2.reverse()
for x in new_numbers2:
    print(x)
print("###########"*5)
print(new_numbers2)
#[15, 9, 8, 7, 5, 4, 2, 1, 0]
print("###########"*5)

