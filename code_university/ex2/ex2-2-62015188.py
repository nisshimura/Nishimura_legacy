"""
ファイル名の00000000を学籍番号に置き換えて提出すること

演習2: 論理演算
"""

"""
問1: NAND回路と同じような演算を行うために、以下の?を適切な論理演算子に書き換えよ
input1, input2が入力であり、outputが出力になるものとする
(ヒント: NAND回路では論理積の否定を行う)
"""
input1 = True
input2 = True
output = not(input1 and input2)
print(output)


"""
問2: NOR回路と同じような演算を行うために、以下の?を適切な論理演算子に書き換えよ
input1, input2が入力であり、outputが出力になるものとする
(ヒント: NOR回路では論理和の否定を行う)
"""
input1 = False
input2 = False
output = not (input1 or input2)
print(output)

"""
問3: XNOR回路と同じような演算を行ってoutputに結果を入れよ
今回は論理演算、if文、論理式など好きなやり方で最終的にoutputに結果が入れば良い
input1, input2が入力であり、outputが出力になるものとする
(ヒント: XNOR回路ではinput1とinput2の真偽が同じときのみoutputが真となる)
"""
input1 = True
input2 = True
output = input1 == input2 #(input1 and input2) or not(input1 and input2)
print(output)
