"""
例題: 提出の必要はありません

本プログラムはPEP8に従い、インデント1回=スペース4つとする
https://www.python.org/dev/peps/pep-0008/#indentation
"""

"""
以下のrange内の?を適切に変更し、1~20まで（20を含む）の間の偶数をすべて表示するプログラムを完成させよ
（ただし、if文は使わないものとする）
"""
for i in range(0, 21, 2):
    print(i)

"""
以下の?を埋めて、2つの文字列string1・string2を1文字ずつ交互に入れた新しい文字列string3を表示せよ
(ただしstring3は、string1の先頭の文字列'b'から始まるようにすること)
"""
string1 = "banana"
string2 = "orange"
string3 = ""
for i in range(len(string1)):
    string3 += string1[i]
    string3 += string2[i]
print(string3)
