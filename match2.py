import os
import pandas as pd


pd.set_option('display.max_colwidth', -1)

# 번호따올곳
PATH = 'D:/project/KPRIS_OA_1999_2020/sim_trademarkName_19980101_20051231/'
files = os.listdir(PATH)
sim_all = pd.DataFrame()

for file in files[1:]:
    sim = pd.read_csv(PATH + file, encoding='cp949')
    sim_all = pd.concat([sim_all, sim])

sim_all.drop_duplicates(inplace=True)

target = pd.read_excel('D:/project/KPRIS_OA_1999_2020/sim_excel/1998 OA.xlsx', sheet_name='Sheet1')
target = target.drop(['registrationNumber'], axis=1)
target = target.drop(['sim_applicationNumber'], axis=1)

df = target.merge(sim_all[['patent_id', 'rejectionContentDetail', 'registrationNumber', 'sim_applicationNumber', 'sim_korean', 'sim_english']], how='left')
df = df[['patent_id', 'korean', 'english', 'rejectionContentDetail', 'registrationNumber', 'sim_applicationNumber', 'sim_korean', 'sim_english']]

savepath = 'D:/project/KPRIS_OA_1999_2020/sim_excel/'

df.to_excel(savepath + '1998 OA_test.xlsx', index=False, encoding='cp949')