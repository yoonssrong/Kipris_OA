import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/1차/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(3)_1_Learningdata/TTA/'

# 칭호
Label_0 = pd.read_csv(inputpath + 'Label_0.csv', encoding='cp949')

# 관념
Label_1 = pd.read_csv(inputpath + 'Label_1.csv', encoding='cp949')
Label_3 = pd.read_csv(inputpath + 'Label_3.csv', encoding='cp949')
Label_3['label'] = 1
Label_3['rejectionContentDetail'] = [i.replace('칭호', '') for i in Label_3['rejectionContentDetail']]
Label_3['rejectionContentDetail'] = [i.replace('외관', '') for i in Label_3['rejectionContentDetail']]
Label_3['rejectionContentDetail'] = [i.replace('호칭', '') for i in Label_3['rejectionContentDetail']]
Label_3['rejectionContentDetail'] = [i.replace('표장', '') for i in Label_3['rejectionContentDetail']]

# 식별력
Label_2 = pd.read_csv(inputpath + 'Label_2.csv', encoding='cp949')

samp_0 = Label_0.sample(n=23000)
samp_1 = Label_3.sample(n=12148)
samp_2 = Label_2.sample(n=23000)

Learning = samp_0.append([Label_1, samp_1, samp_2])

# Shuffle
Learning = Learning.sample(frac=1).reset_index(drop=True)

# Partitioning
Train = Learning.sample(n=55200)
Test = Learning.drop(Train.index)

Train.to_csv(savepath + "Train.csv", index=False, encoding='cp949')
Test.to_csv(savepath + "Test.csv", index=False, encoding='cp949')

print("Learning :", len(Learning))
print("Train :", len(Train))
print("Test :", len(Test))
