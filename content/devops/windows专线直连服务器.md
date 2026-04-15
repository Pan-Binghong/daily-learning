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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SLS7A52%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCSulF6SIc%2F%2Fte420U0G2GjOEfjZ0cd7x9eqTkHT%2F5XtgIhANV1nPNGXXnj4zT4uBjgl%2BG09ZSuUp2IUH0ZC1%2BttAoMKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzKBIeBfUespeJry5wq3AP522mB%2FoEmKnGV3yj4eZSUVYIG84kofyIQlxk8nnFePf3PqR%2F9GyyJ6n4GHJncieCBTXrLpZZ8Gxh%2BwPJPPrslD%2FNKJUkAWg99O5EtPnkeI14NTZXtcQe6w5san%2B02VdFVbnMSDwHvAIZCzK0NCOQBj8%2F5xBnNoAqVj5wud8wAYOGQ5309EC7V9Ju6WWV8YtOm4SRuT9elEkfhcX1fepL4pzkYKX9hEzxKN81pmUbyvm2WjGRHdIlWmW6kynS2C7zGLPuDzsut9tIs5Eux0My4vMrFT3Jge%2F8efi1lhsGViDLyOg6PUQRAfREutYbXj7b9XKOBLKq%2FKvqUHRHCCqBhfOm0QOk1J6C8eHoKMVYp4pz%2B2hbMYDSE5JI25nO0WOP8OLeUWr4KfWv9fQ1PwzOsIad5OVhf%2FwCL1tUdjFYLeqOzpNsMbsaJh61Mfklds%2BNkdBepSGayzYj0CcVYHmb%2FmwdVgCtUGReblP3tCccXX2prZ%2BMurcWFvMTAbFEred2TNPjqqOuupKUpR0QhcDgxv6kkOR%2FlxBbvjo8PgZPsu59cmndvHmp7AFEuU%2BCqzYsIoaNy3AZ%2BE8LICXU%2FlQzz%2FruygbD8K%2F%2BxmDUyZttj6Tg0UnFjQor5v85sJDCyk%2FzOBjqkAQK3Kel4mlBuCa6ixNL36DHtgOsJLDAXx%2FBs5uYLpHRV48Vh%2FwhnxoldbpaZCvYlkYYcIVUiMWf3x13RDC4pS740goTy8adDjWm0OTvbjQ6%2Ba75pqwoHicSMdj0k7SnFly8mtqXN1fGpiZgtcs%2B47jtwDXattCr2gJCXM6BcYr66Yl4gU2UCGcfBOZYJ%2F3FExcPD8aN1uqSdLkHIy22ek%2F3Ywd6W&X-Amz-Signature=f962502590db9e5ef91b97ffa30ed3562705ccfc8f4cb9430fe08222ddbf5bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

