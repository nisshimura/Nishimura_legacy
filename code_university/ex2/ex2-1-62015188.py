"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習1: 時間計算
"""

"""
例: 以下は1時間が何秒かを表示している
"""
ans0 = 60 * 60
print(ans0)

"""
問1: ?を適当な数字に変更し、1日が何秒か求めよう
"""
ans1 = 24 *  60 * 60
print(ans1)

"""
問2: ans1を使って、6日間が何秒か求めよう
"""
ans2 = 6 * ans1
print(ans2)

"""
問3: ans1を使って、割り算で259200秒が何日か求めよう
(小数点(.0)が表示されても良い)
"""
ans3 = 259200 / ans1
print(ans3)