#Lessons 38-40
#------------------------------------------------------------------------------
#[01]
name = input("Add your name : ")
name = name.strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")
#------------------------------------------------------------------------------
#[02]
age = int(input("Add your age : "))
print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You"if age < 16 else f"Hello Your Age Is {age}, All Articles Is Suitable For You")
#[02]
age = int(input("Add your age : "))
if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
#------------------------------------------------------------------------------
#[03]
first_name  = input(str("Add Your First Name : "))
#first_name = first_name.capitalize()
second_name = input(str("Add Your Second Name : "))
#second_name = second_name.capitalize()
print(f"Hello {first_name.capitalize()} {second_name.capitalize():.1s}.")
#------------------------------------------------------------------------------
#[04]
email = input("Add Your Email : ")
email = email.strip()
name = email.split("@")[0]
domain = email.split("@")[1]
domain_type = domain.split(".")[1]

print(f"Your Name Is {name}")
print(f"Email Service Provider Is {domain}")
print(f"Top Level Domain Is {domain_type}")

