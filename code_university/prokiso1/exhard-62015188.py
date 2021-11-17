"""
ファイル名の00000000を学籍番号に置き換えて提出すること

中間課題：五目並べを作ろう
なお、print_board()とmain()関数の中身についてはデバッグ用とし、採点には関わらないものとする
"""

def initialize_board(n):
    """
    盤面を初期化して返す関数
    
    盤面を初期化して返す。
    もし引数nが5未満である場合は、以下n=5として扱うものとする

    盤面は n+2 x n+2 の2次元リストとし、ある(x,y)の位置のマスはlist[y][x] (list名は適当) で表すものとする。
    このリストにはゲームで使わないマスに-1を、石が置いていないマスに0を、白石が置いてあるマスには1を、黒石が置いてあるマスには2を入れるとする。
　　初期化時は中央の n x n は0で、それ以外は-1で埋めておくものとする。
    (これはリストのインデックスの位置を直感的にするとともに、盤面の端を明確にするための処置である)

    Args:
        n (num): 盤面の長さ。5未満であれば内部ではn=5として初期化を行う

    Returns:
        list: n+2 x n+2 の2次元リスト
    """

    board = []
    if n <= 5:
        n = 5
    
    for i in range(n+2):
        line_list = []
        if i == 0 or i == n+1:
            for index in range(n+2):
                line_list.append(-1)
        else:
            for index in range(n+2):
                if index == 0  or index == n+1:
                    line_list.append(-1)
                else:
                    line_list.append(0)

        board.append(line_list)
    print(board)
    return board

def print_board(board):
    """
    盤面を表示する関数
    石がない場所は'*'、白石は'W'、黒石は'B'とし、横方向にはマスとマスの間に半角スペースを置き、ゲームに使わないマスはそもそも何も表示しない
    例えば以下のように表示される
    * * * * * * * *
    * * * * * * * *
    * * * W * * * *
    * * * B B W * *
    * * * * * B * *
    * * * * * * * *
    * * * * * * * *
    * * * * * * * *

    Args:
        board(2次元リスト): 盤面の2次元リスト

    Returns:
        なし
    """

    board_text = ''
    for i in board:
        for index in i:
            if index == 0:
                board_text += '*'
            elif index == -1:
                pass
            else:
                board_text += index
            board_text += ' '
        board_text += '\r\n'
    
    print(board_text)
            

    
def rival_player_num(player_num):
    """
    相手のプレイヤー番号を返す

    白が1、黒が2として、現在のプレイヤー番号が1なら2を、2なら1を返す
    それ以外のプレイヤー番号が引数に与えられたら-1を返す

    Args:
        player_num(int): 現在のプレイヤー番号

    Returns:
        int: 相手のプレイヤー番号
    """
    if player_num == 1:
        return 2
    elif player_num == 2:
        return 1
    else:
        return -1

def check_availablity_all(board):
    """
    盤面に石を置ける場所があるかどうかを確認

    Args:
        board(2次元リスト): 盤面の2次元リスト

    Return:
        is_available(bool): 石を置けるかどうか
    """
    for index in board:
        if 0 in index:
            return True
    return False

def check_availability(board, x, y):
    """
    石をおけるかどうか確認する関数

    Args:
        board(2次元リスト): 盤面の2次元リスト
        x(int): 石を置くx座標
        y(int): 石を置くy座標

    Return:
        bool: 石を置けるかどうか
    """

    if len(board) <= x or len(board[0]) <= y:
        return False
    if board[y][x] == 0:
        return True
    else:
        return False

def put_disc(board, player_num, x, y):
    """
    石を置き、新しい盤面を返す
    player_numの石を(x,y)に石を置き、新しい盤面を返す

    Args:
        board(2次元リスト): 盤面の2次元配列
        player_num(int): 石を置くプレイヤー番号
        x(int): 石を置くx座標
        y(int): 石を置くy座標

    Returns:
        list: 新しい盤面を表す2次元配列
    """

    if player_num == 1:
        board[y][x] = 'W'
    elif player_num == 2:
        board[y][x] = 'B'
    
    return board

def check_five_row(board, x, y):
    """石が5個並んだかチェックする
    
    盤面を示す二次元配列boardのうち、(x,y)を含む縦横斜めで石が5個並んでいるかをチェックする
    1 まずboard[y][x]に石がない場合はNoneを返して関数を終了する
    2 board[y][x]の石の色を仮にplayer_numとしておく
    3 縦方向についてチェックする。board[y][x]からy方向に+1ずつずらし、 player_numと違う数字が出るまでのマスの数を記憶する。同様にy方向に-1ずつずらした場合のマスの数も記憶する。「この2つの数字の合計 + 1(中央の石の分) >= 5」であればTrueを返して関数を終了する
    4 横方向について同様にチェックする。 (board[y][x]からx方向に+1ずつずらしたものと、-1ずつずらせば良い)
    5 斜め方向(左上から右下方向)について同様にチェックする。(board[y][x]からy方向に-1、x方向に-1ずつしたものと、y方向に+1、x方向に+1ずつしたものについて、それぞれplayer_numと違う数字が出るまでのマスの数を数えていけば良い)
    6 斜め方向(右上から左下方向)について同様にチェックする。(board[y][x]からy方向に+1、x方向に-1ずつしたものと、y方向に-1、x方向に+1ずつしたものについて、それぞれplayer_numと違う数字が出るまでのマスの数を数えていけば良い)
    7 最後にFalseを返す。(以上の処理が終わってもまだ関数が続いているということは石が5個並んでいなかったということなので)

    Args:
        board(2次元リスト): 盤面の2次元配列
        x(int): 確認対象のx座標
        y(int): 確認対象のy座標

    Returns:
        bool or None: 石が5個並んでいたらTrue, そうでないならFalse, board[y][x]に石が置いてないならNone
    """
    if board[y][x] == -1 or board[y][x] == 0:
        return None, None
    player_num = board[y][x]
    
    line_count = 0
    add = 1
    mainus = 1

    while True:
        if board[y+add][x] == -1:
            add = 1
            break
        if board[y+add][x] == player_num:
            line_count += 1
            add += 1
        else:
            add = 1
            break

    while True:
        if board[y-mainus][x] == -1:
            mainus = 1
            break
        if board[y-mainus][x] == player_num:
            line_count += 1
            mainus += 1
        else:
            mainus = 1
            break

    if line_count + 1 >= 5:
        return True, player_num

    row_count = 0
    while True:
        if board[y][x+add] == -1:
            add = 1
            break
        if board[y][x+add] == player_num:
            row_count += 1
            add += 1
        else:
            add = 1
            break

    while True:
        if board[y][x-mainus] == -1:
            mainus = 1
            break
        if board[y][x-mainus] == player_num:
            row_count += 1
            mainus += 1
        else:
            mainus = 1
            break

    if row_count + 1 >= 5:
        return True, player_num
    
    right_slanting_count = 0

    while True:
        if board[y+add][x+add] == -1:
            add = 1
            break
        if board[y+add][x+add] == player_num:
            right_slanting_count += 1
            add += 1
        else:
            add = 1
            break

    while True:
        if board[y-mainus][x-mainus] == -1:
            mainus = 1
            break
        if board[y-mainus][x-mainus] == player_num:
            right_slanting_count += 1
            mainus += 1
        else:
            mainus = 1
            break

    if right_slanting_count + 1 >= 5:
        return True, player_num

    left_slanting_count = 0
    while True:
        if board[y+add][x-add] == -1:
            add = 1
            break
        if board[y+add][x-add] == player_num:
            left_slanting_count += 1
            add += 1
        else:
            add = 1
            break

    while True:
        if board[y-mainus][x+mainus] == -1:
            mainus = 1
            break
        if board[y-mainus][x+mainus] == player_num:
            left_slanting_count += 1
            mainus += 1
        else:
            mainus = 1
            break

    if left_slanting_count + 1 >= 5:
        return True, player_num
    
    return False, None

def main():
    """
    ゲームの進行
    - initialize_board()で初期化したboardを用意する
    - print_board()する
    - 現在のプレイヤーの状態を記憶する変数(player_num等)を用意
       先攻は黒なので、最初は2としておく

    以下、無限ループ
    - 盤面に石を置ける場所があるかどうかを確認し，なければ引き分けと表示して終了，あれば以下に進む
    - player_numにあわせて今がどっちの手番なのか表示する
    - コンソールからx, yの座標を入力し(2回に分けたりしても良い)、石が置ける座標が打たれるまで無限ループする
    - 石を置ける座標が入力されたら、put_disc()の返り値の新しい盤面で現在の盤面を上書きし、print_board()する
    - 縦横斜めに石が5つ以上並んでいるかどうかを確認し，並んでいれば勝ったプレイヤーを表示して，終了
    - プレイヤーを入れ替える

    Returns:
        なし
    """
    size = 7
    player_num = 2
    board = initialize_board(size)
    print_board(board)
    while True:
        if check_availablity_all(board) == True:
            pass
        else:
            print('引き分け')
            break
        if player_num == 1:
            print('This is White turn')
        elif player_num == 2:
            print('This is Black turn')
        while True:
            try:
                line = int(input('x:'))
                row = int(input('y:'))
                if check_availability(board, line, row) == True:
                    break
                else:
                    print('you cant put there')
                    pass
            except:
                print('you cant put there')
                pass

        new_board = put_disc(board,player_num,line,row)
        board = new_board
        print_board(board)
        result, winner = check_five_row(board, line, row)
        if result == True:
            if winner == 'W':
                print('White is WINNER!!')
            elif winner == 'B':
                print('Black is WINNER!!')
            break

        player_num = rival_player_num(player_num)


if __name__ == "__main__":
    main()
