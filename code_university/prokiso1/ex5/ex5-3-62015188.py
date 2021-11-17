"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習: 二分探索

第1引数に数字の配列、第2引数に探したい数字を取り、探したい数字が配列の何番目にあるか(=インデックス。0始まりとすること)を返し、見つからなければNoneを返す関数binary_searchを完成できるよう、?を適切に埋めよ

探索方法は以下のような形となる
1. 探索範囲の中心にある数字と探したい数字を比較
2. 配列の中心にある数字が探したい数字より大きければ中心より左側を、小さければ中心より右側を新たな探索範囲とする。もし同じであれば見つけたい数字があったことになるので探索は終了
3. 新たな探索範囲に対して、1番の処理から同じことを繰り返す

また、本プログラムは実行すると入力を待ち、数字を入力してEnterを押すと、binary_searchの第1引数に数字が小さい順にソート済みの配列numbersが、第2引数に入力された数字が与えられて実行され、返り値がprint()される。デバッグにはこれを用いると良い
"""

def binary_search(array, target):
    # 初期探索範囲は配列の左端から右端まで
    left_index = 0
    right_index = len(array) - 1

    while True:
        if left_index > right_index:
            # 探索範囲がなくなったとき、数字は見つからなかったものとする
            return None

        center_index = round((left_index + right_index)/2)

        if target < array[center_index]:
            right_index = center_index - 1
        elif target > array[center_index]:
            left_index = center_index + 1
        else:
            # 探索終了
            return center_index
        
numbers = [3, 7, 8, 9, 13, 17, 18, 20, 21, 24, 27, 29, 30, 33]
target_num = int(input())
result = binary_search(numbers, target_num)
print(result)
