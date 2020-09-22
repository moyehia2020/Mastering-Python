#====================================
#== Assignment For Lessons 11 - 18 ==
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