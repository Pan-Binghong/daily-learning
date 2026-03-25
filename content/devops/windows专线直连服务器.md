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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVY72FWJ%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBdTfVUEavth4LOQ5WVZfXdJESttDHzjaxkoVpWFfHjQIgGIce06LE22sE%2BhlirugdZ7dG7G2TjEyyRkEZKx448vUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJZx3nDSC2oWYyPNtyrcAxezUi3hougLntbaWxNJV6izHjp6Z23Ju8OOzQDmcTLpxJgwyzmFAu4f8Lgugv%2Fj9iAgDztjpd2XXFm9OUSleqBblIZtQmRBvo0NzoUlfXSYO5KXaEH4TzRp6q0XCTpyLLNl7shcN5N%2Bavop2jIK8mMJOCPwvA%2B22aQMWdtYRrELVprUlgL4iP9T61F9BwgUEnly631ODbCCxKPN3CwcoNWergUs1v%2BVFisQF%2Bgte6BcHh3efkfFxBf%2B15vh8vJrhBI4FQuu5NxQqixvbVKR2dQE2qEkq%2FO45qghyG%2FFz9BAQSqY%2BXQmLqWJHva%2BhsS7v%2BhYfmCxO1pcBOwW0uPBLeSm7TAossKmIpKFUY8TcZaXxyTU%2BRY4XcKRlKwvcxAS4ylog9hGDdz93%2BvzNO2k6vClqgAb%2FBN3VaCtAOAzroEwTJ5gxUHgXreIOMN4DNp%2Fz0lSeP%2FAVz%2BTQ%2F53tLvGUdmxYqXFCkdA4zX%2BtcRkKGOTpOJngEtz%2BTGKYXvTm9GohYkgq1266wj4XkrudzOfVblubRcA%2Bnxee9AUfhTgWHgT2uRGZ%2BC%2FC9XJcm%2BfuMXip3XHTDJGIdjm9q0oQq9agYiYAY%2BvLGPA2mPa9A03eRk4dRTRL0eUZkVMFCgJMIfWjs4GOqUBFFNFr1bgm7D1VzjZw59lmkVcJgS2pcs4hEwYEwabKqOU4l6Xc8SjXOSi6ST8YabD%2Ff1gW60gB5tCl4JpahrdpvIKk0yni6if4wE%2B0%2FzRkPts1dKAJB6H1kZNC2EUo0%2FODoASHwFFKOUjwHcmfoDw9sxjx9Bs6YsE5bAaBVZvWd6Mf67CJpRUAD6NkOI0JhpOCJmS8QSiCiGiTl5PPZEv3SfGUGdL&X-Amz-Signature=c08f5474deb7d648373fe00c65e1620933c980a03f43b1a58778e4e2d50334b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

