---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY6BHQFF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQR5zaUlGlBaHeB9PczEUF7kWMepb3QQVDftWi5p0QSwIhAPrm3uJAWEwR6KUiIjoxGJu6E7rzuL5%2F5tVd1WCNDgKbKv8DCH8QABoMNjM3NDIzMTgzODA1IgxzB0A95J%2FbivQiOTAq3AMaD2rZaxXAqaptvBXOrEKzmBHIh8K6DUAPmm0OyLbz84AVfb0QdnTg5ayW84ziVzwhTHC3VKm1WqKfngMslFucmNa6Pvh%2F0xBylgLdKFQONy4wNkkF4edpWWcRDtnffogdD9hYXEucXd7bH6iApMXVW7dqeLbn1gYGi0c%2FzE%2B6t6bmZGohBqvMm06uYnwqKP9JiUrFiJWsrjC5B1wXWHb%2Fwcuz4AMLjuPjZAkie06swKGJvGR36IkMIeC1%2F3WIyOqgwgvHCnSrB8Zb3cD8RvKniutJKQCb%2Bi%2BWuZYKjol%2FTeZvn4jZXnlbNI2Rkeng53V8vmlNKZ7TrdEbGIeJe%2FMo56aSBawjdzwqLySLa%2FtVEJHpSxnDVxG7BXb1M5ILLmjdhEYXpBC5S2HDseEA80Wjc375OF8XYLNvzsBI14%2FTAfm0BDFuqQpBRRH60EurBz8gMzu1NlIcARfL%2Fs8IGkuNjVUi%2FiPaLwAmYHsW2eRL3SeQyBnI4LAvsr2KHEyIjm4XmR1up5Jj5mbufv7UlT2u5MYeLQBWSMDkq3WcxqA9wOmmJiCSuQQS7RMYfT9z%2FL6imNLtZY9DIvYv3jj0n226H6g5Pb2iWTv2oRs2HZYNg%2FwEyPLZdVJsvr6AZzDlrL3OBjqkAS2Wto%2FRgyefXJjl8pdxQcOiSChLEV3bXuqyx%2BfY8bQ%2FWVhjIe9yUFEqg0Br6%2FPW4kd2yyxDfYWS9VPaEZ6YPtzd3Txp9BpRFO04EC2lt61NrYz%2Bl%2FVAZ1aF0uyeAyBJBYala08yuWE1QX1gyFw8XyVmjTAd5Ul5xUvdoLSmBN9YSYglGGJWDgS75aSH%2FptSttrDQh0AmULvXjZQYehpF%2BDeoHPi&X-Amz-Signature=e91658cb3999e33810a68b29115b68a87f31b2506852ba94500ceb397d39e06e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

