import pandas as pd

dcard_article = pd.read_csv('C:\python\python-training\Dcard爬蟲\\random_text_right.csv')#讀取留言資料.csv
dcard_commit = pd.read_csv('C:\python\python-training\Dcard爬蟲\Dcard_comments.csv')


for id in dcard_article['id'] :
    for mid in dcard_commit['文章ID']:
        if id == mid:
            id['內文'] = str(id['內文']) + str(mid['留言內容'])

