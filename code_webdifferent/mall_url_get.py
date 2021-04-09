import pandas as pd 
import csv

csv_file =  "C:\programing\Atom_collection\code_webdifferent\\fix_data.csv"
df = pd.read_csv(csv_file,encoding='cp932')

dispID_dict = {}
name_dict = {}

for index in range(len(df)):
    dispID_dict[df.ソフィア開発環境[index]]=df.画面ID[index]
    name_dict[df.ソフィア開発環境[index]]=df.名前[index]

print(dispID_dict.keys())
print(df)
print(dispID_dict)
print(name_dict)
