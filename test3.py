# 트레인 테스트 개수가 안맞는데..? 확인해봐라

import os
import pandas as pd


# inputpath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/2차/'
#
# label0 = pd.read_csv(inputpath + 'Label_0.csv', encoding='cp949')
# label1 = pd.read_csv(inputpath + 'Label_1.csv', encoding='cp949')
# label2 = pd.read_csv(inputpath + 'Label_2.csv', encoding='cp949')
#
# label0 = label0[:100]
# label1 = label1[:50]
# label2 = label2[:50]
#
# df = label0.append([label1, label2])
#
# print(df)
#
# df.to_csv("./(4)검수후.csv", index=False, encoding='cp949')


inputpath = 'D:/project/KPRIS_OA_1999_2020/(0)OArawdata/'

files = os.listdir(inputpath)

search = pd.read_csv('D:/project/KPRIS_OA_1999_2020/(4)검수후.csv', encoding='cp949')
search = search["patent_id"]

all_OA = pd.DataFrame()
for file in files:
    raw = pd.read_csv(inputpath + file, encoding='cp949')
    all_OA = pd.concat([all_OA, raw])

output = pd.DataFrame()
for id in search:
    target = all_OA.loc[all_OA["patent_id"] == id, :]
    output = pd.concat([output, target])

print(output)
output.to_csv("./(4)원천데이터.csv", index=False, encoding='cp949')