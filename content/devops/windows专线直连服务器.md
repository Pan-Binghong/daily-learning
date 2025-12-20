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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZFO2QT7%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCe7qs%2F8CwHfsW4GnlC3DKMj0BmMqa%2FyLYZRScnfdZcdQIhAMPK76fqL3IpH17MspJGbYn2EEHrxzQbBXiOlAoCQouuKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxSRjEMyGZ1aW%2BfpQYq3ANc9nJXY%2Bvq%2BxDdWBj0oIIpp9ppkvRI25vLDvSMFWkhULFg27KSVlw0m14bOB3Hs0YDRjN%2FBZSlmWxuprVmb9nY4MxK8QDWmVNVRgDYr6XwfLVfpEA10XsjELEH%2BjPNTvZVDeQfyjx7sfV%2FCM3mwwPB3RZo9zqd2FIqlWqzOHd%2Fle0qLnyBW86CcgUNliGHZA9XMueYIWOVmOFeZcWoSNPRCL%2BN771N907i03PcVisN%2BI%2B%2BRb8w2RhYEc024udh1ETZBNxiekdeWaNqUTmdltORhiN9cM7vMXI8sKIECRD%2BRBf9CgggBqKQbqZeqn1IZN0L%2BkXGyf61XSaDMhZr6OmGNzTKvVwdrqZxl5mx22zls7NMqoy928O%2FE0YNI4Js9bqCyK60myi%2ByTvn2j%2BYB%2BqxtyN4CC36V79edEy5P3ws6JaDlp7zGS4M2pJjkkbwYxRse4P5rpVFm4H1m7tgNWrcUgnt2b68q9WGbiDq5gQ7LUNlHnAmAQIVvCOZ9qhoRMAfHjOWRe%2F3jfqeeaGL0iywFxwtZirPR4nWkUOoZ0vOGyly1EpciANunhyBZV5DOusmkmOJnGE3CCYgzFf4jukfJ9mQJ1fWtLLmlifXAM8s7S26p6XTXjVvDTsgqjCyhZjKBjqkAYyN1cwb8t3%2BLVrc7DuJLOunbS33F20MTMxgMJKl2O2GUepQJNnJ%2BKMnkRX6pIUxabStKVdnJ9VInLB%2FjihRuu1p4amzkkN0fXMbmjZEe1I302uO5brA45FSkY6s%2BM57nb2t6ArbMInX4PV1YssIGTz12BiE9V7afvdYKIfPt9DDmjEe2l8JgrH8Bqg8UNFc7zDgr3zI9W2t%2FK6sodQTDRp8K4Gq&X-Amz-Signature=4b2b309899a8b2dccd9e4597a0b79ede596f8964ccd9725982256e231a85e63d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

