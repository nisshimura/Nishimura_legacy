"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習 データ処理:
- 以下で示すフォーマットのデータを処理する関数をそれぞれ実装せよ
- また、全ての関数の中身にあらかじめpassと書いてあるが、これは中身が空っぽの関数のままでも実行できるようにするための措置である。自分で関数を実装し始めたらpassの行は消して良い
"""

"""
データについて:
- データは1行ごとに「時刻(HH:MM:SS)」「タイプ」「数値」の3つの文字列がスペース区切りになっている
- 時刻はHHが時間、MMが分、SSが秒をそれぞれ示す文字列である
- タイプは適当な文字列である
- 数値は0以上の整数を示す文字列である
- 以下全ての問題において、解析対象のデータのフォーマットが崩れている場合を特に考慮しなくて良いものとする

以下に解析したいデータの例を示す
- 各問題の実行例ではこれを使用している
- 時刻00:00:00で始まる最初の行を見逃さないように注意 (つまりこの例では行数は全部で10行である)
"""
data = """00:00:00 A 40
00:00:06 B 1
00:00:06 AB 5
00:01:16 AB 2
00:12:02 AB 4
00:12:26 B 21
00:13:06 B 34
01:25:03 A 4
01:24:41 AB 5
01:33:20 A 7"""

"""
問題1
特定のタイプの出現行数をカウントする関数、count_type()を実装せよ
また、指定したタイプの行がなかった場合は0を返し、いずれかの引数の型が違った場合はNoneを返すこと

実行例
> print(count_type(data, 'A'))
> 3

> print(count_type(data, 'C'))
> 0

> print(count_type(123, 456))
> None
"""
def count_type(data, data_type):
    """
    Args:
        data (str): 解析対象データ
        data_type (str): カウントしたいタイプ
    Returns:
        int or None: 特定のタイプが存在する行数
    """
    data = str(data)
    data = data.split('\n')
    count = 0
    for i in data:
        if data_type == 'A':
            if data_type in i:
                count += 1
            if 'AB' in i:
                count -= 1
        elif data_type == 'B':
            if data_type in i:
                count += 1
            if 'AB' in i:
                count -= 1
            
        elif data_type in i:
            count += 1
    
    return count
    




"""
問題2
00:00:00からtime_stampまでの合計秒数を返す関数、convert_time_stamp()を実装せよ
また、いずれかの引数の型が違った場合はNoneを返すこと
time_stamp自体のフォーマットが崩れている場合は想定しなく良いとする

実行例
> print(convert_time_stamp('00:01:16'))
> 76

> print(convert_time_stamp(123))
> None
"""
def convert_time_stamp(time_stamp):
    """
    Args:
        time_stamp (str): HH:MM:SS形式の時刻を示す文字列
    Returns:
        int: 00:00:00からtime_stampまでの合計秒数
    """
    count = 0
    result = 0

    data = time_stamp.split(':')
    for i in data:
        if count == 0:
            result += int(i[0])*36000 + int(i[1])*3600
            count += 1
        elif count == 1:
            result += int(i[0])*600 + int(i[1])*60
            count += 1
        elif count == 2:
            result += int(i[0])*10 + int(i[1])
            count = 0

    return result


"""
問題3
タイプをKey、対応する行のリストをValueとする辞書を返す関数、generate_dict()を実装せよ
また、いずれかの引数の型が違った場合はNoneを返すこと

ヒント: list = data.split('\n') で行ごとに区切ったリストが手に入る
実行例
> print(generate_dict(data))
> {'A': ['00:00:00 A 40', '01:25:03 A 4', '01:33:20 A 7'], 'B': ['00:00:06 B 1', '00:12:26 B 21', '00:13:06 B 34'], 'AB': ['00:00:06 AB 5', '00:01:16 AB 2', '00:12:02 AB 4', '01:24:41 AB 5']}

> print(generate_dict(123))
> None
"""
def generate_dict(data):
    """
    Args:
        data (str): 解析対象データ
    Returns:
        dict: タイプをKey、対応する行のリストをValueとする辞書
    """
    result = {}
    a = []
    b = []
    c = []
    list = data.split('\n')
    for i in list:
        if 'A' in i and not 'AB' in i:
            a.append(i)
        elif 'B' in i and not 'AB' in i:
            b.append(i)
        elif 'AB' in i:
            c.append(i)

    result['A'] = a
    result['B'] = b
    result['AB'] = c            

    return result
"""
問題4
特定のタイプの行の数値を全て合計したものを返す関数count_total()を実装せよ
また、いずれかの指定したタイプの行がなかった場合は0を返し、引数の型が違った場合はNoneを返すこと

実行例
> print(count_total(data, 'B'))
> 56

> print(count_total(data, 'C'))
> 0

> print(count_total(123, 456))
> None
"""
def count_total(data, data_type):
    """
    Args:
        data (str): 解析対象データ
        data_type (str): カウントしたいタイプ
    Returns:
        int: 特定のタイプのデータの行の数値の合計(数字)
    """
    

    
"""
問題5
タイプをKeyとして、そのタイプの行の数値の全ての合計をValueとする辞書を返す関数、generate_total_dict()を実装せよ
また、いずれかの引数の型が違った場合はNoneを返すこと

ヒント: generate_dict()とcount_total()を再利用すると楽
実行例
> print(generate_total_dict(data))
> {'A': 51, 'B': 56, 'AB': 16}

> print(generate_total_dict(123))
> None
"""
def generate_total_dict(data):
    """
    Args:
        data (str): 解析対象データ
    Returns:
        dict: タイプをKeyとして、数値の合計をValueとする辞書
    """
    pass


if __name__ == '__main__':
    # この中は自由にデバッグに使って良い

    # 以下、実行例と同じものを羅列しておく
    print(count_type(data, 'A'))
    print(count_type(data, 'C'))
    #print(count_type(123, 456))
    print(convert_time_stamp('00:01:16'))
    #print(convert_time_stamp(123))
    print(generate_dict(data))
    # print(generate_dict(123))
    # print(count_total(data, 'B'))
    # print(count_total(data, 'C'))
    # print(count_total(123, 456))
    # print(generate_total_dict(data))
    # print(generate_total_dict(123))
    pass
