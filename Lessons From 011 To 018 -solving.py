#assignments-Lessons From 011 To 018
#[01]
Name = "Osama"
Age  = "38"
Country = "Egypt"
print(" \"Hello 'Osama', How You Doing \ \"\"\" Your Age Is \"38\"\" + And Your Country Is: Egypt ")
#[02]
print(" \"Hello 'Osama', How You Doing \\ \n \"\"\" Your Age Is \"38\"\" +\n And Your Country Is: Egypt ")
#[03]
name = 'Elzero'
print('Second Letter Is '+ f'"{name[1]}"')  # Second Letter Is "l"
print('Third Letter Is ' + f'"{name[2]}"')  # Third Letter Is "z"
print('Last Letter Is '  + f'"{name[-1]}"') # Last Letter Is "o"
#[04]
name = 'Elzero'
print(f'"{name[1:4]}"') # "lze"
print(f'"{name[::2]}"') # "Ezr"
print(f'"{name[-2::-2]}"') # "rzE"
#[05]
name = "#@#@Elzero#@#@"
print(name.replace("#@",""))
#[06]
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
#[07]
name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))
#[08]
name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
#[09]
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
#[10]
name = "Elzero"
print(name.index("z"))
#[11]
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "love", 1))
#[12]
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "love"))
#[13]
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")