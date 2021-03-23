#[02]

def addition(*numbers):
    lis =[]
    for num in numbers:
        if num == 10:
            continue
        if num == 5:
            num = -5
        lis.append(num)
    print(sum(lis))
        
addition(10, 20, 30, 10, 15, 5, 5)

#[03]
def show_skills (name, *skills):
    #print(type(skills))
    if len(skills) == 0:
        print(f"Hello {name} You Have No Skills To Show")
    elif len(skills) != 0:
        print(f"Hello {name} Your Skills Is")
    for skill in skills:
        print("- " + skill)
    
show_skills("Osama", "HTML", "CSS", "JS", "Python")  
print("#####"*10)      
show_skills("Ahmed")


print("#####"*10)
#[04]
def say_hello(name ="Unknown", age ="Unknown", country ="Unknown"):
    return(f"Hello {name} Your Age Is {age} And You Live In {country}") 

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())




