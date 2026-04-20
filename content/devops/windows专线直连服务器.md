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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CFYQKNH%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQD8QbaiHuFlawN5q8mvIKAo8T7txSw4cPIWc3f6kuULjAIgFkoVtmtbJvuJWLn%2Fs9tn6q7OwRCfxoQY122k64nhCH8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDDn0uoCY3lr%2F8qK2BSrcA%2B%2F7s5Vj3nsNjTmEtWbvSY7NaTCj6B2gvaMyRZzO0BHxxccAFOXBmDWd%2BWKWXXdOiIzJ7jGylzCvKC%2BpUtwtMTuGq8AX1IksCyVy9v26SJb2QdyKuU4L5wbuNdqLBO1B7dP48qPVWYrixj2bVVbKqE3txSaIIQul8SxsAnSYEiDGL1WcwI9NamPmTAiXWleJBSvLDxvYElNiWxT71RktCXYB40ddh2M%2FtHtJyoy%2FKSCSKBwUezERBL%2FJhhMVxvDKkp8OlTyWv0airXZPQGa9XX6XAm%2BvUhQPWgW8ShCFgyFklZluZ600KMMx4fMRPDTgcNuHDEhgUYtOYzjlRXIIyNTBFlTU8YROxykAaBFC7ctd2HYZnSWwIb5%2F8LN3oFqXKQR915opKcgoe5HMS%2FXkkdMocsuGV1p639rDZ5lQgdO%2F180AtwvWY9Byh5%2BK1E03vSRqvNeGAw6SLGS%2Fjqp7M5wSb6cYih2cWQOc6WQ2IH30Igw1I%2BvBz6HnBRzl9Ojlr%2BKW6JSyKWg69SOPbogk4stEEo8mb2CHzhzNJY2KJViseZobhImUq%2Fth9%2BIZNhTwT%2FGdcSGKmLrev9ctDIaJHdk0yIHDw41pNSrp8%2BBJ1E9AVgiTz%2BMq%2FZ5%2BLn3qMPGXls8GOqUBc%2BZeitBLU72bRFXScwRiBFjwF5sejFcjqlJRcbJq9imFJ0zWzGuS8MLGDtmfO%2F54iX63SuZDD9w5rtmCRfAQ436ROI%2Fbb%2FCGw97lyDmScVZvlyYxSZ9FCRQaagTy9bcXkdHf6hZyVRDiCwYSrLXFWoLpaz4GQ5c7jHrn8tmcNpgpusKW0aEKvzWB%2BjkQHHIi5njzpp5RXdonWTVGI15I9%2FqmKOvd&X-Amz-Signature=500dbf6f6381bcd555fe9da5a5fbc66a2ff81b64e2ac4457914035e3708ace6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

