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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652GOT7I6%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIA8EDcF4%2BZh%2F%2BF%2BRw0Kx1QAQTTz4R%2FQk%2FRWl3AEUXRx1AiEAleqp4hOKatov3UWUALBWJa02ptppnwADnj4ArFXCE%2FQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOb4%2FTG7FFys2Rv3zSrcA5vecErM3zaGzAth8mge7Ki6ghzwmndQZP4PVGizkgmnItAQgeSyhda2vOtLQw%2FIR1kU2hQrBB%2Fs479pSAw4ie7NTKsKg6BQNXXnjXFz1snihDPAp8o9PXBl%2BQm1xyRu%2BXN3PloWQeQUqYZvNagxFFRV5lFG%2FiVd7rd8U65eYfU1h5vum0Xt9ZMyzgmtVJEu5JpouwYClVFqN3Xdio4fgGgL0UhhsGFyAkukcYIEf3yByuM7Cvcqlm%2BnZEDSgLwDSJtCdKkBoc8DzCgIGJ86NbVZ5s7GTJ1Zy5OyqJRtU7xtY6FEp0O4T2Xxcx1vk5FW4pC47z9AAhusMSAJWTCIrZemKNM46ZBxpd8pr4hgqj1MqTyuqF86062k4yyHtHfuwURhj%2BmS7eDURu6pkCl%2BcUw4ESdmb7htFt9UqChwuZqpV6XoxVUhojXcHJzx3RqdJkHgcOWasNtQF8hPeodDq9EsAE1QqYUMp62OPxYFR84LvYmICWXCtfnobnpnjAfNO6i0PR4RrZa50YVSg8O6bC7aNr18FrPmypi3D6euEn8qakSClZwt66ns%2FIK5UxXQz%2FfM%2FbN%2BnJmKAaeWiJluxpiHMmQMYTM06DHrj%2By0z2cn3fRFdddSdUq0zbjdMJjsnM4GOqUBFTdYZxZovJa3ic79uaVxNyPi4j9DBR%2BzrxK4E8OOyOjF%2FdWcfN%2BNTucsoyz6plIW3%2FqD3z%2BmhgT4YeuRKfPJ%2FjRHFd4vJEAOcNJ9i0AOT5vNKH38gNS4Rtoo3JcCq8xvFE%2BYfP5jw549u9TcUTCDJj7TBw3iEB06jbIPrZ9I3nGgEmjV%2BBRPmyCZeYpVqhGasCFT0SohnH6hATOFBbT7XIh1%2BlmV&X-Amz-Signature=ce61d45c26978e2ba1091bdfa286ee418d413f5e2219aa6e6fdb0aae2e9310ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

