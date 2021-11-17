"""
例題: 提出の必要はありません

配列を左から順に2つずつ比較し、毎回小さい方が左になるように交換したい
(array[0]とarray[1]の比較&交換、array[1]とarray[2]の比較&交換...を行いたい)
?を適切に埋めて、関数my_funcを完成させよ

注意: これはちゃんとソートをするプログラムではありません
"""
def my_func(array):
    for i in range(len(array) - 1):
        if (array[i] > array[i+1]):
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
    print(array)

numbers = [9, 5, 3, 18, 0, 19, 11, 1, 5]
my_func(numbers)
