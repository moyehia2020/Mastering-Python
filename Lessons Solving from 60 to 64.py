# 60 - 64
# [01]
def get_score(**Subjects):
    for Sub_key, Sub_value in Subjects.items():
        print(f"{Sub_key} ==> {Sub_value}")


get_score(Math=90, Science=80, Language=70)
print("#####"*10)
get_score(Logic=70, Problems=60)

print("#####"*10)
# [02]
print("#####"*10)


def get_people_scores(name, **Subjects):
    if len(Subjects) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f"Hello {name} This Is Your Score Table:")

    for Sub_key, Sub_value in Subjects.items():
        print(f"{Sub_key} ==> {Sub_value}")


get_people_scores("Osama", Math=90, Science=80, Language=70)
print("#####"*10)
get_people_scores("Mahmoud", Logic=70, Problems=60)
print("#####"*10)
# get_people_scores(Logic=70, Problems=60)????????????????????????
##################################################################
##################################################################
##################################################################
##### I tried to solve the problem and I could not solve it ######
##################################################################
##################################################################
##################################################################
print("#####"*10)
get_people_scores("Ahmed")

print("#####"*10)
# [03]
print("#####"*10)

scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}


def get_the_scores(name, **scores_list):
    if len(scores_list) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f"Hello {name} This Is Your Score Table:")
    for scores_k, scores_v in scores_list.items():
        print(f"{scores_k} ==> {scores_v}")


print(type(scores_list))

get_the_scores("Osama", **scores_list)
print("#####"*10)
get_the_scores("Osama")
print("#####"*10)
# get_the_scores(**scores_list)
