<<<<<<< HEAD
<<<<<<< HEAD
import random


class Sudoku():
    def __init__(self):
        # self.SUDOKU_GRID_BEGINNER = [
        #     [0, 0, 0, 9, 0, 6, 4, 0, 0],
        #     [0, 7, 0, 0, 5, 0, 0, 0, 3],
        #     [8, 0, 0, 4, 0, 0, 0, 0, 0],
        #     [1, 0, 9, 0, 0, 0, 0, 7, 5],
        #     [0, 0, 5, 8, 0, 0, 2, 0, 0],
        #     [0, 4, 0, 0, 0, 0, 0, 0, 0],
        #     [3, 0, 0, 1, 0, 9, 0, 5, 0],
        #     [0, 0, 0, 0, 2, 8, 0, 9, 0],
        #     [5, 0, 0, 0, 0, 0, 0, 8, 0],
        # ]
        # self.SUDOKU_GRID_BEGINNER = [
        #     [8, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 0, 3, 6, 0, 0, 0, 0, 0],
        #     [0, 7, 0, 0, 9, 0, 2, 0, 0],
        #     [0, 5, 0, 0, 0, 7, 0, 0, 0],
        #     [0, 0, 0, 0, 4, 5, 7, 0, 0],
        #     [0, 0, 0, 1, 0, 0, 0, 3, 0],
        #     [0, 0, 1, 0, 0, 0, 0, 6, 8],
        #     [0, 0, 8, 5, 0, 0, 0, 1, 0],
        #     [0, 9, 0, 0, 0, 0, 4, 0, 0],
        # ]
        self.SUDOKU_GRID_BEGINNER = [
            [0, 1, 0, 0, 5, 0, 0, 7, 0],
            [7, 0, 0, 2, 0, 6, 0, 0, 4],
            [0, 0, 0, 1, 0, 3, 0, 0, 0],
            [0, 5, 2, 0, 0, 0, 1, 4, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 7, 6, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 8, 0, 5, 0, 0, 0],
            [6, 0, 0, 9, 0, 2, 0, 0, 7],
            [0, 2, 0, 0, 4, 0, 0, 6, 0],
        ]

        self.SUDOKU_GRID_True = [
            [5, 3, 1, 7, 2, 9, 6, 4, 8],
            [6, 4, 8, 5, 1, 3, 7, 9, 2],
            [2, 7, 9, 4, 8, 6, 3, 5, 1],
            [4, 1, 6, 8, 5, 7, 2, 3, 9],
            [8, 9, 7, 6, 3, 2, 5, 1, 4],
            [3, 2, 5, 9, 4, 1, 8, 7, 6],
            [1, 6, 2, 3, 9, 5, 4, 8, 7],
            [7, 5, 4, 1, 6, 8, 9, 2, 3],
            [9, 8, 3, 2, 7, 4, 1, 6, 5],
        ]

    def initial(self):
        self.__init__()
        quest1 = self.SUDOKU_GRID_BEGINNER
        quest2 = self.SUDOKU_GRID_True
        return quest1, quest2

    def confirm_line(self, quest):
        tf = []

        for index in quest:
            if 0 in index:
                tf.append(False)
            elif len(set(index)) == 9:
                tf.append(True)
            else:
                tf.append(False)

        result = self.return_tf('line', tf)
        return result

    def confirm_row(self, quest):
        tf = []

        for index in range(9):
            temp = []
            for i in range(9):
                temp.append(quest[i][index])
                if i == 8:
                    if len(set(temp)) == 9 and not 0 in temp:
                        tf.append(True)
                    else:
                        tf.append(False)

        result = self.return_tf('row', tf)
        return result

    def confirm_square(self, quest):
        tf = []
        for i in range(0, 9, 3):
            temp1 = []
            temp2 = []
            temp3 = []
            temp1 += quest[i][0], quest[i][1], quest[i][2], quest[i+1][0], quest[i +
                                                                                 1][1], quest[i+1][2], quest[i+2][0], quest[i+2][1], quest[i+2][2]
            temp2 += quest[i][3], quest[i][4], quest[i][5], quest[i+1][3], quest[i +
                                                                                 1][4], quest[i+1][5], quest[i+2][3], quest[i+2][4], quest[i+2][5]
            temp3 += quest[i][6], quest[i][7], quest[i][8], quest[i+1][6], quest[i +
                                                                                 1][7], quest[i+1][8], quest[i+2][6], quest[i+2][7], quest[i+2][8]

            if len(set(temp1)) == 9 and not 0 in temp1:
                tf.append(True)
            else:
                tf.append(False)
            if len(set(temp2)) == 9 and not 0 in temp2:
                tf.append(True)
            else:
                tf.append(False)
            if len(set(temp3)) == 9 and not 0 in temp3:
                tf.append(True)
            else:
                tf.append(False)

        result = self.return_tf('square', tf)
        return result

    def temp_line(self, quest):
        tf = []

        for index in quest:
            remove_zero = [i for i in index if i != 0]
            if len(set(remove_zero)) == len((remove_zero)):
                tf.append(True)
            else:
                tf.append(False)

        result = self.return_tf('templine', tf)
        return result

    def temp_row(self, quest):
        tf = []

        for index in range(9):
            temp = []
            for i in range(9):
                temp.append(quest[i][index])
                if i == 8:
                    remove_zero = [j for j in temp if j != 0]
                    if len(set(remove_zero)) == len(remove_zero):
                        tf.append(True)
                    else:
                        tf.append(False)

        result = self.return_tf('temprow', tf)
        return result

    def temp_square(self, quest):
        tf = []

        for i in range(0, 9, 3):
            temp1 = []
            temp2 = []
            temp3 = []

            temp1 += quest[i][0], quest[i][1], quest[i][2], quest[i+1][0], quest[i +
                                                                                 1][1], quest[i+1][2], quest[i+2][0], quest[i+2][1], quest[i+2][2]
            temp2 += quest[i][3], quest[i][4], quest[i][5], quest[i+1][3], quest[i +
                                                                                 1][4], quest[i+1][5], quest[i+2][3], quest[i+2][4], quest[i+2][5]
            temp3 += quest[i][6], quest[i][7], quest[i][8], quest[i+1][6], quest[i +
                                                                                 1][7], quest[i+1][8], quest[i+2][6], quest[i+2][7], quest[i+2][8]

            remove_zero1 = [j for j in temp1 if j != 0]
            remove_zero2 = [j for j in temp2 if j != 0]
            remove_zero3 = [j for j in temp3 if j != 0]

            if len(set(remove_zero1)) == len(remove_zero1):
                tf.append(True)
            else:
                tf.append(False)

            if len(set(remove_zero2)) == len(remove_zero2):
                tf.append(True)
            else:
                tf.append(False)

            if len(set(remove_zero3)) == len(remove_zero3):
                tf.append(True)
            else:
                tf.append(False)

        result = self.return_tf('tempsquare', tf)
        return result

    def return_tf(self, place, tf):
        if set(tf) == {True}:
            # print('True')
            return True
        else:
            # print('False' + place)
            # print(tf)
            return False

    def choice_init(self, quest):

        count = 0
        row_answer = []

        for i in range(9):
            xy = self.next(quest, count)
            answer_list = []
            for y in xy:
                temp_answer = []

                for index in range(1, 10):
                    quest, quest2 = self.initial()
                    quest[count][y] = index
                    tf = self.temp_tf(quest)

                    if tf == True:
                        temp_answer += [index]
                        if index == 9:
                            answer_list += [temp_answer]
                            quest[count][y] = 0
                            break
                        else:
                            continue

                    else:
                        if index == 9:
                            answer_list += [temp_answer]
                            quest[count][y] = 0
                            break
                        else:
                            continue

            row_answer += [answer_list]
            count += 1

        return row_answer

    def solve(self, quest, row_answer):
        for i in range(9):
            y = self.next(quest, i)
            count = 0
            for index in row_answer[i]:
                if len(index) == 1:
                    quest[i][y[count]] = index[0]
                    count += 1
                else:
                    count += 1
                    pass

        return quest

    def choice(self, quest):

        count = 0
        row_answer = []

        for i in range(9):
            xy = self.next(quest, count)
            answer_list = []
            for y in xy:
                temp_answer = []

                for index in range(1, 10):
                    quest[count][y] = index
                    tf = self.temp_tf(quest)

                    if tf == True:
                        temp_answer += [index]
                        if index == 9:
                            answer_list += [temp_answer]
                            quest[count][y] = 0
                            break
                        else:
                            continue

                    else:
                        if index == 9:
                            answer_list += [temp_answer]
                            quest[count][y] = 0
                            break
                        else:
                            continue

            row_answer += [answer_list]
            count += 1

        return row_answer

    def solve(self, quest, row_answer):
        for i in range(9):
            y = self.next(quest, i)
            count = 0
            for index in row_answer[i]:
                if len(index) == 1:
                    quest[i][y[count]] = index[0]
                    count += 1
                    print(quest)
                else:
                    count += 1
                    pass

        return quest

    def next(self, quest, count):
        xy = []

        for y in range(9):
            if quest[count][y] == 0:
                xy += [y]
            else:
                pass

        return xy

    def main_tf(self, quest):
        a = self.confirm_line(quest)
        b = self.confirm_row(quest)
        c = self.confirm_square(quest)
        if a == True and b == True and c == True:
            # print(True)
            return True
        else:
            # print(False)
            return False

    def temp_tf(self, quest):
        a = self.temp_line(quest)
        b = self.temp_row(quest)
        c = self.temp_square(quest)
        if a == True and b == True and c == True:
            # print(True)
            return True
        else:
            # print(False)
            return False


def main():
    work = Sudoku()
    quest1, quest2 = work.initial()
    row_answer = work.choice_init(quest1)
    while True:

        answer = work.solve(quest1, row_answer)
        tf = work.main_tf(answer)

        if tf == True:
            print(answer)
            break
        else:
            row_answer = work.choice(answer)
            continue


if __name__ == "__main__":
    main()



=======
import boto3
import csv
import re
=======
import wx
>>>>>>> 86f4928b451d41d9b40d73f59a07f30b79abe0d2

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'LoadingStatus', size=(300, 200))
 
panel = wx.Panel(frame, wx.ID_ANY)

<<<<<<< HEAD
def myfunc01_handler(body):
    dynamoDB = boto3.resource('dynamodb')
    table= dynamoDB.Table('jobcan')
    
    row_name = ['日時', 'スタッフコード', '姓名', '所属グループ名', 'スタッフ種別', '総労働時間', 'プロジェクトコード','プロジェクト名', 'タスクコード', 'タスク名', '工数']

    for i, b in enumerate(body): 
        table.put_item(Item = {'No' : i})
        value = re.sub('"', '', b).split(',')
        print(value)
        if i == 0:
            pass
        else:
            for index, row in enumerate(row_name):
                table.put_item(Item = {row : value[index]})
>>>>>>> 6bcaa64c4264a24f8169d0e53f7dba2f9a2de0a1
=======
s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'Loading...')
 
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(s_text_1)
 
panel.SetSizer(layout)
 
frame.Show()
application.MainLoop()
>>>>>>> 86f4928b451d41d9b40d73f59a07f30b79abe0d2
