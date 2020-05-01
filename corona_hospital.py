import requests
from bs4 import BeautifulSoup
import csv 

file = open("corona_hospital.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["city","district","hospital_name","phone_number"])


hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_list_box = hospital_soup.find("tbody",{"class":"tb_center"})
hospital_list = hospital_list_box.find_all("tr")


# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!
result=[]
for hospital in hospital_list:
    list1 = hospital.contents
    city = list1[1].string
    district = list1[2].string
    hospital_name = list1[3].text
    phone_number = list1[4].string
    hostpial_info = {
        'city': city, 
        'district':district,
        'hospital_name': hospital_name,
        'phone_number': phone_number,
    }
    result.append(hostpial_info)
    
print(hostpial_info)
for result_item in result:
    row=[]
    row.append(result_item['city'])
    row.append(result_item['district'])
    row.append(result_item['hospital_name'])
    row.append(result_item['phone_number'])
    writer.writerow(row)