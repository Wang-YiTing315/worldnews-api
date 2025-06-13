import requests
import json

def search_drone_news():
    # API配置
    api_key = "ea4892cb2ceb4f55b0fcd5b925d51eb8"
    base_url = "https://api.worldnewsapi.com/search-news"
    
    # 请求参数
    params = {
        "api-key": api_key,
        "text": "drone",   # 主题词
        "language": "ja",  # 日语
        "number": 10,      # 返回10条结果
        "sort": "publish-time",
        "sort-direction": "DESC"
    }
    
    try:
        # 发送请求
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析响应
        data = response.json()
        
        # 打印结果
        print("找到的新闻网站：")
        print("-" * 50)
        
        for news in data.get("news", []):
            print(f"标题: {news.get('title', 'N/A')}")
            print(f"来源: {news.get('source', {}).get('name', 'N/A')}")
            print(f"URL: {news.get('url', 'N/A')}")
            print(f"发布时间: {news.get('publish_date', 'N/A')}")
            print("-" * 50)
            
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    search_drone_news() 