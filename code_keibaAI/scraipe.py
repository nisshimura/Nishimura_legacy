from cgi import test
from csv import excel
from unittest import result
import pandas as pd
import time
from tqdm  import tqdm
url = "https://db.netkeiba.com/race/201901020909/"

def scrape_race_results(race_id_list):
    race_results={}
    for race_id in tqdm(race_id_list):
        try:
            url = "https://db.netkeiba.com/race/"+race_id
            race_results[race_id] = pd.read_html(url)[0]
            time.sleep(0.1)
        except IndexError:
            race_id_list.remove(race_id)
            print(f"\nremove {race_id}\n")
        except:
            print("break")
            break

    return race_results

race_id_list = []


# for place in range(1, 3):
#     for kai in range(1, 3):
#         for day in range(1, 3):
#             for r in range(1, 3):
#                 race_id = f"2019{str(place).zfill(2)}{str(kai).zfill(2)}{str(day).zfill(2)}{str(r).zfill(2)}"
#                 race_id_list.append(race_id)

for place in range(1,11):
    for kai in range(1,6):
        for day in range(1,13):
            for r in range(1,13):
                race_id = f"2019{str(place).zfill(2)}{str(kai).zfill(2)}{str(day).zfill(2)}{str(r).zfill(2)}"
                race_id_list.append(race_id)

test = scrape_race_results(race_id_list)

for key in test.keys():
    test[key].index = [key]*len(test[key])

results = pd.concat([test[key] for key in test.keys()],sort=False)
results.to_pickle("./data/Pickel/2019.pickle")

print(pd.read_pickle("./data/Pickel/2019.pickle"))
