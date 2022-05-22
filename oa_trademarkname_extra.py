import pandas as pd
import re
import urllib.request

import pandas as pd
import time
import urllib.request
import xmltodict, json



def making_registrationNumber(registrationNum):
    print('before_registrationNum: {}'.format(registrationNum))
    if len(registrationNum) == 5:
        a = '40' + '00' + str(registrationNum) + '0000'
        b = '41' + '00' + str(registrationNum) + '0000'
        c = '45' + '00' + str(registrationNum) + '0000'
    elif len(registrationNum) == 6:
        a = '40' + '0' + str(registrationNum) + '0000'
        b = '41' + '0' + str(registrationNum) + '0000'
        c = '45' + '0' + str(registrationNum) + '0000'

    return a,b,c

def applicationNumber_Crawling(registrationNum):
    regi_url = "http://plus.kipris.or.kr/openapi/rest/RegistrationService/registrationInfo?registrationNumber={}&accessKey={}".format(registrationNum, api_key)
    response_regi = urllib.request.urlopen(regi_url)
    responseData_regi = response_regi.read()
    responseData_regi = xmltodict.parse(responseData_regi)
    responseData_regi = json.dumps(responseData_regi)
    responseData_regi = json.loads(responseData_regi)
    applicationNumber = responseData_regi['response']['body']['items']['registrationInfo']['registrationRightInfo']['applicationNumber']
    return applicationNumber


def trademarkName_Crawling(applicationNumber):
    name_url = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkBiblioSummaryInfo?applicationNumber={}&accessKey={}".format(applicationNumber, api_key)
    response_name = urllib.request.urlopen(name_url)
    responseData_name = response_name.read()
    responseData_name = xmltodict.parse(responseData_name)
    responseData_name = json.dumps(responseData_name)
    responseData_name = json.loads(responseData_name)

    korean = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo']['TrademarkHangeulName']
    english = responseData_name['response']['body']['items']['trademarkBiblioSummaryInfo']['TrademarkEnglishsentenceName']

    return korean, english


api_key = 'ruMJXj8dyeXNbq6B/ri9S1hHYDDVKvfesIfjyTlUId0='

sim_df = pd.DataFrame(columns=['patent_id', 'korean', 'english','rejectionContentDetail','registrationNumber','sim_applicationNumber','sim_korean','sim_english'])
date =pd.read_csv('date.csv')



for d in range(len(date)):
    startdate = date['start'][d]
    enddate = date['end'][d]

    readfilename = 'pre_{}_{}_0.csv'.format(startdate, enddate)
    writefilename = 'sim_{}_{}.csv'.format(startdate, enddate)

    raw = pd.read_csv('./(1)Preprocessingdata2/{}'.format(readfilename), engine='python')
    sim_index = raw.query('칭호 ==1').index.tolist()


    for nn, s in enumerate(sim_index):

        processpoint = (int(nn) / int(len(sim_index))) * 100

        print('\033[31m'+str(startdate)+'_'+str(enddate)+':'+"%0.1f%%" % processpoint + '\033[0m')
        applicationNumber = raw['patent_id'][s]
        korean = raw['korean'][s]
        english = raw['english'][s]
        rejectionContentDetail = str(raw['rejectionContentDetail'][s])
        numbers = re.findall("\d+", rejectionContentDetail)  ## 문자열내 숫자 추출
        numbers = list(map(int, numbers))  ##list 내의 문자->숫자형으로 변경
        sim_number = [x for x in numbers if x >= 10000 and x < 1000000]
        if sim_number != 0:
            for sn in sim_number:
                registrationNum = making_registrationNumber(str(sn))

                for num in registrationNum:

                    try:
                        sim_applicationNumber = applicationNumber_Crawling(num)
                        print('registrationNumber:{}, applicationNumber:{}'.format(num, sim_applicationNumber))
                        sim_korean = trademarkName_Crawling(sim_applicationNumber)[0]
                        sim_english = trademarkName_Crawling(sim_applicationNumber)[1]
                        sim_df = sim_df.append(
                            pd.DataFrame([[applicationNumber, korean, english, rejectionContentDetail,
                                           num, sim_applicationNumber, sim_korean, sim_english]],
                                         columns=['patent_id', 'korean', 'english',
                                                  'rejectionContentDetail', 'registrationNumber',
                                                  'sim_applicationNumber',
                                                  'sim_korean', 'sim_english']), ignore_index=True)
                        sim_df.to_csv(writefilename, header=True, index=False, encoding='euc-kr')
                    except:
                        print('None_registrationNumber:{}'.format(num))



