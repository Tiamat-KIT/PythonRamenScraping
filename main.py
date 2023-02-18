import requests
from bs4 import BeautifulSoup
import csv
data_list = [["店名","住所","電話番号"]]

""" for i in range(10):
  url = "https://ramendb.supleks.jp/search?page="+ str(i) +"&state=ishikawa&city=%E9%87%8E%E3%80%85%E5%B8%82%E5%B8%82&station-id=0"
  csv_path = "test.csv"
  r = requests.get(url)
  soup = BeautifulSoup(r.content,"html.parser")
  before_data = ""
  store_list = []
  i = 0
  for el in  soup.find_all("h4"):
    if before_data == el.text:
      print("=====")
    else: 
      before_data = el.text
      for el2 in el.find_all("a"):
        r2 = requests.get("https://ramendb.supleks.jp" + el2.get("href"))
        soup2 = BeautifulSoup(r2.content,"html.parser")
        for el4 in soup2.find_all("tr",limit=3):
          for el6 in el4.find_all("td"):
            store_list.append(el6.text)
            i += 1
            if i == 3:
                data_list.append(store_list)
                i = 0
                store_list = [] """


url = "https://ramendb.supleks.jp/search?q=&state=ishikawa&city=%E9%87%91%E6%B2%A2%E5%B8%82&order=point&station-id=&type="
csv_path = "test2.csv"
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
before_data = ""
store_list = []
i = 0
for el in  soup.find_all("h4"):
  if before_data == el.text:
    print("=====")
  else: 
    before_data = el.text
    for el2 in el.find_all("a"):
      r2 = requests.get("https://ramendb.supleks.jp" + el2.get("href"))
      soup2 = BeautifulSoup(r2.content,"html.parser")
      for el4 in soup2.find_all("tr",limit=3):
        for el6 in el4.find_all("td"):
          store_list.append(el6.text)
          i += 1
          if i == 3:
              data_list.append(store_list)
              i = 0
              store_list = []

with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_list)
# https://ai-inter1.com/beautifulsoup_1/#st-toc-h-8
# https://www.sejuku.net/blog/51241
# https://yu-nix.com/archives/bs4-find-all/