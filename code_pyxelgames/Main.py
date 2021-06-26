from typing import Tuple
import pyxel
import math  # math.floorを使うので必要
from random import randint
import time

class App:
    def __init__(self):
        self.b_d = {0: [[48, 18], [16, 14], [32, 32], [16, 16]],  #OLLIE
                             1: [[32, 19], [16, 13], [48, 32], [16, 16]],   #HIPPIE
                             2: [[64, 32], [16, 32], [0, 48], [16, 16]]    #BACK
                             }
        self.s_d = {0: [[0, 0], [16, 16]],  #normal
                            1: [[0, 16], [16, 16]], #jump with board
                            2: [[32, 0], [16, 16]], #jump_onlyman
                            3: [[16, 8], [16, 8]], #board
                            4: [[48, 0], [16, 16]],  # mae age
                            5: [[0, 112], [16, 16]],  #usiro age
                            6: [[16, 24], [16, 8]],  # sleep
                            7: [[16, 48], [16, 16]],  # suc_hippie
                            8: [[32, 48], [16, 16]],  # suc_ollie
                            9: [[48, 48], [16, 16]],  # suc_back
                            10: [[80, 0], [16, 16]],  #ready push
                            11: [[80, 16], [16, 16]]  #do push
                            }

        self.p_d = {0: [[64, 0], [16, 16]], #消灯
                            1: [[16, 32], [16, 16]] #点灯
                            }
        
        self.b_g = {0: [[96,0],[256,32]],
                    1: [[0,64],[160,112]]}

        pyxel.init(160, 120, caption="skate_game", fps=60)

        self.frame = 0
        self.elpasedtime = 0
        self.score = 0

        self.ground_x = 0
        self.ground_y = pyxel.height-(pyxel.height % 16)-16
        
        self.player_x = pyxel.width/5
        self.player_y = self.ground_y-16
        self.p_s = 0

        self.gameover = False
        self.danger = False
        self.muteki_time = 0
        self.muteki = False

        self.police_x = 0
        self.police_y = self.ground_y-16
        self.police_status = 0

        self.board_x = pyxel.width/5
        self.board_y = self.ground_y-16

        self.barriers = []
        for i in range(3):
            seed = randint(0, 2)
            self.barriers.append([i*randint(50, 80), self.ground_y-self.b_d[seed][1][1], seed])

        pyxel.load("./img/skate.pyxres")
        pyxel.run(self.update, self.draw)



    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        self.update_frame()
        self.update_score()
        self.update_police()

        for i, v in enumerate(self.barriers):
            self.barriers[i] = self.update_barrier(*v)
        self.update_player()
        for index in self.barriers:
            self.update_danger(index[2], index[1], index[0])

        if pyxel.btn(pyxel.KEY_BACKSPACE):
            self.gameover = True
        if pyxel.btn(pyxel.KEY_ENTER) and self.gameover:
            self.restart()


    def restart(self):
        self.gameover = False
        self.player_x = pyxel.width/5
        self.player_y = self.ground_y-16
        self.p_s = 0
        self.frame = 0
        self.elpasedtime = 0
        self.score = 0
        self.danger = False
        self.muteki_time = 0

    def update_danger(self, seed, barrier_x, barrier_y):
        if self.is_crashed(self.s_d, self.p_s, self.player_x, self.player_y, self.b_d, seed, barrier_x, barrier_y):
            print('a')
            pass
        if self.is_crashed(self.s_d, self.p_s, self.player_x, self.player_y, self.b_d,seed, barrier_x, barrier_y) and self.danger:
            self.gameover = True
            self.draw_gameover()
        
        elif self.is_crashed(self.s_d, self.p_s, self.player_x, self.player_y, self.p_d, self.police_status,self.police_x, self.police_y) and self.danger:
            self.gameover = True
            self.draw_gameover()
        
        elif self.is_crashed(self.s_d, self.p_s, self.player_x, self.player_y, self.b_d, seed, barrier_x, barrier_y):
            self.muteki_time = self.elpasedtime
            self.danger = True
            self.muteki = True

        if self.elpasedtime-self.muteki_time > 3:
            self.muteki = False
        if self.elpasedtime-self.muteki_time > 10:
            self.danger = False
    
    def update_score(self):
        if self.elpasedtime%2 == 0 and self.frame == 30:
            self.score += 10

    def update_frame(self):
        self.frame += 1
        if self.frame == 60:
            self.frame = 0
            self.elpasedtime += 1

    def update_player(self):
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_UP):
            self.p_s = 1
            self.player_y += -1

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD_1_DOWN):
            if self.player_y >= self.ground_y-16:
                self.p_s = 6
                self.player_y = self.ground_y-8
            self.player_y += 1
            
        if pyxel.btn(pyxel.KEY_SPACE):
            self.p_s = 2


        if pyxel.btn(pyxel.KEY_RIGHT):
            self.p_s = 4
            self.player_x += 1
            
        if pyxel.btn(pyxel.KEY_LEFT):
            self.p_s = 5
            self.player_x += -1
        
        if self.is_Diving(self.player_y):
            self.player_y = self.ground_y - self.s_d[self.p_s][1][1]

        if not self.p_s == 6:
            if self.elpasedtime % 7 == 0 and self.frame == 30 and self.player_y == self.ground_y-self.s_d[self.p_s][1][1]:
                self.p_s = 10
                self.draw_player()
            if self.elpasedtime % 7 == 1 and self.frame == 30 and self.player_y == self.ground_y-self.s_d[self.p_s][1][1]:
                self.p_s = 11
                self.draw_player()
            if self.elpasedtime % 7 == 3 and self.frame == 30 and self.player_y == self.ground_y-self.s_d[self.p_s][1][1]:
                self.p_s = 0
                self.draw_player()
    def update_barrier(self, x, y, seed):

        x -= 1

        if x < -40:
            seed = randint(0, 2)
            x += 240
            y = self.ground_y-self.b_d[seed][1][1]

        return x, y, seed

    def update_police(self):
        if self.elpasedtime % 2 == 0 and self.frame == 30:
            self.police_status = 0
        if self.elpasedtime % 2 == 1 and self.frame == 30:
            self.police_status = 1

    def draw(self):
        if self.gameover:
            self.draw_gameover()
        else:
            pyxel.cls(0)
            self.draw_police()
            # マップの描画
            offset = (pyxel.frame_count // 16) % 160
            for i in range(2):
                pyxel.blt(i*160-offset, 0, 0, self.b_g[0][0][0], self.b_g[0][0][1], self.b_g[0][1][0], self.b_g[0][1][1])
            pyxel.blt(self.ground_x, self.ground_y, 0,
                    self.b_g[1][0][0], self.b_g[1][0][1], self.b_g[1][1][0], self.b_g[1][1][1])
            #障害物
            for x,y,seed in self.barriers:
                pyxel.blt(x, y, 0, self.b_d[seed][0][0], self.b_d[seed]
                          [0][1], self.b_d[seed][1][0], self.b_d[seed][1][1])
            #文字
            for x, y, seed in self.barriers:
                pyxel.blt(x-16, y-32, 0, self.b_d[seed][2][0], self.b_d[seed]
                          [2][1], self.b_d[seed][3][0], self.b_d[seed][3][1])
            self.draw_player()
            s = "SCORE {:>4}".format(self.score)
            pyxel.text(5, 4, s, 12)
            pyxel.text(4, 4, s, 7)

    def draw_player(self):
        pyxel.blt(self.player_x, self.player_y, 0,
                  self.s_d[self.p_s][0][0], self.s_d[self.p_s][0][1], self.s_d[self.p_s][1][0], self.s_d[self.p_s][1][1])
    def draw_board(self):
        pyxel.blt(self.player_x, self.player_y, 0,
                  self.s_d[self.p_s][0][0], self.s_d[self.p_s][0][1], self.s_d[self.p_s][1][0], self.s_d[self.p_s][1][1])
    def draw_police(self):
        if self.danger == True:
            pyxel.blt(self.police_x, self.police_y, 0,
                      self.p_d[self.police_status][0][0], self.p_d[self.police_status][0][1], self.p_d[self.police_status][1][0], self.p_d[self.police_status][1][1])

    def draw_gameover(self):
        pyxel.cls(0)
        pyxel.text(60, 40, 'GAME OVER', 7)
        pyxel.text(40, 60, 'PRESS ENTER TO RESTART', 7)

    def is_Onground(self, player_y):
        if player_y == self.ground_y-self.s_d[self.p_s][1][1]:
            return True
        else:
            return False

    def is_Jumping(self, player_y):
        if player_y < self.ground_y-self.s_d[self.p_s][1][1]:
            return True
        else:
            return False

    def is_Diving(self, player_y):
        if player_y <= self.ground_y-self.s_d[self.p_s][1][1]:
            return False
        return True

    def is_crashed(self, target, status, player_x, player_y, enemy, e_status, barrier_x, barrier_y):
        if self.muteki:
            return False 
        for i in [1,0]:
            for j in [1,0]:
                if player_x+target[status][1][0]*i in [index for index in range(barrier_x, barrier_x+enemy[e_status][1][0]+1)]:
                    if player_y+target[status][1][1]*j in [index for index in range(barrier_y, barrier_y+enemy[e_status][1][1]+1)]:
                        return True
         
App()

