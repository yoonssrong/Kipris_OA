import os
import re
import pandas as pd


path = 'D:/project/KPRIS_OA_1999_2020/(0)OArawdata2/'
savepath = 'D:/project/KPRIS_OA_1999_2020/(1)Preprocessingdata2/'
files = os.listdir(path)

for file in files:
    print(file)
    output = pd.DataFrame()
    raw = pd.read_csv(path + file, encoding='cp949')
    raw = raw.drop(['page_num'], axis=1)

    # 결측치 제거
    raw = raw.loc[raw['rejectionContentDetail'].isnull() == False]

    # rawdata전처리 : html문 제거
    raw['rejectionContentDetail'] = [i.replace('&', '') for i in raw['rejectionContentDetail']]
    raw['rejectionContentDetail'] = [i.replace('amp;', '') for i in raw['rejectionContentDetail']]
    raw['rejectionContentDetail'] = [i.replace('quot;', '') for i in raw['rejectionContentDetail']]
    raw['rejectionContentDetail'] = [i.replace('lt;', '') for i in raw['rejectionContentDetail']]
    raw['rejectionContentDetail'] = [i.replace('gt;', '') for i in raw['rejectionContentDetail']]
    raw['rejectionContentDetail'] = [i.replace('middot;', '') for i in raw['rejectionContentDetail']]

    # 분류를 위한 컬럼 생성
    raw['칭호'] = ''
    raw['관념'] = ''
    raw['식별력'] = ''
    raw['label'] = ''

    contents = raw['rejectionContentDetail']

    # 거절사유 분류
    for i, content in enumerate(contents):
        # 거절사유 칭호
        if content.find('제7조 제1항 제7호') > content.find('칭호') > 0:
            raw.iloc[i, 4] = 1
        if content.find('제8조') > content.find('칭호') > 0:
            raw.iloc[i, 4] = 1
        if content.find('제34조 제1항 제7호') > content.find('칭호') > 0:
            raw.iloc[i, 4] = 1
        if content.find('제35조') > content.find('칭호') > 0:
            raw.iloc[i, 4] = 1

        # 거절사유 관념
        if content.find('제7조 제1항 제7호') > content.find('관념') > 0:
            raw.iloc[i, 5] = 1
        if content.find('제8조') > content.find('관념') > 0:
            raw.iloc[i, 5] = 1
        if content.find('제34조 제1항 제7호') > content.find('관념') > 0:
            raw.iloc[i, 5] = 1
        if content.find('제35조') > content.find('관념') > 0:
            raw.iloc[i, 5] = 1

        # 거절사유 "식별력":
        if content.find('제6조') > 0:
            raw.iloc[i, 6] = 1
        if content.find('제33조') > 0:
            raw.iloc[i, 6] = 1

    # 라벨링
    for i in range(len(raw)):
        if raw.iloc[i, 4] == 1 and raw.iloc[i, 5] == 1 and raw.iloc[i, 6] == 1:
            raw.iloc[i, 7] = '칭호, 관념, 식별력'
        elif raw.iloc[i, 4] == 1 and raw.iloc[i, 5] == 1 and raw.iloc[i, 6] == '':
            raw.iloc[i, 7] = '칭호, 관념'
        elif raw.iloc[i, 4] == 1 and raw.iloc[i, 5] == '' and raw.iloc[i, 6] == '':
            raw.iloc[i, 7] = '칭호'
        elif raw.iloc[i, 4] == 1 and raw.iloc[i, 5] == '' and raw.iloc[i, 6] == 1:
            raw.iloc[i, 7] = '칭호, 식별력'
        elif raw.iloc[i, 4] == '' and raw.iloc[i, 5] == 1 and raw.iloc[i, 6] == 1:
            raw.iloc[i, 7] = '관념, 식별력'
        elif raw.iloc[i, 4] == '' and raw.iloc[i, 5] == 1 and raw.iloc[i, 6] == '':
            raw.iloc[i, 7] = '관념'
        elif raw.iloc[i, 4] == '' and raw.iloc[i, 5] == '' and raw.iloc[i, 6] == 1:
            raw.iloc[i, 7] = '식별력'
        else:
            raw.iloc[i, 7] = '기타'

    output = pd.concat([output, raw])

    # 분류결과 저장
    output.to_csv(savepath + "pre_" + file, index=False, encoding='cp949')

