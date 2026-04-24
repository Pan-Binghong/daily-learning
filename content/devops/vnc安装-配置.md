---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZK6HKU%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpn0OYLd50CfmXUYe%2BCbxqbWiFXJ4zRm2DNz131pFM7QIhALS4DIGo0631ZdNP9jvyYu3ImxkdDCf5eWFj%2BXvytwg0Kv8DCHMQABoMNjM3NDIzMTgzODA1IgxKVxyCr2fEntx9%2FUkq3ANuM4KpZiu5oT1otD%2BeMoHkrUerp6Oagpu82gB45aAS1n%2FsKSYAceGx9aEKuOj8AiezZiVLwR4ljis9WnTY2TPLs9zLk02Ee1Qmd8srXZJoqsp2%2B%2B%2F3AchqKcJWZbOQ58n7fWWdV0LtRe0AVpbWqDweYGdBL8EvenMoM7xF4tSM0NnQ0Ly%2B7f%2BUzBETUTz3BO085tiJOa0JBqMPF1EeDUvafAHVj1YifVZ3%2Fv3WOebJ52F54bKtTG9Y7265KPuwZHbWSlvxrRM12IeBkR2RqOH0hcTHV1Xs6ctCPHTXEJ2XfOZ4XZxRiSEoXREOGrbR7ElHhVDlXg4VnA9BvHL0NGe1L%2FnYeNSE71PMvHtiBKcN2wHbvXiO8c4Cq%2Bw%2F4qn6FIpE42zvBQPjSyzDYyjsvoZl58AdhRysovM2iDhP%2FebURotRVmUhcISPTLAcaPsQPhC19Ijjy8S%2FB5kHSyY46lCubWaFwLUjGKVNXTNYwMsIaZf2SwhQ3hXGJIxCrGCbo%2FDLi6kXizWJrAADuJWmrAOsD0e%2BLxePR1tnmd62eZbOLXfYNFM39YrbFqXem9JWDiTd1%2F75OvRhzBf89MUeINhijOsT4CepqOAN3%2FhcG6Vp7HXgC5Srz500TsKw3DDVpqvPBjqkAc%2BYtpSWjLdpsv9P%2FBy3MauGwR4oO2JFJWl2kyIE0icCjacVgh98rvf3g7nA8ewTWXiPsg5h%2FadTEjuT9axT5WX9Qu98PVW5SunI33MdbbzRQCXflsewe6zVTo0qUHSzTqTzrj0v0hnaZKY3WrWMsOiV2P9%2Ftp3stAQMm%2BZ%2Fcbgl%2BxIE7g6Q9Ny%2BQiH2JlsrxSPAqzhBOL7f4f7hrCl4RltJnCsJ&X-Amz-Signature=a9680dbf7e4ebe491c16e5adf1502f82836538f278b1cdbc45119612c9be97e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFZK6HKU%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpn0OYLd50CfmXUYe%2BCbxqbWiFXJ4zRm2DNz131pFM7QIhALS4DIGo0631ZdNP9jvyYu3ImxkdDCf5eWFj%2BXvytwg0Kv8DCHMQABoMNjM3NDIzMTgzODA1IgxKVxyCr2fEntx9%2FUkq3ANuM4KpZiu5oT1otD%2BeMoHkrUerp6Oagpu82gB45aAS1n%2FsKSYAceGx9aEKuOj8AiezZiVLwR4ljis9WnTY2TPLs9zLk02Ee1Qmd8srXZJoqsp2%2B%2B%2F3AchqKcJWZbOQ58n7fWWdV0LtRe0AVpbWqDweYGdBL8EvenMoM7xF4tSM0NnQ0Ly%2B7f%2BUzBETUTz3BO085tiJOa0JBqMPF1EeDUvafAHVj1YifVZ3%2Fv3WOebJ52F54bKtTG9Y7265KPuwZHbWSlvxrRM12IeBkR2RqOH0hcTHV1Xs6ctCPHTXEJ2XfOZ4XZxRiSEoXREOGrbR7ElHhVDlXg4VnA9BvHL0NGe1L%2FnYeNSE71PMvHtiBKcN2wHbvXiO8c4Cq%2Bw%2F4qn6FIpE42zvBQPjSyzDYyjsvoZl58AdhRysovM2iDhP%2FebURotRVmUhcISPTLAcaPsQPhC19Ijjy8S%2FB5kHSyY46lCubWaFwLUjGKVNXTNYwMsIaZf2SwhQ3hXGJIxCrGCbo%2FDLi6kXizWJrAADuJWmrAOsD0e%2BLxePR1tnmd62eZbOLXfYNFM39YrbFqXem9JWDiTd1%2F75OvRhzBf89MUeINhijOsT4CepqOAN3%2FhcG6Vp7HXgC5Srz500TsKw3DDVpqvPBjqkAc%2BYtpSWjLdpsv9P%2FBy3MauGwR4oO2JFJWl2kyIE0icCjacVgh98rvf3g7nA8ewTWXiPsg5h%2FadTEjuT9axT5WX9Qu98PVW5SunI33MdbbzRQCXflsewe6zVTo0qUHSzTqTzrj0v0hnaZKY3WrWMsOiV2P9%2Ftp3stAQMm%2BZ%2Fcbgl%2BxIE7g6Q9Ny%2BQiH2JlsrxSPAqzhBOL7f4f7hrCl4RltJnCsJ&X-Amz-Signature=5ef1ddb329e070637319f94f486c624f239d7b02d3b442e426a40d514217733e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

