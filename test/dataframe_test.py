import pandas as pd

sungbun1 = ["a", "b", "c", "d"]
sungbun2 = ["a", "c", "d", "e"]
sungbun3 = ["a", "k", "z"]
sungbun4 = ["b", "k", "m"]

list = [sungbun1, sungbun2, sungbun3, sungbun4]

df = pd.DataFrame(list)

# print(df)

s1 = {
    "name": "화장품1",
    "type": "모든피부용",
    "sungbun1": ["a", "b", "c", "d"]
}

s2 = {
    "name": "화장품2",
    "type": "모든피부용",
    "sungbun1": ["a", "b", "c", "d"]
}

s3 = {
    "name": "화장품3",
    "type": "지성용",
    "sungbun1": ["a", "k", "z", ""]
}

s4 = {
    "name": "화장품4",
    "type": "지성용",
    "sungbun1": ["a", "b", "k", "z"]
}

s_list = [s1, s2, s3, s4]


new_list = []

for my_dict in s_list:

    dict = {}
    for key, value in my_dict.items():
        if key == "sungbun1":
            for v in value:
                dict.setdefault(v, True)
        else:
            dict.setdefault(key, value)

    new_list.append(dict)


df = pd.DataFrame(new_list)

print(df)
