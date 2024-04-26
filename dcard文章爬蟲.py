from sre_constants import JUMP
import pandas as pd
import requests
import re
import random
import time

headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
              "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
              "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]

ID = '238349108'
url = "https://www.dcard.tw/service/api/v2/posts/" + ID 
requ = requests.get(url, headers = {
    "user_agent" : random.choice(headerlist)
})
rejs = requ
print(rejs)
pd.DataFrame(
        data=
        [{'id':rejs['id'],
          '標題':rejs['title'],
          '內文':rejs['content'],
          '回應數量':rejs['commentCount'],
          '發文時間':rejs['createdAt'],
          '愛心數量':rejs['likeCount'],
          '標註':rejs['topics'],
          '分類':rejs['forumName']}],
        columns=['id','標題','內文','回應數量','發文時間','愛心數量','標註','分類'])

# def Crawl(ID):
#     link = 'https://www.dcard.tw/service/api/v/posts/' + str(ID)
#     requ = requests.get(link, headers = {
#     "user_agent" : random.choice(headerlist)
#   })
#     rejs = requ.json()
#     return(pd.DataFrame(
#         data=
#         [{'id':rejs['id'],
#           '標題':rejs['title'],
#           '內文':rejs['content'],
#           '回應數量':rejs['commentCount'],
#           '發文時間':rejs['createdAt'],
#           '愛心數量':rejs['likeCount'],
#           '標註':rejs['topics'],
#           '分類':rejs['forumName']}],
#         columns=['id','標題','內文','回應數量','發文時間','愛心數量','標註','分類']))

# url = 'https://www.dcard.tw/service/api/v3/forums/cycu/posts?popular=false&limit=100&before=23132'
# resq = requests.get(url, headers = {
#   "user_agent" : random.choice(headerlist)
#   }
# )
# rejs = resq.json()
# df = pd.DataFrame()
# for i in range(len(rejs)):
#     df = df.append(Crawl(rejs[i]['id']),ignore_index=True)
#     df.to_excel('C:/Users/xu35k6jo6/Desktop/Dcardtest.xlsx', engine = 'xlsxwriter')
#     # print(i)
#     # randomtime = random.randint(20,22)
#     # print(randomtime)
#     # time.sleep(randomtime)


# for j in range(100):
#     last = str(int(df.tail(1).id))
#     url= 'https://www.dcard.tw/service/api/v2/forums/cycu/posts?popular=false&limit=100&before=' + last
#     resq = requests.get(url, headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
#     }
#   )
#     rejs = resq.json()
#     for i in range(len(rejs)):
#         df = df.append(Crawl(rejs[i]['id']), ignore_index=True)
#         print(101+i+100*j)
#         df.to_excel('C:/Users/xu35k6jo6/Desktop/Dcardtest.xlsx', engine = 'xlsxwriter')
#         time.sleep(random.randint(20,22))
        
# print(df.shape)
# proxies= {
#     "http": "185.217.137.241:1337",
#     "https": "185.217.137.241:1337"
# }
# url= 'https://www.dcard.tw/service/api/v2/forums/cycu/posts?popular=false&limit=100&before='
# print("!")
# resq = requests.get(url, headers = {
#   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
#   },
#   proxies= proxies
# )
# print(resq.text,"!!!!!!!!")