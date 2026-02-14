---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX664ZRF%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIAFP02btqyf9tmjlvajpSplIl2bxSdRyub1iNWdX0A2PAiBwFLCkPYHuC76WpgfWfwEzjilM0SqJfnUPiNi0bJTHlSqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSuSSjtVJaDWtPacQKtwDcSzfa2ir%2FU6qLvr6D2jMNdpwIerl82u5HSw%2FdA1t8zhQMlyHoBRdq5ci9RngnY0F0IYYjUZbOmF6UfVvdFC8mkLio3lGWOxkZ8QnzRUW%2Bdb9a%2BOw%2FVY%2BYQqBXt%2BreenYG5v4HloBOVrB%2FtZQ%2BLAUGXo%2BfXmyXwKF5gxZDxu5m57PjgJ0KkBKgIJ5K837VYMTjlP3ojmSYg219I1UoErx3bydbbhqZFrau7ai0y2Zw3m0fifB1KDe9slfPuaJfbwGsOYhiBwq71zrO4SML42xRswdjMx1AJglYOz0iGjXSCEKmZG%2B6ZaZODcmt4mS%2B4ZtaQkEedO5rC7xb9WWHbh%2Bw3XxpaeW15TV1cutrFURagWw4pKpzhfX1pTktXPpEh474O1rJN40EUDZ8WeMJrKFRLowPfT%2F9NI6f1pJuHKM8YcZ2eNiY06GonGPcXu%2BYrn2Rny%2B8dq7%2Fby8o1Gy14uHxL0nIfZ8zOIPaiTkjz5fl3KLaUWc1wmDAAQONbTdGxoRVABXyZnKiYn2LEm%2BqwhtqXNkirobMcdKnP38xYkcYSrZyq1%2B4RpxfQ%2FYINPO0ANUwnqGaUyBEelLX4PN4OppxKqPHT5iSsFw3WNzg3taU04Ie3ri1Wx4H%2B%2Fs%2FgYwnMC%2FzAY6pgFJ8RyNu68xZnZTokHENS55QcjE1uQAICD8JHJf1gQ8A55mzmupfK1qlZnw8j24iiutlJ7dBgxlpfE4FBMcFMoQqbvUx9jl2knilbQbpSyyC2aSzP0inQBw1nT7%2B43A4ZRi%2B2UNxMQ3sFtWkuyh02z4tRGagpI4O4K8n5liAb9ejtQlgDDDAyOE0oYW9KKc%2FJx2cpc3m4AAuNwocp1QivHEYcR1bZeU&X-Amz-Signature=719ad5b14d3f37955b92ca6b74ba295e1448c9af67e16ff02b7b45ef45247af8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

