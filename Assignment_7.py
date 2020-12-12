#Lessons 033 - 037
#[1]
print(bool(True))
print(bool(1))
print(bool(1.0))
print(bool([1, 2, 3]))
print(bool(False))
print(bool(""))
print(bool([]))
print(bool(0))

print("#" * 40)
#[2]
html = 80
css = 60
javascript = 70
print(html > 50 and html > 50 and javascript > 50)

print("#" * 40)
#[3]
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)

print("#" * 40)
#[4]
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
print(result**3)
print(result**3%26000)
print((result**3%26000)/5)
print(type(str((result**3%26000)/5)))
