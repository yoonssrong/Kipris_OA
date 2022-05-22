# 샘플링 50% 해라

import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/3차/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/3차_Sample_50%/'

# 칭호
Label_0 = pd.read_csv(inputpath + 'Label_0.csv', encoding='cp949')

# 관념
Label_1 = pd.read_csv(inputpath + 'Label_1.csv', encoding='cp949')

# 식별력
Label_2 = pd.read_csv(inputpath + 'Label_2.csv', encoding='cp949')

samp_0 = Label_0.sample(n=len(Label_0)//2)
samp_1 = Label_1.sample(n=len(Label_1)//2)
samp_2 = Label_2.sample(n=len(Label_2)//2)

samp_0.to_csv(savepath + "Label_0.csv", index=False, encoding='cp949')
samp_1.to_csv(savepath + "Label_1.csv", index=False, encoding='cp949')
samp_2.to_csv(savepath + "Label_2.csv", index=False, encoding='cp949')
