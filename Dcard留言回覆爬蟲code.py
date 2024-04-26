import time
import requests
import json
import pandas as pd
import random

dcard_article = pd.read_csv('C:\python\python-training\Dcard爬蟲\\random_text_right留言.csv')#讀取留言資料.csv

# https://www.dcard.tw/service/api/v2/posts/235996273/comments?after=60
# https://www.dcard.tw/service/api/v2/posts/238582263/comments?205c3a32-3848-4184-909b-e806e16cb496&limit=10
alldata = []
tempdata = []
j = 1 # 第n個留言
k = 0 #已儲存的第n筆資料

for articleID in dcard_article['發文ID'] :
    last_comment = ''
    url = 'https://www.dcard.tw/service/api/v2/posts/238582263/comments?parentId='+ str(articleID)
    doit = True
    i = 0 # 留言回覆的第n批(每批10個回覆)
    print('處理資料:第', j,'個留言-第', i + 1,'批')
    print('回復樓層ID : ' +articleID )
    request_url = url 
    list_req = requests.get(request_url) # 請求

    try:
        getdata = json.loads(list_req.content)
    except:
        print( '錯誤回報(status_code) : ' + str(list_req.status_code) + '\n爬太快了，休息一下')
        if list_req.status_code == 403 :
            print("去'https://www.dcard.tw/f'解鎖")
        break
    #將整個網站的程式碼爬下來

    if len(getdata) > 0:
        alldata.extend(getdata) # 將另一個陣列插在最後面
    else:
        doit = False
        
    last_comment = str(len(alldata)) # 取出最後一篇文章
    i=i+1
    if len(list_req.text) == 2:
        print('此樓層沒回覆') 
    else :
        k+=1
        print('有資料，正在儲存此回覆')
    
    time.sleep(random.randint(20,22))
    tempdata = alldata
    tempdata = pd.DataFrame(alldata)
# 翻譯欄位
    tempdata.rename(columns={
        'id': '發文ID',
        'anonymous': '',
        'postId': '文章ID',
        'createdAt': '發文時間',
        'updatedAt': '更新時間',
        'floor': '回覆樓層',
        'doorplate': '留言樓層',
        'content': '留言內容',
        'likeCount': '按讚數',
        'hiddenByAuthor': '是否被作者隱藏',
        'gender': '性別',
        'school': '學校',
        'host': '是否為發文者',
        'hidden': '是否隱藏'
    }, inplace=True)
#存檔
    try:
        tempdata.to_csv(
            'C:\python\python-training\Dcard爬蟲\\random_text_right留言的留言.csv', # 檔案名稱
            encoding = 'utf-8-sig', # 編碼
            index=False # 是否保留index
        ) 
        j+=1

    except:
        print('ID : ' + articleID +' 儲存錯誤\n')
        break
    print('已儲存共: ' , k , ' 筆資料\n')

