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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBVDBPLM%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAm08mRB4ttSsMXBdj0MFUMeSisxskTUTH0CYlI1kgRtAiEA7m3Ys89%2FJdkPPpf3cGWImQfrDib%2B0z2KAQ4n50yPDVYq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGVR69JljE%2Fl%2FesXkCrcA12XL5y%2BoosWrOF46I0PTn%2FcJHyKKUaFG34%2FtYtrqc7vSQE%2BRgHM2JBqcPg8%2FFSVW4Cd8%2F1dh41CcE7hJ6sylU0cWjaabWbe4h%2FSh4hYq7iIHDHKYaHbq3w%2BR5SaG8Wb%2FdzeLznJZtmPKsCRCSpySoKvFoibwAmO4g%2FVskcd78oy5OzXfyt4ZfSAYxAwRt9SXycazvm3xFmXrbnXETOapHBTpF%2BLRMp3AGpJkQKKlyomwM3NcOuu4ZlKVg3j6MendWi7tfvnjN%2BBEze3ree9SlAoSwGOusSGY9CWr4J8GIAZH8tiDVeeP5F%2BsQLjGkSJO1A9mjMTDwp7zw7vB4SR%2Bmx6ROw5QDa71ZvrTZrhsXO3YTC3Z4URKoOd5ddNppwM8ZPKK9jmOGV5BVYlg8oWRDfzHcRA%2FUPYcu22nimCiK0ulvsAzLIp835gWoXtIne4%2FFiy7AUwhFXWXFqKtSccnryaIhHlr108NmpoNOSQz09%2BkQXicHQI6W2ewVfl%2Bk1BLZeBqYyjbcy56XXpgVw4%2FA1cgl9hzGq8oyLRK1S%2FvkYKbPXhxryTImC80MH4JlQQ%2FyuxcuzQ1Un0Xr3MncKep82TIiDEEIJLFbOQx%2FnzP5OkhA0WCrjYJxUa59IKMLSsq88GOqUB%2FvdH99E7LsrinQpKBqNeSJtJpoegxAMcspim1ogBnMFvg%2B2tLJBfK5kZY4CDdcF5nBTNHSuXX2EDD2VAmjQVSm17JGq37HdqMe4sKDXmyQcxH%2F3fO0DGKcKOYZ0ZjgX20rxJq4eEOl3yIH0OdLSm%2B%2BPWobC4K3C1aGO%2F0qBazJh%2FZc19l7gzD%2B6Tascu%2BVQAOZ1WqZdP2jsGhPNgNg0yJgS95DGr&X-Amz-Signature=152e9ad10c837c86aa99f395aad5a015dbf1f60fb7b7a31ff4a9373b8c342de5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

