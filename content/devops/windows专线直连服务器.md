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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN6HZRMG%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIFcOFmb95Z9LdeMvyiBHyY1gARu65%2Be7aE8QZFazw%2FSAAiEAhkwnf%2BPj7YZrlTJ8KFaVy9TXpTmp7eTOwCEGoE%2Fvfe0q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDPAQmHmAWC1yOIY49ircA1BAl1iS49tvuGqmgmFrZjawhbbyI0L9myeS5YSJWzbgMSac3J0jfRdjJesy543WuW8a8%2Fg3JnJbMRLAx4x8dgJ0edctIUcfVHhCStIKkX5%2Bd2vgoAlNMfwn4nm9fFpqdwNdql%2ByRumC5dTm3%2F6W6PgJo%2BocdR%2Bj8ruZMYURak5cdt3fFkKOL1IqCgwcH07uGnNKRvWwLhwBA%2Brg%2BDIKpyuRY9OkxmcnJAwERvZYTmiq6j511ZbxevnDV6CeVLMK6Dta2XalXw7bGSkR1v8tkDOH4N7WPD0kZGtCr0tLjZP93h%2BrCBsqKArvY5dL1QoF%2FfxpRP9P1OWStNXsjzyJOf1G93tPsCI02u%2FnIV23sunZTIYMR%2BggOhm5nM7zZD4KP9%2FqT%2B5y%2BND1mppFcBjB4a1R6zFsxKz0ap1G3Ys7GaPOuYTzCsJ6ZXwBagyVlJYNSNyabz4vwU1rW6LuOI4%2BU7kcFtakbp%2FFjU%2B7cRo%2F3FjkRtmUvgUvexXAt7qF7AHdfuTWbdFl3CqgsYz1fEcL5JSa%2FsV5vJ6XCaKu9oJuIQdbMvFxWaFIHl9LUr3jR9NTji3rIbeqCr9mXNkTpLkrr30W0sdg2zSpuYpLKECeFu8BF6wSWSmgplSMrtdvMN248s0GOqUBS3SI7wUTY%2BAPCKh9opnXxri95rd5dO%2BXgbguOc5xwrP%2FT4gLRDR9MDltP1OfpPuBpS1%2FTwXmgUfVspvAjkrazmZZT1byCxGqTiSF5R1rWLfa%2FPw47VBBzZGkQlQvTN%2FO9YnolNWaXG4U3NjeD09CsKNxGl3CCXgRkrVylAC8E9oxyDaUgimPCqhl9awHXfgKNWvNB2LB4ZjPuw%2BWszvQfsjECx%2Bq&X-Amz-Signature=db036c9b5337903470bb80b1be8a5d8859f7f8f51e162baacb139ca7e45662b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

