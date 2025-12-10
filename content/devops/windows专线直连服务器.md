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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGW7DP2Z%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIBgqH0mqnReAD8axLptcABGyASLCic7akD4e12JjvP60AiEAwpMyu7RiTfKYIZUZH9juR8iPp929Yd2Nn5rAGnqa6jEqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN03O7OCCcUR6PWVnyrcA8hmoPQcDdSGaiv9Cgm6Sfh4%2Bo4h0HvnGyToQ6DSmrcTfFURRTK2BraHgIlEemOmyW5GEuZxP90GMZWrbv5aae8DNoMmqBWl2rWljGU%2Fc4eO2Ir7qcszbAt1fgZEHUd2lcZ8ljBVP86C9wuOfYo%2F0VwKW722nbHpocjE1EbGNEVk2KV4pcojo%2FGPYRkUqFuOA4ouIeLEaZAdav81TNDEPPrBnymBQCA74gpACojYQJ8NHHccP8Twu4xg2OwpaMvSjnZupyZIrW1xzBmpZkJkztJflc02y28QvpIjijGfXL9xE2T0h7Ti2IljAiXAGpYHwtT9VWNM5sSKaf38qxM8clo1%2BvgfAlcVPv2JHdUjj99bcBhEoxnHEQoTgIqFIz0mDmnTerYULWqyZ9kpbouV2yjJ4yx6F79G1BIB54kE0d22HGqRPD%2FGzl4F0PvIZRLxc1jdYi%2F%2BXg2g1oIJM2StEfYxlB6cPIRxKQlQIkAOxP8QU7K1Sj4Gd6XmDsOQNWTSebUHuATeIGqXMX2967SHBZTW142FvB4saI4Wq32rL4xfZkPcO9FvJGFwN5769rwctVOx%2Fuow%2F%2BmS0xfy3FAaC57PLuLbTPEYgOW3ySlHPnk6NLlSF0r%2FAsrLt9J5MIi%2F48kGOqUBxPWS6oWuctW378mXt3DyHw6ofJyLqovHCVEfuhOsLP4ZOa9fr47rxMeqNSUgtl9kaHDu3xphS9i2qWBfSiCn72R9JyS0M4y9kfNtib72R7QXdpAhl0X67VrucKL84r1pVqgJf1FH%2FTny71ADp43ms3EynqZL62SqlJVz4nzYm%2Bt0f%2FZSEWQ2lBbQsheRy9ikn6kHzHPXkb6wBp5OsHYD7vMLtQVk&X-Amz-Signature=a597fb2ec549ce5a49496b0aed5675cf9e22d50db5e16075b8b77e5bec5b1b6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

