import csv
import pandas as pd 

# with open('test.csv', 'r', encoding='shift_jis') as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
#     for row in csv_reader:
#         print(','.join(row))

df = pd.read_csv('test.csv', encoding='cp932')
df_del = df.rename(columns={'Unnamed: 0':'順位'})
df_del = df_del.rename(columns={'勝利':'win'})
df_del = df_del.rename(columns={'選手名':'name'})

df_del = df_del.drop(['順位', 'チーム', '防御率', '試合', '敗北', 'セlブ', 'ホlルド', '勝率', '打者', '投球回', '被安打', '被本塁打', '与四球', '与死球', '奪三振', '失点', '自責点', 'WHIP', 'DIPS', 'Year'], axis=1)

df_del = df_del[df_del['name'] != '選手名']
df_del['win'] = df_del['win'].astype(str).astype(int)

df_del = df_del.set_index('name')['win']
df_del = df_del.groupby('name').sum()

player_dict = df_del.to_dict()

player_dict = sorted(player_dict.items(), key = lambda x: x[1], reverse=True)        
print(player_dict)

