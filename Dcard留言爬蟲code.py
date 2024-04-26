import time
import requests
import json
import pandas as pd
import random

dcard_article = pd.read_csv('C:\python\python-training\Dcard爬蟲\\random_text_right.csv') #讀取文章資料.csv
# https://www.dcard.tw/service/api/v2/posts/235996273/comments?after=60
# https://www.dcard.tw/service/api/v2/posts/238582263/comments?parentId=639a74c8-4a2e-4473-ae39-1e45357df235&limit=10
alldata = []
tempdata = []
j = 1 # 第n篇文章
k = 0 # 已儲存的第n筆資料
h = False
for articleID in dcard_article['id']:
    last_comment = ''
    url = 'https://www.dcard.tw/service/api/v2/posts/'+ str(articleID) +'/comments'
    doit = True
    i = 0 # 文章內第n批留言(每批30筆)
    print('處理資料:第', j,'篇-第', i + 1,'批')
    print('文章ID : ' ,articleID )
    while doit:
        if h == True:
            break
        if i != 0: # 判斷是否是第一次執行
            request_url = url +'?after='+ str(last_comment)
        else:
            request_url = url # 第一次執行，不須加上後方的before
            
        list_req = requests.get(request_url) # 請求

        #將整個網站的程式碼爬下來
        try:
            getdata = json.loads(list_req.content)
        except:
            print( '錯誤回報(status_code) : ' + str(list_req.status_code) + '\n爬太快了，休息一下')
            if list_req.status_code == 403 :
                print("去 https://www.dcard.tw/f 解鎖")
                h = True
        if len(getdata) > 0:
            alldata.extend(getdata) # 將另一個陣列插在最後面
        else:
            doit = False
        
        last_comment = str(len(alldata)) # 取出最後一篇文章
        

        time.sleep(random.randint(20,23))
        i=i+1
    tempdata = alldata # 以tempdata先儲存資料，以防被擋儲存不了。
    tempdata = pd.DataFrame(alldata)
# 翻譯欄位
    tempdata.rename(columns={
        'id': '發文ID',
        'anonymous': '',
        'postId': '文章ID',
        'createdAt': '發文時間',
        'updatedAt': '更新時間',
        'floor': '樓層',
        'content': '留言內容',
        'likeCount': '按讚數',
        'hiddenByAuthor': '是否被作者隱藏',
        'gender': '性別',
        'school': '學校',
        'host': '是否為發文者',
        'hidden': '是否隱藏',
        'department': '個人主頁',
    }, inplace=True)
#存檔
    try:
        tempdata.to_csv(
            'C:\python\python-training\Dcard爬蟲\\random_text_right留言.csv', # 檔案名稱
            encoding = 'utf-8-sig', # 編碼
            index=False # 是否保留index
        ) 
        j+=1
        k+=1
    except:
        print('ID : ' + articleID +' 儲存錯誤\n')
        break
    print('已儲存共: ' , k , ' 篇文章之留言\n')