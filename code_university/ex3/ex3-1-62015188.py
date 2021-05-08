"""
ファイル名の00000000を学籍番号に置き換えて提出すること
"""

"""
問1
コンソールから受け取った1つ目の文字列をint型に変換しageに代入、
2つ目の文字列をfloat型に変換しsightに代入するよう、?を適切を埋めよ
"""
age = int(input('age:'))
sight = float(input('sight:'))

"""
問2
年齢ageがlegal_driver_age以上かつ
視力sightがeligible_sight以上の場合に"普通免許の受験資格がある。"と表示され、
年齢ageがlegal_driver_age未満なら "運転は{legal_driver_age}歳から。"と表示され、
そうでなければ "年齢か視力が足りない。"と表示されるよう、?を適切に埋めよ
"""
legal_driver_age = 20
eligible_sight = 0.7

if age >= legal_driver_age and sight >= eligible_sight:
    print("普通免許の受験資格がある。")
elif age < legal_driver_age:
    print("運転は", legal_driver_age, "歳から。")
else:
    print("年齢か視力が足りない。")
