import urllib.request
from tqdm import tqdm
import pandas as pd
import time
import urllib.request
import xmltodict, json
import re

##html 제거
def remove_tag(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext


timesleep = 0.7
api_key = 'JNDlhXxeBGqzOEcqzllBnTAFlQss1EdWy=jWFjqRI=4='

date =pd.read_csv('D:/KPRIS_OA_1999_2020/date.csv')
NonIntermediateDocumentapplicationNumber =[]
IntermediateDocumentapplicationNumber=[]

error_df = pd.DataFrame(columns=['patent_id', 'error'])

## 연도 변경시 시작할 페이지 번호 0 지정
# text = open('./rejectionDetail_error_page.txt', mode='wt', encoding='utf-8')
# text.write(str(0))
# text.close()
text = open('D:/KPRIS_OA_1999_2020/rejectionDetail_error_page.txt', mode='r')
x = text.readline()
text.close()
x = int(x)

for d in range(len(date)):

    ## 연도별 반복문 진행
    startdate = date['start'][d]
    enddate = date['end'][d]
    filename = f'{startdate}_{enddate}_{x}.csv'
    error_filename = f'error_{startdate}_{enddate}.csv'
    df = []
    df = pd.DataFrame(columns=['patent_id', 'page_num','korean','english','rejectionContentDetail'])



    response = urllib.request.urlopen(
        'http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch?applicationDate=' + str(
            startdate) + '~' + str(
            enddate) + '&application=true&refused=true&expiration=true&withdrawal=true&publication=true&cancel=true&abandonment=true&trademark=true&serviceMark=true&trademarkServiceMark=true&businessEmblem=true&collectiveMark=true&internationalMark=true&character=true&figure=true&compositionCharacter=true&figureComposition=true&totalCount=1&ServiceKey=gsR1vZ00RvZGu=1lsEtKL2CE7BD0AjJda1n=odrfN7Q=')
    time.sleep(timesleep)
    responseData = response.read()
    responseData = xmltodict.parse(responseData)
    responseData = json.dumps(responseData)
    responseData = json.loads(responseData)

    totalCount = responseData['response']['count']['totalCount']
    # 특정기간
    # i = page num


    for i in tqdm(range(x, (int(totalCount) // 20) + 1)):

        try:
            ## error시 다시 시작할 페이지번호 저장
            text = open('./rejectionDetail_error_page.txt', 'w')
            text.write(str(i))
            text.close()

            print('page number:', i)
            url = 'http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch?applicationDate=' + str(
                startdate) + '~' + str(
                enddate) + '&application=true&refused=true&expiration=true&withdrawal=true&publication=true&cancel=true&abandonment=true&trademark=true&serviceMark=true&trademarkServiceMark=true&businessEmblem=true&collectiveMark=true&internationalMark=true&character=true&figure=true&compositionCharacter=true&figureComposition=true&numOfRows=20&pageNo=' + str(
                i + 1) + '&ServiceKey=' + str(api_key)
            response = urllib.request.urlopen(url)
            time.sleep(timesleep)
            responseData = response.read()
            responseData = xmltodict.parse(responseData)
            responseData = json.dumps(responseData)
            responseData = json.loads(responseData)
            # j = page별 문서개수(최대 20개)
            for j in range(20):  # 20 말고 해당 페이지 개수로 변경, 20개 고정이라 20으로함
                applicationNumber = responseData['response']['body']['items']['item'][j]['applicationNumber']

                # rejectionContentDetail crawling(거절내용 가져오기)_)

                print(applicationNumber)
                url = "http://plus.kipris.or.kr/openapi/rest/IntermediateDocumentOPService/rejectDecisionInfo?applicationNumber=" + str(
                    applicationNumber) + "&accessKey=" + str(api_key)

                response_contents = urllib.request.urlopen(url)
                time.sleep(timesleep)
                responseData_contents = response_contents.read()
                responseData_contents = xmltodict.parse(responseData_contents)
                responseData_contents = json.dumps(responseData_contents)
                responseData_contents = json.loads(responseData_contents)

                name_url = f"http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkBiblioSummaryInfo?applicationNumber={applicationNumber}&accessKey={api_key}"
                response_name = urllib.request.urlopen(name_url)
                time.sleep(timesleep)
                responseData_name = response_name.read()
                responseData_name = xmltodict.parse(responseData_name)
                responseData_name = json.dumps(responseData_name)
                responseData_name = json.loads(responseData_name)

                korean = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo'][
                    'TrademarkHangeulName']
                english = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo'][
                    'TrademarkEnglishsentenceName']

                if not responseData_contents['response']['body']['items'] == None:

                    if type(responseData_contents['response']['body']['items']['rejectDecisionInfo']) == dict:

                        rejectionContentDetail = remove_tag(
                            responseData_contents['response']['body']['items']['rejectDecisionInfo'][
                                'rejectionContentDetail'])
                        df = df.append(pd.DataFrame([[applicationNumber, i, korean, english, rejectionContentDetail]],
                                                    columns=['patent_id', 'page_num', 'korean', 'english',
                                                             'rejectionContentDetail']), ignore_index=True)
                        df.to_csv(filename, header=True, index=False, encoding='euc-kr')

                    elif type(responseData_contents['response']['body']['items']['rejectDecisionInfo']) == list:

                        for k in range(len(responseData_contents['response']['body']['items']['rejectDecisionInfo'])):
                            rejectionContentDetail = remove_tag(
                                responseData_contents['response']['body']['items']['rejectDecisionInfo'][k][
                                    'rejectionContentDetail'])
                            df = df.append(
                                pd.DataFrame([[applicationNumber, i, korean, english, rejectionContentDetail]],
                                             columns=['patent_id', 'page_num', 'korean', 'english',
                                                      'rejectionContentDetail']),
                                ignore_index=True)
                            df.to_csv(filename, header=True, index=False, encoding='euc-kr')




        except Exception as ex:
            error_df = error_df.append(pd.DataFrame([[applicationNumber, ex]], columns=['patent_id', 'error']),
                                       ignore_index=True)
        error_df.to_csv(error_filename, header=True, index=False, encoding='euc-kr')
