# Lessons Solving from 065 to 068
# [01]
import os

print("Current working directory:", os.getcwd())
print(os.path.dirname(__file__))
print(os.path.abspath(__file__))

for i in range(1, 51):
    if i == 25:
        my_files = open(
            "/Users/mo-yehia/Desktop/Python/special-text.txt", "w")
        continue
    my_files = open(f"/Users/mo-yehia/Desktop/Python/{i}.txt", "w")
    my_files.write(F"Elzero Web School => {{{i}}}\n")
    my_files.write("Current Working Directory\n")
    my_files.write(f"/Users/mo-yehia/Desktop/Python/{i}.txt \n")
    print(my_files)
    i += 1


# [02]

my_files = open("/Users/mo-yehia/Desktop/Python/1.txt", "a")
my_files.write("Appended => Elzero Web School \n"*50)


# [03]
my_files = open("/Users/mo-yehia/Desktop/Python/1.txt", "r")
lines = 0
words = 0
chars = 0
char_l = 0

for line in my_files:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    chars = chars + len(line)
    for x in line:
        if "l" == x:
            char_l += 1

print(f"Number Of Lines Is => {lines}")
print(f"Number Of Words Is => {words}")
print(f"Number Of Chars Is => {chars}")
print(f"Number Of Chars Is => {char_l}")

# [04]
my_files = os.path.dirname(__file__)
num = 13
for i in my_files:
    os.remove(f"/Users/mo-yehia/Desktop/Python/{num}.txt")
    num += 1
# Please find the error?
##################################################################
##################################################################
##################################################################
##### I tried to solve the problem and I could not solve it ######
##################################################################
##################################################################
