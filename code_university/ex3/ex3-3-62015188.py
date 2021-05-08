"""
ファイル名の00000000を学籍番号に置き換えて提出すること
"""

"""
2~100の間の数で素数をすべて見つけ出し、printせよ
ヒント: 2重ループ

print結果は

2
3
...

と、見つけた素数が小さい順にprintされていれば良い
"""

sosu_list = []

for i in range(2,101):
    if bool(sosu_list) == True:
        for sosu in sosu_list:
            temp_cadidate = []
            if i % sosu == 0:
                temp_cadidate = []
                break
            else:
                temp_cadidate.append(i)
        sosu_list.extend(temp_cadidate)
    else:
        sosu_list.append(i)
for index in sosu_list:
    print(index)