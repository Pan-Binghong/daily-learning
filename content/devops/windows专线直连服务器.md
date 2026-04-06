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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624NUHNRA%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDA2jE%2BDJYqVFVqa607ar3D8ZcDMZMfQKVeTxItE%2FABpAiEA6cvJkqSd66%2BdNQ784SNB7CnuGdw5DRLe8CIiAbVilx8qiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0szVJ1eWxJASgOdCrcA%2Fn%2FX6Zmv2YuLACYg8QVcpNt9SCSws0hklE8bFJhkqHu4wakA8XqfWogHQfog48fEkemXapY6Bp%2BsE%2BOS2oa4xV79LE8epBBtj3cU556czYX48HQUFWyg6xezeg6Sq2myYt9lo4nG1NYZfrgOhnolbFNEjvOKRZY7uBjvLMQm8zG7HdcBeT8oInwILJ35tFANnq1i8AJ9fzXa810MiW%2BIbhB1XtL2D0rGsS4Mp%2BHsR5RN6MLmnJd5cXawEpG32MXRjmcOCHbQH8y5oUR6ArC%2F16SqNymonf98e6%2BGl806EbW0hseOqc850p98ga9ScJQ4C%2FQFDob3SQFBwFZ90v7QMcmteP0uOk1VGC7em0HxfbJ24UC3XuhZUbWyeswwMMNeLLwQkpAYE36A8PZFd%2BRvpOIjnQONmcHbRAu8S9a6yfGSt9urPAk%2Fpx4cMZNOtMtFK1tCHyj%2BjsvsDqvuaok5fQGFEzXRnBlBAp64gM14BjHU3%2BsnlF1NENirgdigYyh2CFH2DWCpAY29VkGyahOhQb0JlMrfFxtEbt8pqoIJyKGttUdZ7NIdsYfbFjbhwooZT7h%2B3vq2cNiS%2B9Cny1LWWkdIoIaO9TZTbTmXfRkMJqhS1riva9f9JJRhRZCMIyzzM4GOqUBRQb2aYPZCD5j5VTGCsPO96UwCmp%2FrzmxRgsAN8bHWcU37fQ9kI3ZutL8DAxJSr0cBlPBaA0z8eQHz6Lw2ziHE%2F%2BI3mUNp9tkseqfemxDQUvnIiUi2UIYbvMsWSwA2ikJdrLC%2FbmFH2DfqO1UqHtQZvBlZVYPuohw0epGj8BVA3Bc7SzZIxgoO72V8wdA6l52Y7SdluWJxIKFx6p1Hh3NmgcZpvnt&X-Amz-Signature=52f2d264a7df1925dcff26a1c09116f2b66f04dc8a6aac96fd198d5cf32a6cd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

