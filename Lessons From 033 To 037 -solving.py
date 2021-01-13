#assignments-Lessons From 033 To 037
#[01]
print(bool(True))
print(bool(1))
print(bool(-1))
print(bool([1, 2, 3]))
#--------------------------
print(bool(False))
print(bool(0))
print(bool( ))
print(bool([]))
#---------------------------
print("#####" * 10)
#[02]
html = 80
css = 60
javascript = 70
print(html and css and javascript > 50)
#---------------------------
print("#####" * 10)
#[03]
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num > num_one and num > num_two)
#---------------------------
print("#####" * 10)
#[04]
num_one = 10
num_two = 20

result = num_one + num_two
print(result)
print(result ** 3)
print((result ** 3) % 26000)
print(((result ** 3) % 26000)/5)
print(type(str(((result ** 3) % 26000)/5)))
#---------------------------

