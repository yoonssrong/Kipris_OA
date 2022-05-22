import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(2)Labelingdata/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(3)Learningdata/4/'

Learning = pd.read_csv(inputpath + 'Label_all.csv', encoding='cp949')
output = pd.DataFrame()

# Learning = Learning[(Learning['label'] == 0) | (Learning['label'] == 1) | (Learning['label'] == 2) | (Learning['label'] == 7)] #원하는 Label case 가져오기
Learning = Learning[Learning['label'].isin([0, 1, 2])] # 원하는 Label case 가져오기

# Partitioning
Train = Learning.sample(frac=0.8)
Test = Learning.drop(Train.index)

Train.to_csv(savepath + "Train.csv", index=False, encoding='cp949')
Test.to_csv(savepath + "Test.csv", index=False, encoding='cp949')
