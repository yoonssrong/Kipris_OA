import os
import pandas as pd


pd.set_option('display.max_colwidth', -1)

rawpath = 'D:/project/KPRIS_OA_1999_2020/(1)Preprocessingdata2/'
savepath = 'D:/project/KPRIS_OA_1999_2020/sim/'
rawfiles = os.listdir(rawpath)
pre_all = pd.DataFrame()

for rawfile in rawfiles:
    pre = pd.read_csv(rawpath + rawfile, encoding='cp949')
    pre_all = pd.concat([pre_all, pre])

pre_all = pre_all[['patent_id', 'korean', 'english', 'rejectionContentDetail']]
pre_all.drop_duplicates(inplace=True)


path = 'D:/project/KPRIS_OA_1999_2020/(0)OArawdata2/2002 OA.csv'
file = pd.read_csv(path, encoding='cp949')
file.drop_duplicates(inplace=True)
file = file.drop(['patent_id'], axis=1)

df = file.merge(pre_all[['patent_id', 'korean', 'english', 'rejectionContentDetail']], how='left')
df = df[['patent_id', 'korean', 'english', 'rejectionContentDetail', 'registrationNumber', 'sim_applicationNumber', 'sim_korean', 'sim_english']]

df.to_csv(savepath + '2002 OA.csv', index=False, encoding='cp949')

print(len(file))
print(len(df))
