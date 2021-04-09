from bs4 import BeautifulSoup as bs4
import requests as req

class Jleague:
    r = req.get("https://www.jleague.jp/match/section/j1/1/")
    soup = bs4(r.content, 'html.parser')
    
    club_L = ''
    goals_L = ''
    club_R = ''
    goals_R = ''
    
    def set_L(self):
         
        self.club_L = self.soup.find_all(class_="clubName leftside")
        self.goals_L = self.soup.find_all(class_="point leftside")
   
    
   
    
    def set_R(self):
        self.club_R = self.soup.find_all(class_="clubName rightside")
        self.goals_R = self.soup.find_all(class_="point rightside")

      
     
        
   
def main():
    
    result_dict = {}
    
    Leftside = Jleague()

    info_L = Leftside.set_L()
    
    for index in range(9):
        Name_l = Leftside.club_L[index].text
        Goal_l = Leftside.goals_L[index].text
        result_dict[Name_l] = Goal_l
    
    Rightside = Jleague()
    info_R= Rightside.set_R()
    
    for index in range(9):
        Name_r = Rightside.club_R[index].text
        Goal_r = Rightside.goals_R[index].text
        result_dict[Name_r] = Goal_r
    
    print(result_dict)

    goal = result_dict.get("\nFC東京\n")
    print('FC東京:' + goal)

if __name__ == '__main__':
    main()


        