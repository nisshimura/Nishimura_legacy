"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習1: バブルソート
例題を参考にして、以下の仕様を満たすような関数bubble_sort()を完成させよ

- 配列を左から順に比較し、小さい方が左になるように交換していく
- 配列の最後まで比較&交換が終わったら、再び配列の最初から同じ処理を繰り返す
- この繰り返しは、配列の交換が1度も行われなくなるまで続ける

(余計なprint()があると採点の際に不具合が出る可能性があるので注意)
"""

def bubble_sort(array):
    while True:
        array, count = my_func(array)
        if count == 0:
            break
    print(array)

def my_func(array):
    count = 0
    for i in range(len(array) - 1):
        if (array[i] > array[i+1]):
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
            count += 1
    return array, count


numbers = [9, 5, 3, 18, 0, 19, 11, 1, 5, 9, 5, 3, 18]
bubble_sort(numbers) # 正しく実装できた場合、ここでarrayの中身が小さい順にソートされて表示される
 
