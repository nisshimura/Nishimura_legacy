"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習:
実行すると文字列の入力を待ち、文字列が入力されたら(Enterが押されたら)、
与えられた文字列の最初の3文字と最後の3文字からなる文字列を出力するプログラムを作成せよ

以下の仕様を満たすこと
- 文字列はinput() で入力を待つ
- 文字列の最初の3文字と最後の3文字からなる文字列を出力
- ただし、文字列の長さが3より小さい場合は、"Invalid string"と出力
 
(実行例1):
abcdefg
abcefg

(実行例2):
金子研
金子研金子研

(実行例3):
ああ
Invalid string
"""    
x = input()
if len(x) < 3:
    print('Invalid string')
else:
    print(x[0:3] + x[len(x)-3:len(x)])