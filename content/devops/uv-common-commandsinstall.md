<<<<<<< HEAD
---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

=======
---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5IHQ7C%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCQibYBb%2BcnAxSXn0RARkEQ%2FzospVyNkuv%2FFbRG498INwIhALLFN7ZvYOpsqZDfUh0elOGoXROOqsySyFFqNjMRWu8VKv8DCAkQABoMNjM3NDIzMTgzODA1IgzRM0x0Tgs5K6VXpXsq3AOt61YskxdHSWciniL5DJXv5LvJsNAKDY4PX3rSEDI1Ze8ehpMaHhQD1vdSUgC5mwMSVxIfkK673uZoq6lGoMgD4stRYOfyHx1ewnhIKi9JdIfuW6%2F%2BYIJqVElM76rxRW9sRMxyNBOmm%2FGdS5iIw8l9XJ5%2FbTtOLvMpHey8H85sdaEXOWuUCt%2FJBSSeiLk%2FeKWQTWtOm00x9wbvtFl8dRCCmj2K6X1ZAqqqSfVPSD7%2FTOCoaHhilASo8u71H9HIGW5wTBTgOHOWS%2FZkt8hSEP2hO4%2FA4jnZ7B0xiJsGE7%2FrGUAasOcwnKT0eI3xb9%2FryVsemzDE5TsLXHqeBe0K9cBy1egTERXTywfCLOVVU48Hay3y%2F4AUHa3JoIJjQSAGg2KPt7rwq8I9qHpI6R2jKIOQnl8PH8pYX8d3M62rJHKt3Jd5dd%2BClNZGwTbWSiSbgl96ZQh05%2BPsiTpKTkFj3A1SmAc9S3XRD913%2BFV8GT%2B7bfDE3oSC7eZZBWrS7GZBF2M%2FxyQDzl%2BMTr2vZVQLj885p8YnY7A8js%2FZJVpXe11R6FJKIK5XuL9uD8DtNaaZNfuH0uCBa7Q8U7QXW3xzGvC0XTs4fZgmH6L5UUxaketiU%2FDGGTQp%2FtDIK626NTCknszPBjqkAYtrgEbW%2BsSsLAbnnqFMToVGC1Ka8UtjhaVifEGUEKY5HnqUK3IyTh3U9vIf073hWNkkQAy%2Fubqvpu%2F37k6d3AuXAfrODywG13ZsLjgO42LAhzHhGD7sB1Ifa4b%2ByqpC2sxOkFo7ASijJIy1yxmcJsTV4pYsWDanascmT%2FkEhbaV%2BTOlPGZcvJzRHHbuJD%2Fedu%2B1ByiMrQ2V9PWL1ALPD4STu2%2B3&X-Amz-Signature=2bf61029fe618a9f92c5dc7dde250e6351681b67952b5301e7f60115bbfb78e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5IHQ7C%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCQibYBb%2BcnAxSXn0RARkEQ%2FzospVyNkuv%2FFbRG498INwIhALLFN7ZvYOpsqZDfUh0elOGoXROOqsySyFFqNjMRWu8VKv8DCAkQABoMNjM3NDIzMTgzODA1IgzRM0x0Tgs5K6VXpXsq3AOt61YskxdHSWciniL5DJXv5LvJsNAKDY4PX3rSEDI1Ze8ehpMaHhQD1vdSUgC5mwMSVxIfkK673uZoq6lGoMgD4stRYOfyHx1ewnhIKi9JdIfuW6%2F%2BYIJqVElM76rxRW9sRMxyNBOmm%2FGdS5iIw8l9XJ5%2FbTtOLvMpHey8H85sdaEXOWuUCt%2FJBSSeiLk%2FeKWQTWtOm00x9wbvtFl8dRCCmj2K6X1ZAqqqSfVPSD7%2FTOCoaHhilASo8u71H9HIGW5wTBTgOHOWS%2FZkt8hSEP2hO4%2FA4jnZ7B0xiJsGE7%2FrGUAasOcwnKT0eI3xb9%2FryVsemzDE5TsLXHqeBe0K9cBy1egTERXTywfCLOVVU48Hay3y%2F4AUHa3JoIJjQSAGg2KPt7rwq8I9qHpI6R2jKIOQnl8PH8pYX8d3M62rJHKt3Jd5dd%2BClNZGwTbWSiSbgl96ZQh05%2BPsiTpKTkFj3A1SmAc9S3XRD913%2BFV8GT%2B7bfDE3oSC7eZZBWrS7GZBF2M%2FxyQDzl%2BMTr2vZVQLj885p8YnY7A8js%2FZJVpXe11R6FJKIK5XuL9uD8DtNaaZNfuH0uCBa7Q8U7QXW3xzGvC0XTs4fZgmH6L5UUxaketiU%2FDGGTQp%2FtDIK626NTCknszPBjqkAYtrgEbW%2BsSsLAbnnqFMToVGC1Ka8UtjhaVifEGUEKY5HnqUK3IyTh3U9vIf073hWNkkQAy%2Fubqvpu%2F37k6d3AuXAfrODywG13ZsLjgO42LAhzHhGD7sB1Ifa4b%2ByqpC2sxOkFo7ASijJIy1yxmcJsTV4pYsWDanascmT%2FkEhbaV%2BTOlPGZcvJzRHHbuJD%2Fedu%2B1ByiMrQ2V9PWL1ALPD4STu2%2B3&X-Amz-Signature=5f6056b0e04d19ebf59d010d732c1d1283a449297e96a9811f093609a310f25f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK5IHQ7C%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCQibYBb%2BcnAxSXn0RARkEQ%2FzospVyNkuv%2FFbRG498INwIhALLFN7ZvYOpsqZDfUh0elOGoXROOqsySyFFqNjMRWu8VKv8DCAkQABoMNjM3NDIzMTgzODA1IgzRM0x0Tgs5K6VXpXsq3AOt61YskxdHSWciniL5DJXv5LvJsNAKDY4PX3rSEDI1Ze8ehpMaHhQD1vdSUgC5mwMSVxIfkK673uZoq6lGoMgD4stRYOfyHx1ewnhIKi9JdIfuW6%2F%2BYIJqVElM76rxRW9sRMxyNBOmm%2FGdS5iIw8l9XJ5%2FbTtOLvMpHey8H85sdaEXOWuUCt%2FJBSSeiLk%2FeKWQTWtOm00x9wbvtFl8dRCCmj2K6X1ZAqqqSfVPSD7%2FTOCoaHhilASo8u71H9HIGW5wTBTgOHOWS%2FZkt8hSEP2hO4%2FA4jnZ7B0xiJsGE7%2FrGUAasOcwnKT0eI3xb9%2FryVsemzDE5TsLXHqeBe0K9cBy1egTERXTywfCLOVVU48Hay3y%2F4AUHa3JoIJjQSAGg2KPt7rwq8I9qHpI6R2jKIOQnl8PH8pYX8d3M62rJHKt3Jd5dd%2BClNZGwTbWSiSbgl96ZQh05%2BPsiTpKTkFj3A1SmAc9S3XRD913%2BFV8GT%2B7bfDE3oSC7eZZBWrS7GZBF2M%2FxyQDzl%2BMTr2vZVQLj885p8YnY7A8js%2FZJVpXe11R6FJKIK5XuL9uD8DtNaaZNfuH0uCBa7Q8U7QXW3xzGvC0XTs4fZgmH6L5UUxaketiU%2FDGGTQp%2FtDIK626NTCknszPBjqkAYtrgEbW%2BsSsLAbnnqFMToVGC1Ka8UtjhaVifEGUEKY5HnqUK3IyTh3U9vIf073hWNkkQAy%2Fubqvpu%2F37k6d3AuXAfrODywG13ZsLjgO42LAhzHhGD7sB1Ifa4b%2ByqpC2sxOkFo7ASijJIy1yxmcJsTV4pYsWDanascmT%2FkEhbaV%2BTOlPGZcvJzRHHbuJD%2Fedu%2B1ByiMrQ2V9PWL1ALPD4STu2%2B3&X-Amz-Signature=0f95bc7bdf2238b49027fbf8571c037383af9ba984bc3f7f70e8e5ecb0a97cb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
