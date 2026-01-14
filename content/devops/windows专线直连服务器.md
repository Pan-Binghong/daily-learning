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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U7DMRTJ%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCajqQc5HooBAgaQME%2BPxUYHxmVBjCCc0fNLJcNjcSMTwIgQL2TZZ7G1VRds9zVabg%2FBq1cjJ2kyGIzGT2%2BByqwLpAq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDIVmEm0RrCjqS7C28yrcA%2Bkay9hqwus9sQuLKaYNuBssd%2BhDeuACkQR4kp50JnHxToPbceM24CT%2B2Wg1rC%2FEau%2FjeRggJZekavrVnz76X3bGre%2FPE2QIcbUTo0Fv9rkpHeYIonqnkDwJrVWicnjguuCjhSfZF%2FyiR%2B86Y0WLpS4vHTzz2GlxlrlA1xRwaX9cQ7tGO1w5L5%2BNbQVPXWo07AyAmyxqni9Cs15%2Bl9JFpyCinouI%2F8haXG84DWH6kc2uwQ6jRL4nqrUGXRnYsOiQuvPRImKTz5KY3atl56ZKRer9UPRUFJHMIHwMn%2FjTep9SUlw0l1H7S2UpIshwU8syKqjwm3lbb8J9yLq6ei%2B3NNut%2FVFnLZI5fQA1OL9bzGalecW2Sr2gfPF2i20KPCpGG2ZZ8xuOnrPP6wvb5S0KOqBV6QGT4PdyIHCa1GJopQw8JsrNxwz1ym7rL%2BMREc1UaO4E2CtIGApDTA8onX0fWL8%2FnPRkAxSZhjKo7ZCyWd8CIznU1oKwD6ejdyUTnm7IIfemzALE4vpgNDUq4N5q%2F%2BL9wGJ1lLDkID0XkXEP4R%2BunboCWhGGXCoMcxhtxs8TnC2cRkiwhIqKdePPOmlrX5CyKjvS900%2BA5jujjeYMxAEl4QyMijq7jo5MxPbMJuPnMsGOqUBJxKmeffFSTrKHFMWa1%2BSZloIhRSyc2F9Hs%2FBMbDagF6nAEAchcY81OIj2wO%2BXjDdwHbIITTqWrrfs96j7hdsdW%2FVC%2B4%2FPCrRSzHRRB3AxVwQ8pNiHyEwZhGWHSyELR86j4WPH30c%2F8hL81zDZ6XVZzSbOrezpyNlLGWLxJd8tDEBAq0J4NUN1Kk0Cjhg6XlRavuFOXSJuy19hrk9GNpVpP4UQhMG&X-Amz-Signature=d5140be7218463c552fac807bf7c6203a326f8853453184a039c5bd9a63e6ca8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

