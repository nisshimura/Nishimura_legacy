from bs4 import BeautifulSoup as bs4
import requests as req

class Jleague:
    division = "0"
    url = "https://www.jleague.jp/match/section/j1/" 
    
    
    club_L = ''
    goals_L = ''
    club_R = ''
    goals_R = ''
    
    def __init__(self, division):
        self.division = division
        self.url = self.url + str(division) + "/"
        r = req.get(self.url)
        self.soup = bs4(r.content, 'html.parser')    
    
    def set_L(self):      
        self.club_L = self.soup.find_all(class_="clubName leftside")
        self.goals_L = self.soup.find_all(class_="point leftside")
   
    def set_R(self):
        self.club_R = self.soup.find_all(class_="clubName rightside")
        self.goals_R = self.soup.find_all(class_="point rightside")

    def getAllResultDict(self):
        result_dict = {}       
        
        self.set_L()
        for index in range(9):
            Name_l = self.club_L[index].text
            Name_l = Name_l.strip('\n')
            Goal_l = self.goals_L[index].text
            result_dict[Name_l] = Goal_l
        
        self.set_R()
        for index in range(9):
            Name_r = self.club_R[index].text
            Name_r = Name_r.strip('\n')
            Goal_r = self.goals_R[index].text
            result_dict[Name_r] = Goal_r

        return result_dict

#score_6 = Jleague(6)
#goals_6 = score_6.getAllResultDict()

#score_10 = Jleague(10)
#goals_10 = score_10.getAllResultDict()

def printResult(team_name):
    print(team_name + ' : '  + goals.get(team_name))

for index in range(1,3):
    division = Jleague(index)
    goals = division.getAllResultDict()
    printResult('浦和')


   