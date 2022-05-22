import os
import pandas as pd
import re
from tqdm import tqdm


inputpath = 'D:/project/KPRIS_OA_1999_2020/tmp_preprocessiong/'
savepath = 'D:/project/KPRIS_OA_1999_2020/tmp_preprocessiong2/'
files = os.listdir(inputpath)
files = files[7:8]
# files = tqdm(files)


for file in files:
    print(file)
    raw = pd.read_csv(inputpath + file, encoding='cp949')
    # raw = raw.drop(['page_num'], axis=1)

    for col in raw.columns:
        print(col)