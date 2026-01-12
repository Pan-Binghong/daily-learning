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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DVSEL4F%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBluxI%2BGxYI%2FxpifLJvkBUfHw5qFO9f96bie5jiqP1kAAiAnueq05aajsj2fYjCr4aduoa3O%2FTQoaFN%2F8mUpuZj9OSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOFkk4mF4KnLxpUxpKtwDnrQ%2B8DnCHSXJ6cnUNZ4yqD4461e4U4t%2Bd%2Bxa%2FsLDEyoFo2qRvIu4fIG7eBImwsuYb9pN0e4FIxADU0wsBzu54Bd82dLQ9LDGuNQKC2V1XcM3sy0iZHYPuMI0JQZudyp4itbhJe2S%2FI5JJxugmhEeDoZ20AI%2B1fvN3LFwUd1AHxhyS%2Ftw4ROzl7vQazBBLMzYpdIBqNO94bH5CHr5u0laK8RmAjMADFnfiExTM3zMUqmmmjOhwkyAj9KRsez9qdRW6HQw%2BAdthw9wKYLbJsJzzPAiaW3EFEViHN140xjGJD8yCxXJz3Ce9x%2FCOf4RyQRJHH0oCi8Si76EQT1mFpvX96N3xg355o%2Fd4mwIKIiGjb0z%2BO3tytUzLOG7BYYH7ikZ4hE3ytI44NJR%2FlD9QPtet82BI%2B5qfaRxoR972gGc1GLq%2FSvGfGZIc7nn%2FSy5M%2BY5I2YgGEwidNQo9rqq2PqxiSgbmzngAZKex9viwm487rbLZhFS%2Bz6xxeQo9gYrhJo6232SezTNynixwmEZSiBQoCyR7bGTU8cy1ZP7h4FqwAELDVhpM37wFTgMDLz3PC50xpaIYhqlqjE6vRWitNfVGCiywNxueNYzXbvUbq1wW8FrBw31%2FloG7u661EYwoviQywY6pgEUQR6LX7NcB6mOhtlbx4yBs%2BU9MuMYoCd0%2Fko%2BpU%2FVz73q5yC2zMdKaDYF4TRl5TfaJBq2DUDqdNWlU1%2FKf0K1B%2BI2o8huIq3v%2FGMuBEBO5eGC6LHDjVyEnS9sxXC1xMd06BWlajHi8XacT8PzmBSCmtKRkSspblHwL%2FTY2Yscw8DEVFe7NeqGGB%2Bh1FFpV%2BRl1PNcGYGWAjSGqjHK4Hip8%2Fwx33ny&X-Amz-Signature=562cec50811c5ab616d49876335914526414350255949c8c7d44a7a5cb7bf80b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

