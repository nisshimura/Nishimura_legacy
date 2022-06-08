import pandas as pd
def orthopedy(results):
    df = results.copy()
    df = df[~(df["着順"].astype(str).str.contains("\D"))]
    df["着順"] = df["着順"].astype(int)
    df["性"] = df["性齢"].map(lambda x:str(x)[0])

    df["年齢"] = df["性齢"].map(lambda x:str(x)[1:]).astype(int)


    df["体重"] = df["馬体重"].str.split("(", expand=True)[0].astype(float)
    df["体重変化"]=df["馬体重"].astype(str).str.split("(", expand=True)[1].str[:-1].astype(int)

    df["単勝"]= df["単勝"].astype(float)

    df.drop(["タイム","着差", "調教師", "性齢", "馬体重"],axis=1,inplace=True)

    return df


results = pd.read_pickle("./data/Pickel/2019.pickle")
df = orthopedy(results)
df.to_pickle("./data/Pickel/2019_orthoped.pickle")
