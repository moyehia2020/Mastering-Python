#====================================
#== Assignment For Lessons 11 - 20 ==
#====================================
#[01] Create 3 Variables Name, Age, Country
name = "Mohamed"
age = "35"
country = "Egypt"

#[02] Print This Text To The Console => "Hello 'Variable Name', How You Doing \ """ Your Age Is "Variable Age""
print("Hello "+name+", How You Doing \\ Your Age Is "+age+" And You Live In "+country)

#[03] Print The Same Previous Text But in 3 Lines Not Single Line
print("""Hello {}, How You Doing \\ 
Your Age Is {} 
And You Live In {}""".format(name, age, country))

################ OR ################
text = """Hello {}, How You Doing \\ 
Your Age Is {} 
And You Live In {}"""

print(text.format(name, age, country))

#====================================
#=======From [04] to [08] ===========
#====================================
your_name = "Elzero"
print(your_name[1])    		#[04] Get The Letter "l" From Elzero
print(your_name[-1])   		#[05] Get The Letter "o" From Elzero 
print(your_name[1:4])  		#[06] Get The Letters "lze" From Elzero
print(your_name[::2])       #[07] Get The Letters "Ezr" From Elzero 
print(your_name[-2::-2])    #[08] Get The Letters "rzE" From Elzero

#[09] Remove Special Character From The String "#@#@Elzero#@#@" And Return Elzero
print("#@#@Elzero#@#@".strip("#@#@"))

#[10] Make A Function Add Zeros Before Given Number And Return Number Not Exceed 4 Width Example "0010", "1800"
def num_Width(num):
	return num.zfill(4)

print(num_Width("2"))

#[11] Make A Function Add Hashes Before Given String And Make Width Not Exceed 20 Characters
def add_Hashes(str):
	return str.rjust(20,"#") 

print(add_Hashes("Mohamed"))

#[12] Convert This String "OSamA" To "osAMa"	
print("OSamA".swapcase()) 

#[13] Count How Much Word Love in This String "I Love Python And Although Love Elzero Web School"
print("I Love Python And Although Love Elzero Web School".count("Love")) 

#[14] Find The Index Of The Letter "z" in String "Elzero"
print("Elzero".index("z"))

#[15] Replace The Word <3 With Love Letter One Time in This String => "I <3 Python And Although <3 Elzero Web School"
print("I <3 Python And Although <3 Elzero Web School".replace("<3","Love",1))

#[16] Replace All The Words <3 With Love Letter in This String => "I <3 Python And Although <3 Elzero Web School"
print("I <3 Python And Although <3 Elzero Web School".replace("<3","Love"))

#[17] Format The Variables Created in Step One With The New Way f""
print(f"Hello {name}, How You Doing \\ Your Age Is {age} And You Live In {country}")

#===========================================
#[18] Write Down All Types Of Integer
#===========================================
#----Integer--------
num = 1
num = 100
num = -1
num = -100
#----Float----------
num = 1.0
num = - 1.0
#----Complex--------
num =  1j
num =  -1j
num =  3+1j
#===========================================
#[19] Get The Imaginary Part For The Complex Number "1+2j"
#===========================================
x = 1
n = 2
y = complex(x,n)
print(y)
print(y.real)
print(y.imag) #<---------- The Answer

#===========================================
#[20] Convert Number 10 To Floating Point Number With 10 Number After Decimal
#===========================================
print(float(10))
print(format(float(10) ,".10f"))

#===========================================
#[21] Convert Floating Number 159.650 To Integer
#===========================================
print(int(159.650))

#===========================================
#[22] Function==============================
#--- Create Function Accepts Three Parameters ( num1, num2, operation )
#--- Check if Given Arguments Is Integers
#--- Return The Results of Addition if Third Parameter is ( add )
#--- Return The Results of Multiplication if Third Parameter is ( multiply )
#===========================================
def three_num(num1,num2,operation):
    if operation == "+":
        return num1 + num2 
    elif operation == "*":
        return num1 * num2 
    else:
        return "You Can use it in '+' or '*'"
 

print(three_num(5,6,"+"))
print(three_num(5,6,"*")) 

#===========================================
#[23] Get The Same Result Without Use The Exponents 3 ** 8
#===========================================
print(3 ** 8)
print(3 * 3 * 3 * 3 * 3 * 3 * 3 * 3)

#===========================================
#[24] Whats The Different Between 21 / 2 And 21 // 2 "Write Soultion With Comment"
#===========================================
print(21 / 2)      # 10.5 ----------- Division (The result is an Float number)
print(int(21 / 2)) # 10   ----------- Division (The result is an Float number)

print(21 // 2)     # 10 ---------- Floor division (The result is an integer number)
print(22 // 2)     # 11 ---------- Floor division (The result is an integer number)