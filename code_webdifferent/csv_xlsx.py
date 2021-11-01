import pandas as pd

File = "C:\programing\Atom_collection\code_webdifferent\【&mall】2020年3月リニューアル静的ページ一覧 (3).xlsx"

df = pd.read_excel(File,sheet_name=0,index_col=None)
df.to_csv("C:\programing\Atom_collection\code_webdifferent\\fixer.csv",encoding='utf-8')