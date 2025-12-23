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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJBYQWIG%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIE09G5wlr7uShnFgZoX1IaCuwlMrIMHmPvgeiFEmxqc4AiEAvqUnFSO0FwBDbX1XazV%2FdGTs5X%2BcpSPHHnKIX%2BsWfRoq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDFDYssn9jeDXA9B69ircA5%2BiuRVQcGP2pLRLT%2B7H6c1JjeDlcoRIIUuOViakqvdz8U04kBLK2SLPJL16QQ3kNtROWZ%2BYrNX7XYbeBbOq%2F627SZaN3D%2FNJb5SXaecYvA%2Fg77oAzR3UcZMAzhp7YK0Ra1OTZW4MstZ9t9MzZJCQNkaza34ZVaMjAB6LAIn7LpkCBePnqYxZoBiO1rOGFU9s6MgQuwR6urQWuuCbzN%2FWYrSecFXTBx0ZcccCSQ9H%2BIxaOAkIorq4jjbHYETS%2BRMPXDt8BHnl%2FI%2BrFOvzn7plc19zCxAdWHtEry5KhmA%2BS8n4OxpaiseeG08z8gqMow19g7oOaWDawF1WNoaZ5IsumvO9yFuo8374DKBnxEswsGb7%2BEvjNtxO3gz4UnfvWymHLg%2BKi6LYCxZIqoPtJbCpQoUdYqOaXrrq0dMh7c4TjCvZwlML6gxqb5oztr5P0QIWtybIIk7NF6lsK%2FXCke%2BDhm3ui9%2BTMLxCCcBGRH%2FAFjpNR9c435dNjDrNj4K5VOz9fukMRymitYy4OiMmM8Pzq8IByJktLBFm4adobZhUy1mycq1oo%2Flxee6xoCEArwkiczpnGo6iJLLVtN43x4WIQ4N%2BMIuKHohRD%2FiWlnNobKqcgN%2BaTvLQBvHYlaUMK38p8oGOqUBeUMQkBwkl6fJa3Ovmkh3kREm%2F2IvTUiVbeRPODp%2BtKcLWgV5jKmyGNeYGR0BALW%2FqhC%2Fw7q7Zy8twTWxjvtIlZ341paLWIYxWKm39%2F%2BiUfb6YsckNSXuny%2BmbIurfxmjYGv%2BtB3pQre4qEATYVunJnT9UR8oLDRqsLLYn8a5zXxDXXONdr0yagfH6nurqjKW1cb6UVKmQYy6Cb9PM0nQYI2w5AWq&X-Amz-Signature=65b24bfaab515922ccfd9f47c635fd738e90043c5777f8db422f20941f4cc2ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

