#[1]
my_skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
x = 0
for i in my_skills:
    x+=1
    print(x,i)
#--------------------------------
print("====" * 9)
#--------------------------------
#[2]
def getNumbersBefore(num):
    for i in range(1,num):
        print(i, end="")
    if num <= 0 :
        print("Negative Numbers & Zero Not Allowed")
    return num
print(getNumbersBefore(10)) # 12345678910
getNumbersBefore(0) # Negative Numbers & Zero Not Allowed
getNumbersBefore(-1) # Negative Numbers & Zero Not Allowed
#--------------------------------
print("====" * 9)
#--------------------------------
#[3]
word = "Elzero Web School"
word1 = "Elzero Web School"
word2 = "Youtube World"
word3 = "We Love PHP"

def getFirstLetter(word):
    word = word.split()
    for ii in word:
        print(ii[0], end="")
    return""

print(getFirstLetter(word))  # "EWS"
print(getFirstLetter(word1)) # "EWS"
print(getFirstLetter(word2)) # "YW"
print(getFirstLetter(word3)) # "WLP"
#--------------------------------
print("====" * 9)
#--------------------------------
#[4]
my_string = "I Love Elzero Web School"
def countSubStrings(thesub, thestr):
    return thestr.count(thesub)

print(countSubStrings("l", my_string)) # 4
#--------------------------------
print("====" * 9)
#--------------------------------
#[5]
numbers = [1, 2, 2, 2, 4, 5, 7, 2, 2, 8, 9]
numbers = set(numbers)
for n in numbers:
    print(n)
#--------------------------------
print("====" * 9)
#--------------------------------
#[6]
thenumber = 195650432
def addCharacters(num) :
    return "{:,.2f}".format(num)
print(addCharacters(thenumber)) # 195,650.432

#--------------------------------
print("====" * 9)
#--------------------------------
#[7]
my_skills = ["HTML", "CSS", "JS", "Python", ["Flask", "Django"], "MySQL"]

for skill in my_skills:
    if type(skill) == list:
        for i in skill:
            print(f"--- {i}")
    else:
        print(f"- {skill}")
#--------------------------------
print("====" * 9)
#--------------------------------
#[8]
my_list = [100, 20, 10, 11, -2, 1, 4, 200]
print(min(my_list))



