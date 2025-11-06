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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVSMYOPA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdjuzN1BeAEGn3%2BcMICetC9SvUxPXQsFNXSCdEk8hzPAiBHBXL6GrOvZEhQPhjpn0VPqjgX0wSwdLGS0hW7eK8mHSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8MyQYyVIm9KX7So8KtwDOw1C%2Fb78NmsEvjwoEeMkjoVTZ8f4F%2BNqO%2BYSxNtRtPHvGyEIpXudY7iqkQ1XR01v4Qxm1PDUuWbywOQff99LJUUTXPJBjfihGn2Vu1h1dk7Nic3lzLpQXoM4LDud7%2Fd%2FG8KGGDVv8ljXQ%2FWjq%2BGlSwwLjYC0eEyphjuzxipAvxqgDjxZOWIS6Z%2BfM9llQkO0sRMQqeMcM%2FYxCv5VCbS7aHBEYq%2FiI%2BhrUK4HImJUzm4SvXE8A1wdWOy0%2FHSzkuhxRU1fJPlsSNh3q4%2F9LefUuAusIIUNYMgK4LHCA%2FQwwphbAZugZptjXlG86d%2Fg73rert26h7N75VreszPXtTXCSM1fznBjMKdjYuWfCesmRkGT%2F4pxmWzLMpjQpBCDXcy7kKnqMHnrW%2Bb87QskAT1Cb3kFaC0mw6geuDciHTv28zpPZ%2Fs0puV0AvaBKOy8avmG8RD5eB0ECxDVvfhIeWNTUS5tOt4%2BvkI6NwtkHC1GthxvBzL157flLn8Ewy6p0thPmlx97C40PDnaDZAsaCy5I5eeEqnnn7tPHtfQRLpdc%2BuydR%2Fst393FIIo8eVztfwJJC5z0HG4aZeBwu%2FeXajFbuicXbsruB%2BpxRytzeAij%2Bq%2BV2BgrH069ctVUzIw0PGvyAY6pgFbJWaZHIJhRMzsColK%2F9qQiwSxNV2nzr6mKkaEa0%2FxI6PVHIMjGyz0bE4g9dBQpQRvtsM9q5n9uRocJIXagSmeIBjdts3j9FkSZizDHeAzKwlOZAklDJanjf9OQMvRg9i5dycnt%2FUdpQb2vd0VWzO6Ylkd3n0Ike2mureibSEbSCL4JPTkeiO5sPOOAhXv933sQzvh67c5ZXr9Enc22anU6HPwGioM&X-Amz-Signature=5ccb0ce0b8ff8c3c8c1433c972c185d2653fa5f857e779f1f52d7f612875fbaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

