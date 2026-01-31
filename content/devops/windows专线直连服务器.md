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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654KGMGMD%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBnRO%2FCkHl5F%2FQ%2BWBKBhx3tI2rDp5jQKQN8NFl1r5OhAIgUGQuCdxGciF61nKe9XcQsg2zKeTBpXxev1%2BbACM25bQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBTb38XpPdFw1ksfLyrcA%2BoFE94LedsZFcOi%2BR9GBkuscgrDZA4scO9cPLPj4tYS7bCRn6hL3wmA6zzYY5y5L6Po1Irsba5P6OpRKuEbQxs%2Bubf4EGb23ESFEMgkWsBbYAxjtzICOcqcR1mTILeGajigEkeEHHkQwBswNOLw0G8U6pFfISrZTTV9lFcqcF1pyBNv4niyuSLq%2Fq%2FoNk7EZN%2FsJSsPcQxDgKg63J5%2Btcpfn%2BrahFxnqd3vdayoKjkHYjLLvl1mLVluOgA22mb6V%2FrdlkgXTeqhKVQVEUKkC0ZGTqhx9WCUlHN64gnTaSu4in55aqQSVHjDeU7SvME5YyqRUnEmYjimunufwIAoOHj9zKRkzVpkgMfh3YBz8EavYfjNFtteYxZ2a0qunpBOV9aztqoretmX8fA0NJSltUUhD0fML8R1zB1B69sf%2B3YyVoZaQr0gVpASjpUrTkxCS0qIr50H6Qc2%2F8l82vuFLKgsrNC3H21Fk6k6%2FofzXmZ33ny3XAS5ajbWy0ejPh6ahtBPfutQpZr1CEv1lRwFujGbbymP%2FnAy%2BCZbctiT%2FO58EBG1gfqHH%2BhJvCJdEZpV3Fd8PdjGbTR9%2BF5tIi3SKPFx5nKx6JVoikQWTp9nCWZJrse6m7z5gvWDsmoYMJfM9csGOqUBkbGk6E85MNNFrN9m41cDyRZ5ZVxrc9suj4pefjCX%2F16dP7ENIFWdVlDZrytxshgf7cua2g5NgHhahy0hxOP8UO710QK4224TLNof7AfDqWRtXure6V3DrOhuiH2%2FW3WiikcdGwP7Dzal8m2J2URuuHcEa5HfRbRBHvIn9q2YCAuYfp2CTdv48yzqpYDTyPZ2pm7zgMEJzBNyH6xgB2kS7qPVpi8S&X-Amz-Signature=91a3f4c633cf6a8902b45e953aebf192d998d95baeb8d1a817a16a449dfb88f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

