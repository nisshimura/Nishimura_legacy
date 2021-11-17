import random


def data_center(answer, data):
    data += answer
    return data

class Sudoku():
    def __init__(self):
        self.SUDOKU_GRID_BEGINNER = [
            [0, 4, 0, 0, 0, 7, 1, 0, 0],
            [5, 3, 0, 0, 9, 0, 0, 7, 0],
            [0, 0, 7, 0, 6, 0, 9, 4, 0],
            [4, 0, 6, 0, 8, 0, 7, 5, 1],
            [0, 1, 0, 0, 0, 0, 6, 9, 0],
            [0, 5, 3, 0, 1, 0, 0, 0, 2],
            [9, 6, 0, 0, 3, 0, 0, 1, 0],
            [3, 7, 0, 0, 5, 1, 0, 0, 0],
            [1, 0, 0, 2, 0, 9, 3, 6, 7],
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
        tf =[]

        for index in quest:
            if 0 in index:
                tf.append(False)                   
            elif len(set(index)) == 9:
                tf.append(True) 
            else:
                tf.append(False)

        result = self.return_tf('line',tf)
        return result

    def confirm_row(self, quest):
        tf = []
        
        for index in range(9):
            temp = []
            for i in range(9):
                if quest[i][index] == 0:
                    temp.append(0)
                else:
                    temp.append(quest[i][index])
                if i == 8:
                    if len(set(temp)) == 9 and not 0 in temp:
                        tf.append(True)
                    else:
                        tf.append(False)
                        

        result = self.return_tf('row',tf)        
        return result

    def confirm_square(self, quest):
        tf = []
        for i in range(0, 9, 3):
            temp1 = []
            temp2 = []
            temp3 = []
            temp1 += quest[i][0],quest[i][1],quest[i][2],quest[i+1][0],quest[i+1][1],quest[i+1][2],quest[i+2][0],quest[i+2][1],quest[i+2][2]
            temp2 += quest[i][3],quest[i][4],quest[i][5],quest[i+1][3],quest[i+1][4],quest[i+1][5],quest[i+2][3],quest[i+2][4],quest[i+2][5]            
            temp3 += quest[i][6],quest[i][7],quest[i][8],quest[i+1][6],quest[i+1][7],quest[i+1][8],quest[i+2][6],quest[i+2][7],quest[i+2][8]            

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

        result = self.return_tf('square',tf)
        return result

    def return_tf(self, place, tf):
        if set(tf) == {True}:
            # print('True')
            return True
        else:
            # print('False' + place)
            # print(tf)
            return False       

    def solve(self,quest):
        answer = []

        for index in quest:
            sample = self.random_row()
            ex = list(set(index))
            try:
                ex.remove(0)
            except:
                pass
            for k in range(len(ex)):
                sample.remove(ex[k])
            count = 0
            for i, j in enumerate(index):
                if j == 0:
                    index[i] = sample[count]
                    count += 1
                else:
                    pass
            
            answer += [index]
        return answer

    def random_row(self):
        num_list = [1,2,3,4,5,6,7,8,9]
        sample = random.sample(num_list,9)
        return sample



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

        
        

def main():
    work = Sudoku()
    data = []
    while True:
        quest1, quest2 = work.initial()
        answer = work.solve(quest1)
        tf = work.main_tf(answer)
        #data = data_center(answer, data)
        # print(data)
        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        if tf == True:
            break
        else:
            continue
    
    print(answer)
if __name__ == "__main__":
    main()