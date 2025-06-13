# 新闻API工具集

这个项目包含两个Python脚本，用于与World News API进行交互，主要用于新闻搜索和新闻源检查功能。

## 功能特点

### 1. 新闻搜索 (scratch URL.py)
- 使用World News API搜索特定主题的新闻
- 支持按语言筛选（默认日语）
- 可自定义返回结果数量
- 按发布时间排序
- 显示新闻标题、来源、URL和发布时间

### 2. 新闻源检查 (check URL.py)
- 检查指定网站是否被World News API监测
- 支持批量检查多个网站
- 提供详细的检查结果反馈

## 安装要求

- Python 3.6+
- requests库

```bash
pip install requests
```

## 使用方法

### 新闻搜索
1. 在`scratch URL.py`中设置您的API密钥：
```python
api_key = "your_api_key_here"
```

2. 运行脚本：
```bash
python scratch_URL.py
```

### 新闻源检查
1. 在`check URL.py`中设置您的API密钥：
```python
API_KEY = "your_api_key_here"
```

2. 在`websites`列表中添加要检查的网站URL：
```python
websites = [
    "https://example.com",
    "https://another-site.com"
]
```

3. 运行脚本：
```bash
python check_URL.py
```

## API密钥获取

要使用这些脚本，您需要从[World News API](https://worldnewsapi.com/)获取API密钥。

## 注意事项

- 请确保妥善保管您的API密钥
- API可能有调用频率限制，请参考World News API的官方文档
- 建议在使用前测试API连接是否正常

## 错误处理

两个脚本都包含了基本的错误处理机制，可以处理：
- 网络请求错误
- JSON解析错误
- API响应错误

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

MIT License 
