import os
import pandas as pd
import re

# 최대 줄 수 설정
pd.set_option('display.max_rows', 500)
# 최대 열 수 설정
pd.set_option('display.max_columns', 500)
# 표시할 가로의 길이
pd.set_option('display.width', 1000)

inputpath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/1차/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(4)_검수후/2차/'


raw = pd.read_csv(savepath + 'Label_7.csv', encoding='cp949')

raw['rejectionContentDetail'] = [i.replace('<br>', '') for i in raw['rejectionContentDetail']]
raw['rejectionContentDetail'] = [i.replace('</br>', '') for i in raw['rejectionContentDetail']]

contents = raw['rejectionContentDetail']


output = []
for i, content in enumerate(contents):

    # if content.find('제7조 제1항 제7호') > 0 | content.find('칭호') == -1 | content.find('표장') == -1:
    #     print(content)
    # if content.find('제8조') > 0 | content.find('칭호') == -1 | content.find('표장') == -1:
    #     print(content)
    # if content.find('제34조 제1항 제7호') > 0 | content.find('칭호') == -1 | content.find('표장') == -1:
    #     print(content)
    # if content.find('제35조') > 0 | content.find('칭호') == -1 | content.find('표장') == -1:
    #     print(content)

    if content.find('관념') > 0 | content.find('칭호') == -1:
        # print(content)
        output.append(content)

print(output)
print(len(output))