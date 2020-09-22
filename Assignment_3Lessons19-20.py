#===========================================
#============= Assignment Three ============
#============= Lessons 19 To 20 ============
#===========================================
#[01] Write Down All Types Of Integer
#===========================================
num = 1
num = 100
num = -1
num = -100

#===========================================
#[02] Get The Imaginary Part For The Complex Number "1+2j"
#===========================================
x = 1
n = 2
y = complex(x,n)
print(y)
print(y.real)
print(y.imag) #<---------- The Answer

#===========================================
#[04] Convert Number 10 To Floating Point Number With 10 Number After Decimal
#===========================================
print(float(10))
print(format(float(10) ,".10f"))

#===========================================
#[05] Convert Floating Number 159.650 To Integer
#===========================================
print(int(159.650))

#===========================================
#[06] Function==============================
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
#[07] Get The Same Result Without Use The Exponents 3 ** 8
#===========================================
print(3 ** 8)
print(3 * 3 * 3 * 3 * 3 * 3 * 3 * 3)

#===========================================
#[08] Whats The Different Between 21 / 2 And 21 // 2 "Write Soultion With Comment"
#===========================================
print(21 / 2)#----------- Decimal and Integer 
print(21 // 2)#---------- Only Integer