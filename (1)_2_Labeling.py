import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(2)_1_Labelingdata/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(2)_2_Labelingdata/'

files = os.listdir(inputpath)

output = pd.DataFrame()
for file in files:
    raw = pd.read_csv(inputpath + file, encoding='cp949')
    raw = raw.drop(['칭호', '관념', '식별력'], axis=1)

    # raw = raw.iloc[:,[3, 7]]

    raw['label'] = [i.replace('칭호, 관념, 식별력', '6') for i in raw['label']]
    raw['label'] = [i.replace('칭호, 관념', '3') for i in raw['label']]
    raw['label'] = [i.replace('칭호, 식별력', '4') for i in raw['label']]
    raw['label'] = [i.replace('관념, 식별력', '5') for i in raw['label']]
    raw['label'] = [i.replace('칭호', '0') for i in raw['label']]
    raw['label'] = [i.replace('관념', '1') for i in raw['label']]
    raw['label'] = [i.replace('식별력', '2') for i in raw['label']]
    raw['label'] = [i.replace('기타', '7') for i in raw['label']]

    output = pd.concat([output, raw])

output.to_csv(savepath + "Label_all.csv", index=False, encoding='cp949')
