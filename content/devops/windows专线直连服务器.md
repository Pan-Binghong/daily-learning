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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVMABOZ2%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCFG3Td%2BUcES5KvR08GN6Pt%2FcS8WkpO0ud3iRWZI%2Fy8TwIhAJ7nV7vjU8HiLOfY2lIE97tgIx2ndgjdWj2fj9mTKdNQKv8DCCUQABoMNjM3NDIzMTgzODA1IgwTg%2FrXhu4IfmbEXq8q3APL7Ma0r6e%2Bs2GpwKoQ44rBIu%2BygmahD79myOMwqOGJqMn4lS6P8SzAKQvzXzFPe6DtZFiNi8kQF%2FgmJ5X7kfNkUv9k0mmvvJ2lKV%2FNLDJGKfz4KynS44tho0YRO1pv0KGiXZcxCiTHqJjJTmIiIgR5d7gwEU%2BIF1zeVDgkYWfTmAXCbM0yH4zuAsSRIqQHeXkEzYHE5gl%2FzC%2Fu7CjatEzbhaN2Ouj%2BSwzLTJdYvSAcxUjzJkgr%2Be%2BugN0Wjx1eFWyPtHP7D99lP5c6%2FSaXhZwZN2PQE88Tvlh5i7Qlsv932qFiLfL%2FLs1AcNCq%2FiBRwxnJ2XlXkvCzHbm33kWobLxYUY0AsT67334nNwrWztYdPprEScIJNxlxDJVyEVd5OwhUrjy3TTTP1aQMBG6MmAujqIIJbWdyvR4kFLbpg1Km9pqIFg07Xw8P64JRLjOlpqjUUJqK4xZJ4b6xFgIkRRUQvDr5coSWM%2BgwZBUPQ5cXwKNMbmrh90u5MuNKXvWDNA4XE8LHrUDamhmWpDIS0x2lzQtsIJmvHB9LgwETG4zjHa8qA%2BZ2uDKC%2FGrA6L7TNo2ODlNaw75cci89lQs5TA9GsbX6wo%2Fc5XgqJ%2BF8icXkogKxjigz%2FllVRIi0GDCW%2FbjNBjqkAdmGM5%2FlZgIZxERzBPDteJCjMWqek5AJ0L5KlXe9GQTucXmEYlD0RcMs70rcTVp6OOUsFX%2B9WQE3hlBT8QBgUeDd4Nn61d%2B%2Fa%2Fik6NfEWpgECRWL%2Fn2fmO3fZcRJbNz07eU%2Fgi6AX%2FxV7pXjNOGs3EeRnyBswNeQjRYSTYPiwcaICqsI%2F8K1%2Byxijh97Hpy9v40KaR37Hbyb5vR6MdDr4lY5uifd&X-Amz-Signature=57634640b3ad47669bbf68fa1f2eb24f9a7f83b918a6b54c68fde8f142d2fdd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

