import pandas as pd 
import csv

df = pd.read_csv("C:\programing\Atom_collection\code_jobcan\sophia.csv", encoding='cp932')

userID_dict = {}
password_dict = {}

for index in range(4):
    userID_dict[df.IDM[index]]=df.userID[index]
    password_dict[df.IDM[index]]=df.password[index]



print(userID_dict)
print(password_dict)

