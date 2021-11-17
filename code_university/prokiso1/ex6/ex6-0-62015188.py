"""
ファイル名の00000000を学籍番号に置き換えて提出すること
例題: 以下の3つの関数をDocstring(Googleスタイル)に従って完成させよ
"""

def ex_sum(a, b):
    """2つの数の和を返す関数

    Args:
        a (int): 合計したい数その1
        b (int): 合計したい数その2

    Returns:
        int: aとbの和

    """
    return a + b


def ex_multi(a,b):
    """2つの数の積を返す関数

    Args:
        a (int): 掛け算する数その1
        b (int): 掛け算する数その2

    Returns:
        int: aとbの積

    """

    return a * b

def calc(f,a,b):
    """f(a, b)の結果を返す関数

    ただし、関数fがNoneの場合は、"function is not given."と表示し、Noneを返す

    Args:
        f (callable): 関数f, ここではex_sum()かex_multi()のみ渡されるとする
        a (int): 関数fに引き渡す引数その1
        b (int): 関数fに引き渡す引数その2

    Returns:
        int or None: f(a, b)の結果。引数fがNoneならNone

    """
    if f == None:
        print("function is not given.")
        return None
  
    return f(a,b)


