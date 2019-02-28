import pandas as pd

with open("in/a_example.txt", "r") as ins:
    all_slides_list = []
    i = 0
    for line in ins:
        if ' ' not in line:
            continue
        tags_list = []
        V_or_H = line[0]
        num_tags = line[2]
        tags = line[4:-1]
        all_slides_list.append([i, V_or_H, num_tags, tags.split()])
        i += 1

df = pd.DataFrame(all_slides_list)
df.columns = ['ID', 'H_or_V', 'num_tags', 'tags']

df.head()

df.describe()

df_H = df.loc[df.H_or_V=='H']
df_H.head()

df_V = df.loc[df.H_or_V=='V']
df_V.head()

