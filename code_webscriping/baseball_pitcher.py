from bs4 import BeautifulSoup as bs4
import requests as req
import csv


class baseball:
    division = '0'
    url  = 'https://baseball-data.com/'
    info = []
    List  = []
    count = 0
    
    def __init__(self, division):
        if 2018 >= division >= 2009:
            self.division = division - 2000
        
        elif division == 2019:
            self.division  = ''
        
        else:
            print('we have no data')
            exit()

        self.url = self.url + str(self.division) + '//stats/pitcher-all/win-1.html'
        
        r = req.get(self.url)
        self.soup = bs4(r.content, 'html.parser')  
        
        th = self.soup.find('th')
        self.Note = []
        self.Note.append('')
        
        
        for index in range (20):
            if th == None:
                exit()
            else:
                th = th.findNext('th')
                temp = th.text.replace('<br />',  '')
                self.Note.append(temp)
        

        self.Note.append('Year')
        #self.info.append([str(int(self.division) + 2000)])
        self.info.append(self.Note)
        
    
    def Serch(self): 
        self.tbody = self.soup.find('tbody')
        self.tr = self.tbody.find('tr')
          
    def Serch2(self):                
        td = self.tr.find('td')
        Pitcher_list = []
        if td == None:
            return self.info
        else:
            Pitcher_list.append(td.text)
        
        for index in range (20):
            key = td.findNext('td')
            test = key.text.replace('\u3000', '')
            Pitcher_list.append(test)
            td = key

        self.tr = self.tr.findNext('tr')
        
        if self.division == '':
            Pitcher_list.append(2019)
        elif 18 >= int(self.division) >= 9:
            Pitcher_list.append(str(int(self.division) + 2000))
      
        self.info.append(Pitcher_list)
        
        Pitcher_list.clear

                
    
    def Get(self):
    
        self.Serch()
        for v in range (300):
            self.Serch2()

        return self.info    


for index in range (2009, 2020):
    division = baseball(index)
    division.Get()
    List = division.info

    #print(List)


    f = open('test.csv', 'w')
    writer = csv.writer(f)
    writer.writerows(List)
    f.close()








    
        






   

        