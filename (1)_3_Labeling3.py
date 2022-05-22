import os
import pandas as pd


PATH = 'D:/project/KPRIS_OA_1999_2020/(2)_3_Labelingdata2/'

raw = pd.read_csv(PATH + 'Label_all.csv', encoding='cp949')

for i in range(0,8):
    target = raw[raw['label'] == i]
    print('Label_{} :'.format(i), len(target))
    target.to_csv(PATH + 'Label_' + str(i) + '.csv', index=False, encoding='cp949')

print('Finish!')