#assignments-Lessons From 026 To 027
#[01]
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
unique_list = list(unique_list)
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])
#----------------------
print("####"*8)
#[02]
nums = {1, 2, 3}
letters = {"A", "B", "C"}
nums_letters = nums.union(letters)
print(nums_letters)
nums.union(letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
#----------------------
print("####"*8)
#[03]
my_set = {1, 2, 3}
print(my_set)
my_set.clear()
print(my_set)
letters = {"A", "B", "C"}
my_set.update(letters)
my_set.remove("C")
print(my_set)
#----------------------
print("####"*8)
#[04]
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
#----------------------
print("####"*8)
#[05]
my_skills = {
    "HTML" : "90%",
    "CSS" : "80%", 
    "Python" : "30%",
    "AI" : "20%"
    }
print(f"{list(my_skills)[0]} Progress Is {list(my_skills.values())[0]}")
print(f"{list(my_skills)[1]} Progress Is {list(my_skills.values())[1]}")
print(f"{list(my_skills)[2]} Progress Is {list(my_skills.values())[2]}")
print(f"{list(my_skills)[3]} Progress Is {list(my_skills.values())[3]}")
 
