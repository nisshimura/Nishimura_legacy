import openpyxl
import wx

import csv

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

class MyFileDropTarget(wx.FileDropTarget):
    filename = ''
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window


    def OnDropFiles(self, x, y, filenames):
        # ファイルパスをテキストフィールドに表示
        for file in filenames:
            self.window.text.SetValue(file)

        self.filename = filenames[0]
        return True

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Drop Target", size=(600, 300))
        panel_ui = wx.Panel(self)
        # panel_ui1 = wx.Panel(self, id=ID_ANY, pos=(0,0), size=(200,100)))
        # panel_ui2 = wx.Panel(self, id=ID_ANY, pos=(200,0), size=(200,100))
        layout = wx.GridBagSizer()

        label = wx.StaticText(panel_ui, -1, 'File name')
        self.text = wx.TextCtrl(panel_ui, -1, '', size=(400,-1))
        
        button1 = wx.Button(panel_ui, label='Open', size=(60,20))
        button1.Bind(wx.EVT_BUTTON, self.OnOpenButton)
        
        layout.Add(label, (0,0), (1,1))
        layout.Add(self.text,(0,1), (1,2))
        layout.Add(button1, (1,0), (1,1))
        
        layout.AddGrowableRow(0)
        layout.AddGrowableRow(1)

        layout.AddGrowableCol(0)
        layout.AddGrowableCol(1)
        layout.AddGrowableCol(2)
        panel_ui.SetSizer(layout)

        self.dt = MyFileDropTarget(self)
        self.SetDropTarget(self.dt)
        self.Show()
    
    def OnOpenButton(self, event):
        filename = self.dt.filename
        work = Mainwork()
        work.Main(filename)
        
class Mainwork():
    def opencsv(self, filename):
        with open(filename,encoding='utf-8') as f:
            reader = csv.reader(f)
            self.l = [row for row in reader]
    
    def make_table(self):
        engine = sqlalchemy.create_engine('sqlite:///code_aws/sqlite_datas/sophia2_db.sqlite3',echo=True)

        Base = declarative_base()

        class Sophia(Base):
            values = ['date','id','name','group','staff_type','work_time','projectcode','projectname','taskcode','taskname','man_hour']

            
            date = Column(Integer)
            id = Column(Integer)
            name = Column(String)
            group = Column(String)
            staff_type = Column(String)
            work_time = Column(Integer)
            projectcode = Column(Integer)
            projectname = Column(String)
            taskcode = Column(Integer)
            taskname = Column(String)
            man_hour = Column(Integer)
            no = Column(Integer, primary_key=True)
            
            # date = Column(String)
            # id = Column(String, primary_key=True)
            # name = Column(String)
            # group = Column(String)
            # staff_type = Column(String)
            # work_time = Column(String)
            # projectcode = Column(String)
            # projectname = Column(String)
            # taskcode = Column(String)
            # taskname = Column(String)
            # man_hour = Column(String)

            __tablename__ = 'Sophia'

        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)()

        for i, v in enumerate(self.l):
            sophia = Sophia()
            if i == 0:
                pass
            else:
                for index, j in enumerate(v):
                    if index == 0:
                        sophia.date = j
                    elif index == 1:
                        sophia.id = j
                    elif index == 2:
                        sophia.name = j
                    elif index == 3:
                        sophia.group = j
                    elif index == 4:
                        sophia.staff_type = j
                    elif index == 5:
                        sophia.work_time = j
                    elif index == 6:
                        sophia.projectcode = j
                    elif index == 7:
                        sophia.projectname = j
                    elif index == 8:
                        sophia.taskcode = j
                    elif index == 9:
                        sophia.taskname = j
                    elif index == 10:
                        sophia.man_hour = j
                    elif index == 11:
                        sophia.no = i
                    else:
                        print('NOOOOOOOOOOOOOOOOOOOO')
                   
                    session.add(instance=sophia)
        
        session.commit()
        session.close()

    def Main(self, filename):
        self.opencsv(filename)
        self.make_table()
    
if __name__ == '__main__':
    app = wx.App()
    MyFrame()
    filename = app.MainLoop()
