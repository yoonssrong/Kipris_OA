# 검수 3차 : 전처리 수정 및 데이터 라벨링 축소(7->4) 작업

import os
import pandas as pd

inputpath = 'D:/project/KPRIS_OA_1999_2020/(2)_3_Labelingdata2/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/3차/'


Label_0 = pd.read_csv(inputpath + 'Label_0.csv', encoding='cp949')
Label_1 = pd.read_csv(inputpath + 'Label_1.csv', encoding='cp949')
Label_2 = pd.read_csv(inputpath + 'Label_2.csv', encoding='cp949')
Label_3 = pd.read_csv(inputpath + 'Label_3.csv', encoding='cp949')
Label_4 = pd.read_csv(inputpath + 'Label_4.csv', encoding='cp949')
Label_5 = pd.read_csv(inputpath + 'Label_5.csv', encoding='cp949')
Label_6 = pd.read_csv(inputpath + 'Label_6.csv', encoding='cp949')
Label_7 = pd.read_csv(inputpath + 'Label_7.csv', encoding='cp949')

# 칭호
re_Label_0 = Label_0.append([Label_3, Label_4, Label_6])
re_Label_0['label'] = 0
# re_Label_0['rejectionContentDetail'] = [i.replace('관념', '') for i in re_Label_0['rejectionContentDetail']]
# re_Label_0['rejectionContentDetail'] = [i.replace('식별력', '') for i in re_Label_0['rejectionContentDetail']]
# re_Label_0['rejectionContentDetail'] = [i.replace('표장', '') for i in re_Label_0['rejectionContentDetail']]

re_Label_0.to_csv(savepath + "Label_0.csv", index=False, encoding='cp949')
print(len(re_Label_0))

# 관념
re_Label_1 = Label_1.append([Label_3, Label_5, Label_6])
re_Label_1['label'] = 1
# re_Label_1['rejectionContentDetail'] = [i.replace('칭호', '') for i in re_Label_1['rejectionContentDetail']]
# re_Label_1['rejectionContentDetail'] = [i.replace('외관', '') for i in re_Label_1['rejectionContentDetail']]
# re_Label_1['rejectionContentDetail'] = [i.replace('호칭', '') for i in re_Label_1['rejectionContentDetail']]
# re_Label_1['rejectionContentDetail'] = [i.replace('표장', '') for i in re_Label_1['rejectionContentDetail']]
# re_Label_1['rejectionContentDetail'] = [i.replace('식별력', '') for i in re_Label_1['rejectionContentDetail']]

re_Label_1.to_csv(savepath + "Label_1.csv", index=False, encoding='cp949')
print(len(re_Label_1))

# 식별력
re_Label_2 = Label_2.append([Label_2, Label_4, Label_5, Label_6])
re_Label_2['label'] = 2
# re_Label_2['rejectionContentDetail'] = [i.replace('칭호', '') for i in re_Label_2['rejectionContentDetail']]
# re_Label_2['rejectionContentDetail'] = [i.replace('외관', '') for i in re_Label_2['rejectionContentDetail']]
# re_Label_2['rejectionContentDetail'] = [i.replace('호칭', '') for i in re_Label_2['rejectionContentDetail']]
# re_Label_2['rejectionContentDetail'] = [i.replace('표장', '') for i in re_Label_2['rejectionContentDetail']]
# re_Label_2['rejectionContentDetail'] = [i.replace('관념', '') for i in re_Label_2['rejectionContentDetail']]

re_Label_2.to_csv(savepath + "Label_2.csv", index=False, encoding='cp949')
print(len(re_Label_2))
