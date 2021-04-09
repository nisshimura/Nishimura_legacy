from bs4 import BeautifulSoup as bs4
import requests as req


r = req.get("https://www.jleague.jp/match/section/j1/1/")
soup = bs4(r.content, 'html.parser')



clubname_l = soup.find_all(class_="clubName leftside")
goal_l = soup.find_all(class_="point leftside")
clubname_r = soup.find_all(class_="clubName rightside")
goal_r = soup.find_all(class_="point rightside")



            
clubname_l = soup.find_all(class_="clubName leftside")
goal_l = soup.find_all(class_="point leftside")
clubname_r = soup.find_all(class_="clubName rightside")
goal_r = soup.find_all(class_="point rightside")

result_dict = {}

for index in range(9):
    Name_l = clubname_l[index].text
    Goal_l = goal_l[index].text
    result_dict[Name_l] = Goal_l
        
for index in range(9):
    Name_r = clubname_r[index].text
    Goal_r = goal_r[index].text
    result_dict[Name_r] = Goal_r
    
print(result_dict)

goal= result_dict.get("\nFC東京\n")
print('FC東京:' + goal)




        