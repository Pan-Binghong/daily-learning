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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IAL4FIX%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIDLdUlpO%2B7yL3MZHnHWGvry21XBFoz863yvBjobfeJ62AiEAjaMAmYuc2ANrZOijMb8LJdx28JpcODcBPw2LesaUiRgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK684LE5KDgmLTbZfircAyxjk97PzkoLaSh5fsoSi1kJFpb8HQh2rjQ84juahY6lPr6mFKOiHEM1%2FnrxSOxF3nyX%2FPjzK213ANdYCg%2F6aNAMs4KSVEoxxZxM2IcBCIBvHsOQtjlV39iHIHC9cjOBH8frlvET5ohwqA%2FC8%2F7HyMBxo7kE6AFiAry3O4LkT8tvljPSnybwAZ%2F738c%2FM7L2SyzN9riQJPP4mCc%2F5htAWd5SpqTeRf5ijAeFEoqrVot6RbUqs%2FxwDIR1cPOdMRV2Gw905aDRZu69GGf2H1mr6GB6Yj0G%2Bsn82EFeqpF8hVHDiEQmHXEQUFJKAQMMLzjwDGJ0J6s3q%2B%2FabYqpUFo4mZNLqaTQNX4oN0MadQ4fvOKx4a0hcR5wmhJ%2FG3Zxns3XelQODm3qPSrGhpi8Dd2K1mp4DEV%2FFE9Hvi0jbHk%2FXI2fXj2QRWU48TIatHXSHkwulrbIl2u4Jy9Ln0RHd8HUtWpGOs95jwB2u7phYLoV5wAl%2BBk8tYmwoyH9p9pQbVK%2FMQMVYekuLvIe4s6XIqo6XaWjR5kpUA4k2xXHwc0mdWP2U%2FWaGwbiAjd9onfYWRnI3288LtLrIWPoiaJksTuTKUM8NuW1hv%2BTPHTZB5nCoyRyyFYCH0Nzje3dBWX%2FMNXPrckGOqUBTvNlV4SWycg44yyTxOVg9Q2UiCsnyro5vUf4mBBS0c6JcA58G51BlNpdwef2K3rHu165dXh7FLjAt0%2Fou9eCRuIJqT7p5fcrc81OVWd5NLAVCv811cZ0qUwMbyrZACOysxdFmk2yx2Lrkk5yhW2KQ%2FeAaPkptN3pDzA3xNcUsj3fE7KMTnBEQpZaBesZzyNVFuODNL%2BJjemzCUkj33M3Cbvi5h8P&X-Amz-Signature=1f30e1990e5e719e3fc0f7edcd72eadedab44ace7d572f64c3093413ee31ffe6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

