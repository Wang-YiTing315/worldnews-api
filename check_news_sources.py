import requests
import json

API_KEY = "4fbfa884f56e4829bf0aad0a47313116"
BASE_URL = "https://api.worldnewsapi.com/suggest-news-source"

def check_news_source(url):
    params = {
        "url": url,
        "language": "ja"  # 设置为日语
    }
    
    headers = {
        'x-api-key': API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data.get("suggested"):
            return True, f"网站 {url} 已被监测，建议添加为新闻源"
        else:
            return False, f"网站 {url} 未被监测"
            
    except Exception as e:
        return False, f"检查网站 {url} 时发生错误: {str(e)}"

# 要检查的网站列表
websites = [
    "https://www.drone.jp/",
    "https://dronetribune.jp/",
    "https://xtech.nikkei.com/",
    "https://drone-journal.impress.co.jp/",
    "https://news.livedoor.com/",
    "https://news.livedoor.com/article/detail/28852083/"
]

print("开始检查网站监测状态...")
print("-" * 50)

for website in websites:
    is_monitored, message = check_news_source(website)
    print(message)
    print("-" * 50) 