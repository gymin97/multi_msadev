# jsonlab06.py -> with => try  ~ except 까지 수정
# github = MSA20220121 / 김경민_jsonfile.py
import json

# 파일 읽기
try:    
    jsonFile = open('Datalab/mydata.json', 'rb') # rb !!
    tempData = json.load(jsonFile)
    resultData1 = tempData['name']
    resultData2 = tempData['age']
    resultData3 = tempData['address']
    resultData4 = tempData['email']
    resultData5 = tempData['empcheck']
except Exception as ex :
    print ('error: ',str(ex))
else:
    jsonFile.close()


# 파일 만들기
jsonData1 = {
    "empid" : 12345678,
    "name" : '홍길동',
    "info": [
        {'date1' : '2022-01-21', 'home' : '서울시'},
        {'dep' : '개발', 'email' : 'aaa@aaa.co.kr'}
    ],
     "empcheck": True
}

try:
    writeFile1 = open('Datalab/mydata1.json', 'w') 
    json.dump(jsonData1, writeFile1) # 옵션으로 indent = 숫자
except Exception as ex :
    print ('error: ',str(ex))
else:
    writeFile1.close()


try:
    writeFile2 = open('Datalab/mydata2.json', 'w', encoding="utf-8") 
    json.dump(jsonData1, writeFile2, ensure_ascii=False) # 옵션으로 indent = 숫자
except Exception as ex :
    print ('error: ',str(ex))
else:
    writeFile2.close()


try:
    writeFile3 = open('Datalab/mydata3.json', 'w') 
    json.dump(jsonData1, writeFile3, ensure_ascii=False, indent=4) # 옵션으로 indent = 숫자
except Exception as ex :
    print ('error: ',str(ex))
else:
    writeFile3.close()


try :
    writeFile4 = open('Datalab/mydata4.json', 'w', encoding = 'utf-8' )  # 한글 이용시 - 파일 읽을떄 utf-8, dump 할때 ensure_ascii = False
    json.dump(jsonData1, writeFile4, ensure_ascii= False, indent=4) 
except Exception as ex :
    print ('error: ',str(ex))
else:
    writeFile4.close()


tmp = 0