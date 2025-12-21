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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTVIYVW4%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIGAuN2eODmLjXrVjhiRRNvaOcWbtTPkLQCxQOVJIz%2BhjAiAlGmaqPdVsuUlMHnH4kBPPCZHZs5%2FrTYaO4M09QaErNyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML8q2%2FHACbJ70%2BPmZKtwD3dCNn4OYhEOt%2F3ecFEDkMTM4xjv5GaqphTatb0dhobaV7YuhOa8w%2B29aO%2Fqh7b%2B20grSYB0D7vrGfuMGELp3sN9xkkwIWUUQhJ3VDu8T8tIm0RtEkKqG9fLrdIxOeG8qoOeTFcKEEa3dYysFcgowcR%2FG8igVXva%2BMQzIaOq30JwEte5zFjJXmXN8OQSyTg5ImNKC9KT%2BkdVkXt%2BUAI2Q%2Fr%2FSbKuJmWigtZ0zZJvF%2B9iH%2BnzixBqCCNJBz5XmWJG%2BF4mXsfYFPvOP%2Fe%2ByNVSSnyd2JDIghXJoPQ%2FNcgQIRp0pVLnZRkdDpWhEiPHsXiPer2KjTMIIVp%2BUWW7%2FpqYb7pTJdTiKaq6rLObMv9fjBJAskgglJrWh2XHCiPrEUSr8CJIsbDdEkFJraIWysR9papYhjD9dR8eMRAr1pQWu3HKBdXp2YyQkSr74UjmW0Qo%2BL%2BNBVCtqsKTK%2BK5x8rvRUGbwwsyQ6F6Jlsg78ngARPLePsMyO%2FAMAUAwYb4C9UQ%2Bf8xyeusSzJkd1ekkQwjrPijX9MwDYD41AdUqDqsBZ5HWgDc6DT1mqsN7n3T3Wt6wHV9cSSZA%2BfMqHP9FbC9vzkDt4tKiF0Fgta%2F%2FARWDkHygI%2F4a%2FfurconPfGYwmPicygY6pgG9GC1g8on6pbeBRiu2OtEwDO8DPpiaFIPfCQ%2Fkmes4rWQx2ZPm6KkLKRTOzU2MO0iCz5qEhf%2FaxhcRDbgwxZD6zTfEW3bH1jjjQdC2Jf9YIC96vFHmvcHeJn15Qu%2BCM1%2Bbqmz3sdlI6Cu5PCd1xAoxAgq5zJ0UkrjssOZ15Jf6%2BcR5MQSUCPsVEwGlZMT8pVVA%2FctLYtBXF4YCcgozqAcM1vP6j%2BSi&X-Amz-Signature=a687578c64db92217e275fc43e476d63ec9dcb56c864c957aefdf451ece86595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

