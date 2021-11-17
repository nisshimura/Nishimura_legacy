"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習1: 以下の関数をDocstringに従って完成させよ
"""

def find_divisible(min_num: int, max_num: int):
    """min_num以上, max_num以下の整数の中から、7で割り切れる最小の整数を返す関数

    min_num以上, max_num以下の整数の中から、7で割り切れる最小の整数を1つ返す。もし範囲内に場合はNoneを返す

    Args:
        min_num: 探索範囲の最小値
        max_num: 探索範囲の最大値

    Returns:
        int or None: 範囲内の7で割り切れる最小の整数。見つからない場合はNone

    """

    for i in range(min_num, max_num + 1):
        if i % 7 == 0:
            return i
    
    return None
