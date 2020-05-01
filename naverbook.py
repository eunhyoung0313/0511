import requests
import csv
from bs4 import BeautifulSoup

file = open("naver_books.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "img_src", "link","author", "publisher"])


final_result=[]
for i in range (8):
    print(f'{i+1}번째 페이지 크롤링중..')
    book_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}')
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol",{"class" : "basic"})
    book_list = book_list_box.find_all("li")

    
    result =[]
    for book in book_list:
        title= book.find("a",{"class":"N=a:bta.title"}).text
        img_src=book.find("div",{"class": "thumb_type thumb_type2"}).find("img")["src"]
        link = book.find("a",{"class":"N=a:bta.title"})["href"]
        author =book.find("a", {"class": "txt_name N=a:bta.author"}).text
        publisher= book.find("a", {"class":"N=a:bta.publisher"}).text
        
       
        book_info = {
            'title': title,
            'img_src': img_src,
            'link': link ,
            'author': author   , 
            'publisher':publisher
        }
        result.append(book_info)
    final_result = final_result+ result

    for book in final_result:
         row=[]
         row.append(book['title'])
         row.append(book['img_src'])
         row.append(book['link'])
         row.append(book['author'])
         row.append(book['publisher'])
         writer.writerow(row)
        