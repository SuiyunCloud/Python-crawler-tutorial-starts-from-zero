1. 输出json时中文乱码
Add follow configuration in settings.py
```python
FEED_EXPORT_ENCODING = 'utf-8'
```

2. 获取某个网站，报302错误
Rootcause: website will redirect to new url and then redirect back; scrapy filter duplicated url by default, therefore the url will be ignored
Solution:
Rewrite make_requests_from_url for the spider, define request not to drop duplicated.
```python
def make_requests_from_url(self, url):
    return Request(url, dont_filter=True)
```