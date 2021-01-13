#assignments-Lessons From 038 To 040
#[01]
name = input("Add Your Name : ")
name = name.strip()
print(f"Hello {name}, Happy To See You Here.")

print("#####" * 10)
#----------------------
#[02]
age = input("Add Your Age : ")
age = int(age)
print(type(age))
if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

print("#####" * 10)
#----------------------
#[03]
first_name  = input("Add Your First Name : ").strip().capitalize()
second_name = input("Add Your First Name : ").strip().capitalize()
print(f"Hello {first_name} {second_name[0]}.")

print("#####" * 10)
#----------------------
#[04]
email = input("Add Your Email :").strip().lower()
name = email[:email.index("@")].capitalize()
Domain = email[email.index("@")+1:email.index(".")].capitalize()
Top_Level_Domain = email[email.index(".")+1:]
print(f"Your Name Is {name}")
print(f"Email Service Provider Is {Domain}")
print(f"Top Level Domain Is {Top_Level_Domain}")
