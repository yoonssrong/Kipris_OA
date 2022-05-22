import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/3차/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(3)_1_Learningdata/3차/'

Label_0 = pd.read_csv(inputpath + 'Label_0.csv', encoding='cp949')
Label_1 = pd.read_csv(inputpath + 'Label_1.csv', encoding='cp949')
Label_2 = pd.read_csv(inputpath + 'Label_2.csv', encoding='cp949')
output = pd.DataFrame()

print('Label_0 : ', len(Label_0))
print('Label_1 : ', len(Label_1))
print('Label_2 : ', len(Label_2))

# 샘플링 후 스플릿할 경우
# samp_0 = Label_0.sample(n=23200)
# samp_1 = Label_1.sample(n=23200)
# samp_2 = Label_2.sample(n=23200)
#
# Learning = samp_0.append([samp_1, samp_2])

# 전체에서 스플릿할 경우
Learning = Label_0.append([Label_1, Label_2])

# Shuffle
Learning = Learning.sample(frac=1).reset_index(drop=True)

# Partitioning
Train = Learning.sample(frac=0.8)
Test = Learning.drop(Train.index)

# root 생성
if not os.path.isdir(savepath):
    os.mkdir(savepath)

Train.to_csv(savepath + "Train.csv", index=False, encoding='cp949')
Test.to_csv(savepath + "Test.csv", index=False, encoding='cp949')

print(len(Train))
print(len(Test))