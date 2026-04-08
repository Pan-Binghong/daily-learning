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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKIYN33S%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIH9nTkPhKZtud68lumgIMWBp9p9aF7DywWtRo88xu6brAiEAyZJLLXrEqCzB%2BTfs09WERFNjLBKmHOq6pY2Be8RuBt8qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDTNG4Y%2BhZip5MmFeyrcA5gsi0hfh6iVs5BjV4bO6g17fkCPXs6%2FzIjtkSlWWSrasvfQPgC4rkVZbol20Lzukhwtd4pdUSz72fDLe1QlozcaMRPVIndOrYmbkgPr6Bo0LRns9cgnNMD5jyuyV%2BCN%2FWZ8MJPtMT10bPy7%2FrwrQrdJw92G7WnnOlJjybGVooBFm4IWIA%2BTrsTp6pmiJA2z4NDW06x2YuPHgO9%2FhDF6YBjvVGkwQ%2BIwKoTq4AuWv0DVFS8FnMVXbBKlncWmMo4AAWx4FBKVfjEmWdL8qfN8mXI1tFuoRGg6Yr9ZhMxEA8hiknWBiXoXkmTYYvNq1oYuAziM50wuz5D6pCgNAbGrZStUq0E9e8AfjwbdbFQ%2BncRqyGBe0QbjUOQ4jOP1QpCGczPqnFi%2B5Q2vgDvYipoEGLi%2FYESqB4tg4SEkGnUe%2FsMOHSKkfz9rh6KF%2BXzgU59%2B%2Fn%2FuOkiqRa9A7UPg4%2F85g%2Fd%2B2ZG3ACXTPrWtVqYBerBgGzm9CBLF9IHkp3EgVPkLM37p0DLMde5c7CewT4FwwEBq9hqH%2Fnm1k5ifCVEhHZQosAQWQfcF3x42ZDMbjPCAVylvvuHrKPTlBQZm3jUB2neZc0FMmwITiFICL0IJlr58CAE89%2FRahddCoKjjMMKJ184GOqUBJi2Yr6ZrqkJXqj01njMdkYuihDzoveoWDZEmtvvJ4auIwzjgCtx%2Fuw0Eh1xohmNupa%2BeuPGJVNw2byG1auKscgjVLLEoQizbfo40twQvjFuoZyQSG3EdMBHdYYgWF3yluza2Q6aqt76mHto08t2ADK%2BwzHiEjy%2Bmv6x4VBAptZ9I%2F2eptzVLkQ7cePTQqq6Kugv5PfUq2srIggHPzlv8oLtgHlvH&X-Amz-Signature=d2ffb45810904bfa5f7dbf7d0f0ad0622f521b60d4e5f629bbd15641ed3e2450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

