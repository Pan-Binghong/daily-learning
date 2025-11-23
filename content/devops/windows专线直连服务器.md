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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6JOLNPM%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDoy9BJ%2BEolCKINpJfupXLb3OeXCnvV4zYt1Zwt4GyneAIhANKcc9Q1ipT2eHzF5nAviatTOYVqZ0PISx1wNbRh4kwDKv8DCDIQABoMNjM3NDIzMTgzODA1IgwZk44ztbXT%2BF94uW8q3ANaNPIoUkRXn13oIOje9yBIlELeOmLFgFOCj7kHwBZBTnPlEPrGfP1TlN8kSPhT48O4TuhJXoPgDOp5KpS%2FkIOcUzBAbbegro9yF3LPPRdd5pseC0tGv5Yq2%2F61PlylmuxryFaWVs7rdZ0NREPJgATLj7IOEsYdR%2BNE5BtJRhTRge1g36S0jyAEM9wMJdedBenYVcGtxtS5j2KUxK5LONxuz42nLUVk8RDtJQXtj8cifzscJAy8cvw2P2w%2BvSteR%2FSRjSu9DV%2B9DS8IwYA2yG2Y7dga4sv3zBFPlqyChjzlqawc6WDumtGt2g4DcnrnJ9FvC3Fyc%2FXZbSv4nqTz%2FXvlb7YQVLUrIQaHB1igTc6DAliuMjm952GPYnCKlMC75q7KS8ANy%2BvR6Q5655wZ31hzFSBpJaxo4BmPq3ZKZL44eDnh89fO1Pws4S8awIpq5%2BRnEE7281Qr43rg5Wl19cxpjzh2TgivKnERf817%2BAi0Nb3bcmVRexYjw7hMxCIWFBDFtnOeDBPkycmYsZ91dQxV%2FtjZ9cST1TIja9l4uJVKD8WrVxny2yJeL4DB2xFduwVYNzfdiU9agZ%2BdknOE28d4gWfKFzTjVUCs16TGBHouc%2BST%2B3hKGlk5nkFwYjDksInJBjqkAYlLtiet8NDkM1UKumsOoQ4%2FY%2FAKsGWxABx2PDFexYfWc1%2BW3yV6aQFpQnsuSsI0KVhqeABFYaUcFr71Q%2FzNYrTUAnM3IBSMqLIc4UyVdG45YWB0c%2B6wHh0KXWfGHPCPsu7B14GPwMuJfS1sE9ZzpRqDNthHl4GgdnQiiTLiD9tLP9CxTN%2FG6%2FfiFtLmQecVOLYlnNmG7%2B3ITsdlrp7gxilnaGJr&X-Amz-Signature=5c455c3e8c0fa93e472a6865e9588ca4841b7b50f33cfa2428ee7f79e4253637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

