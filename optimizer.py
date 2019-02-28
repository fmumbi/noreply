import pandas as pd
import numpy as np

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
        all_slides_list.append([[i], V_or_H, num_tags, tags.split()])
        i += 1

df = pd.DataFrame(all_slides_list)
df.columns = ['ID', 'H_or_V', 'num_tags', 'tags']

df.head()

df.describe()

df_H = df.loc[df.H_or_V=='H']
df_H.head()

df_V = df.loc[df.H_or_V=='V']
df_V.head()

def vertical_slide(df):
   pic1 = df.iloc[0]
   pic2 = df.iloc[1]

   tags_union = set(pic1["tags"]).union(pic2["tags"])
   return pd.DataFrame([[[pic1["ID"], pic2["ID"]],
           "V",
           str(len(tags_union)),
           list(tags_union)]])

df_V = vertical_slide(df_V)


def add_new_silde(slidedeck, df_H, df_V):
    if len(df_H) > 0:
        slidedeck.append(np.array(df_H.iloc[0]))
        df_H = df_H.drop(df_H.index[[0]])    
    if len(df_V) > 0:
        slidedeck.append(np.array(df_V.iloc[0]))
        df_V = df_V.drop(df_V.index[[0]]) 
    return slidedeck, df_H, df_V
    

def create_slidedeck(df_H, df_V):
    slidedeck = []
    slidedeck.append(np.array(df_H.iloc[0]))
    df_H = df_H.drop(df_H.index[[0]])
    while len(df_H)+len(df_V) > 0:
        slidedeck, df_H, df_V = add_new_silde(slidedeck, df_H, df_V)
    return slidedeck


slidedeck = create_slidedeck(df_H, df_V)
print(slidedeck)
