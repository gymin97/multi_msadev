from flask import Flask
import json
import requests
import pandas as pd
# 변수선언 - 프로그램의 이름 저장한느 변수 (파일이름 저장 변수)
# application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작 기본값 = app.py 파일을 생성

# 함수선언 
# 시작할때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로를 저장 
def FlaskLab():
    return 'flask 데이터 응답'

@app.route("/data1")
def FlaskData():#startPage, pageCount, address): # 요청받음
    keyValue = r'%2FH2rHG%2FJ95hTADJiUQJ4QzpBbdHCE4CBYf7V6AjSaiNSKM7uePItX0GmBO3vrJL7Q5JHigKGc0%2FXId%2B3S2m0dQ%3D%3D'

    # url 만들기
    # http://api.odcloud.kr/api/apnmOrg/v1/list?
    # page=1&perPage=10
    # &cond%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC
    # &serviceKey=%2FH2rHG%2FJ95hTADJiUQJ4QzpBbdHCE4CBYf7V6AjSaiNSKM7uePItX0GmBO3vrJL7Q5JHigKGc0%2FXId%2B3S2m0dQ%3D%3D
    dataURL = 'https://api.odcloud.kr/api/apnmOrg/v1/list?'
    dataURL += 'page='+str(1) + '&perPage=' + str(10)
    dataURL += '&cond' + r'%5BorgZipaddr%3A%3ALIKE%5D=%EA%B0%95%EB%82%A8%EA%B5%AC' # 지역
    dataURL += '&serviceKey=' + keyValue

    dataResult = requests.get(dataURL)
    data = json.loads(dataResult.text)['data']

    return str(data) # 공공데이터 결과값 응답
