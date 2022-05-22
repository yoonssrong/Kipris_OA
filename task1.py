# patent_id만 뽑아줘라

import os
import pandas as pd

PATH = 'D:/project/KPRIS_OA_1999_2020/(0)_1OArawdata/특허_OA/'
savePATH = 'D:/project/KPRIS_OA_1999_2020/(0)_1OArawdata/'

files = os.listdir(PATH)

output = pd.DataFrame()
for file in files:
    # df = pd.read_csv(PATH + file, encoding='cp949')
    df = pd.read_csv(PATH + file, engine='python')
    patent_id = df.iloc[:,0]
    # patent_id = df['patent_id']
    output = pd.concat([output, patent_id])
    print(file, len(df))

print(len(output))
output.to_csv(savePATH + "patent_id_특허.txt", index=False, header=None)