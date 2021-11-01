#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/kitao/pyxel
# https://github.com/zwazel/Python-Snake/blob/master/pyxel/pyxel/core/include/pyxelcore/constants.h
# pyxeleditor  D:\プログラム\python\07_AI\pyxel\pyxel_examples\assets\jump_game.pyxres
import csv
from collections import deque, namedtuple
from random import randint
import pyxel
import datetime
now = datetime.datetime.now()
now = now.strftime("%y%m%d")  # 開始日時(記録ファイル名にする)

Point = namedtuple("Point", ["w", "h"])  # プレイヤーの向き
RIGHT = Point(16, 16)
LEFT = Point(-16, 16)
COLOR = 12


class App:
    GROUND_Y = 105  # 地面の座標

    def __init__(self):
        pyxel.init(160, 160, caption="skate_game")
        #pyxel.image(0).load(0, 0, "assets/cat_16x16.png")
        pyxel.load("./pyxel_examples/assets/jump_game.pyxres")

        # 初期化
        self.START = False
        self.GAMEOVER = False
        self.score = 0
        is_active = True
        self.direction = RIGHT
        self.player_x = 72
        self.player_y = self.GROUND_Y - 16
        self.player_vy = 0  # Y方向の速度
        self.gravity = 0.98  # 重力
        self.player_is_alive = True
        self.far_cloud = [(-10, 75), (40, 65), (90, 60)]
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]

        # 一回目iの隣数は出現間距離 range数は同時に出現する個数
        self.fruit = [(i * 40, randint(0, 104), randint(0, 3), True)
                      for i in range(6)]

        # 音再生
        pyxel.playm(0, loop=True)
        # 実行
        pyxel.run(self.update, self.draw)

    def update(self):
        # Qボタンで終了
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # スペースボタン
        if pyxel.btn(pyxel.KEY_SPACE) or pyxel.btn(pyxel.GAMEPAD_1_START):
            self.START = True
        if self.GAMEOVER and (pyxel.btn(pyxel.KEY_ENTER or pyxel.btn(pyxel.GAMEPAD_1_START))):
            self.reset()
        if not self.START or self.GAMEOVER:
            return

        # 加速度更新
        self.player_vy += self.gravity
        # 速度を更新
        self.player_y += self.player_vy

        # プレイヤーを地面に着地させる
        if self.player_y > self.GROUND_Y - 16:
            self.player_y = self.GROUND_Y - 16

        # プレイヤー
        self.update_player()

        # 果物
        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

        # スコア
        if not self.GAMEOVER:
            self.score += 1

    def update_player(self):
        # 左側へ移動する
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0)
            self.direction = LEFT

        # 右側へ移動する
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16)
            self.direction = RIGHT

         # 地面に居る時にジャンプする（2段ジャンプの防止）
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD_1_B):
            if self.player_y == self.GROUND_Y - 16:
                self.player_vy = -13
                self.score += 200

        if self.player_y > pyxel.height:
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600:
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True

    def update_fruit(self, x, y, kind, is_active):
        # プレイヤーと接触した場合
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            if kind == 0:
                is_active = False
                self.score += 300
                pyxel.play(3, 4)
            else:
                self.GAMEOVER = True
                is_active = False
                pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16, 16, 0)

                mylist = ['SCORE', self.score]
                with open(now + '_jumping_game_by_pyxel.csv', 'a', encoding="utf-8") as f:
                    writer = csv.writer(f, lineterminator='\n')  # 改行コード
                    writer.writerow(mylist)
                pyxel.stop()
        # 左へ2進む
        x -= 2
        # 3番目のキャラ（うんこ）の場合に上下にも動く
        if kind == 3:
            y = y + randint(-2, 2)

        # 画面端に消えたら右端へリセット
        if x < -40:
            x += 240
            y = randint(0, 104)
            kind = randint(0, 3)
            is_active = True

        return (x, y, kind, is_active)

    def reset(self):
        # 初期化
        self.START = True
        self.GAMEOVER = False
        self.score = 0
        pyxel.playm(0, loop=True)

    def draw(self):
        if self.GAMEOVER:
            MESSAGE =\
                """
GAMEOVER

    PUSH ENTER
"""
            pyxel.text(51, 40, MESSAGE, 1)
            pyxel.text(50, 40, MESSAGE, 7)
            return

        # 背景色
        pyxel.cls(COLOR)

        # 雲を描画
        offset = (pyxel.frame_count // 8) % 160
        for i in range(2):
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)

        offset = (pyxel.frame_count // 4) % 160
        for i in range(2):
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        # 山脈を描画
        offset = pyxel.frame_count % 160
        for i in range(2):
            pyxel.blt(i * 160 - offset, 88, 0, 0, 64, 160, 24, 12)

        # 地面
        pyxel.rect(0, self.GROUND_Y, pyxel.width, pyxel.height, 4)

        # 画像を表示したいところでblt関数を呼び出す
        # プレイヤー
        pyxel.blt(self.player_x,
                  self.player_y,
                  0,  # image_no
                  0,                 # 切り出しの左側
                  0,                 # 切り出しの上側
                  self.direction[0],  # 切り出す幅
                  self.direction[1],  # 切り出す高さ
                  COLOR)

        # 果物描画
        for x, y, kind, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 32 + kind * 16, 0, 16, 16, 12)

        # スコア描画
        s = "SCORE {:>4}".format(self.score)
        pyxel.text(5, 4, s, 1)
        pyxel.text(4, 4, s, 7)

        if not self.START:
            MESSAGE = "PUSH SPACE KEY"
            pyxel.text(61, 50, MESSAGE, 1)
            pyxel.text(60, 50, MESSAGE, 7)
            return


def main():
    App()


if __name__ == "__main__":
    main()
