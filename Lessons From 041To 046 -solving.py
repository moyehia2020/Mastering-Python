#assignments-Lessons From 041 To 046
#[01]
num1 = str(input("num1 : ").strip())
num2 = str(input("num2 : ").strip())
oper = str(input("Choose a math operation (+, -, *, /, %, //): "))
if oper in ["+" , "-" , "*" , "/" , "%"]:
    operation = num1 + oper + num2
    print(f"{num1} {oper} {num2} = {eval(operation)}")
else: 
    print("Operation not supported.")

#-----------------------------------------
print("###" * 10)
#[02]
age = 17
print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")

#-----------------------------------------
print("###" * 10)
#[03]
age = int(input("Add Your Age : "))
age_months = age * 12
age_weeks = age * 12 * 4
age_days = age * 12 * 4 * 7
age_hours = age * 12 * 4 * 7 * 24
age_minutes = age * 12 * 4 * 7 * 24 * 60
age_seconds = age * 12 * 4 * 7 * 24 * 60 * 60

print(f"Your Age In Months Is {age_months} Months")
print(f"Your Age In Weeks Is {age_weeks} Weeks")
print(f"Your Age In Days Is {age_days} Days")
print(f"Your Age In Hours Is {age_hours} Hours")
print(f"Your Age In Minutes Is {age_minutes} Minutes")
print(f"Your Age In Seconds Is {age_seconds} Seconds")

#-----------------------------------------
print("###" * 10)
#[04]
country = input("Input Your Country :").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    discount_country = price - discount
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${discount_country}")
else:
    print("Your Country Not Eligible For Discount And The Price Is $100")







