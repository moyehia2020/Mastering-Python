#[01]
my_nums = [15, 81, 5, 17, 20, 21, 13]
v = []
for x in my_nums:
    if x % 5 == 0:
        v.append(x)
    v.sort()
    v.reverse()
xx = len(v)
for x in v:
    print(f"{xx} ===> {x}")
    xx=xx-1
print("All Numbers Printed")
#[02]
for x in range(21):
    if x == 6 or x == 8 or x == 12:
        continue
    x = str(x)
    print(x.zfill(2))
print("All Numbers Printed")
#[03]
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C',
}
points={
  'A': 100,
  'B': 80,
  'C': 40,
}
total=[]
for k , v in my_ranks.items():
  print(f"My Rank in {k} Is {v} And This Equal {points[v]} Points")
  total.append(points[v])
print(f"Total Points Is {sum(total)}")


        



    