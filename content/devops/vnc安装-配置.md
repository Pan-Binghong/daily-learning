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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNLD6ES%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgNe6HHEYmAwCm9qY6RX7FIMKguDzgK3aZpRqWzyj6%2BwIhANdfpVknPKobxfGhCsXRsdp8V5Ixx6UMWHGQrJSOowJCKv8DCH8QABoMNjM3NDIzMTgzODA1IgxACg%2BOwqtTVZjAWQwq3ANB7%2FqgKUJlf8pft11p99lVq4ZiCt8%2FHYrekTaSI%2BmQM9KcJ8UrEXLK9abe58C4GLEW30X8OpKqb0B8AC5VCgzW8mBdh%2FOV3Ya%2FMd9e3285OX03EbkY5ja8Hr%2BF2rk9ePNImdp2s0TiNJpmjhM%2FcXROdMUYAKQj%2BnSly2ZDxwXEnxlAXonHPK0mGVc8VQbKbbrtD1ZrdFFybT2OV7zAxWCffgrRE%2BqUgwO7X1H0TZTQg10z6JwM5PK6XJsoflJW4nGUhC9A3uX3XahzYnDvCgu%2B8FfhPTZH%2Bk0Oce4dry217uvTHELDMikBN6lOoQKbt1rphYQfBSF2nG1OPxL3kO2u34ff1pUDZkX5WzJPVBqrRQRjO4ashJPi8gF96Bk3yJAg0iJaxY%2FtDd7e3ehR4cdbz24YIRAfAcaDZ0X8a4FYCjLqog57HwxYaobzpLmleRkzyLdjReAe4jopdsHIUsUR05EJmwnR4nEDZkWNV2KgQ%2Fl%2BZB0vPPcob1TxjSCExBFgZ9mbyQVPzAkdcLh6%2BpOptSugoC0R6rk%2BALGwZQvd6TmS%2Buw6gO1ZvyGiyJH42KR%2FO%2FTCbmLO0ZoehlA63ulbxG4h3H%2Bk9l%2FqNo%2FOJgYuALJf%2BpGjKX0oGg5%2BuTDLrL3OBjqkAUO4HXR9iqet278WhzOSog8niXINXYN3eqprVOuQirEhZcHNX2y0ov9ZvxblrCiWXLuh8bTEe4F9PgI7OaTwCb5qZ%2BNSJmgkv27GJw7QEuYv9LGW137%2B12uqaOyOodb09KtsBrEUmA19N4ALoC87GyGKQxDPeGX0F6vuw6SE%2F%2BdAvrZ3YEph4WCF501XTHvyRqLarDQtsgT8q2A6xLHYjgliD5ii&X-Amz-Signature=77a9618e8e745c9a30c464a82c856e7f616a92b2135ab9851f71d5112ac54ce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBNLD6ES%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgNe6HHEYmAwCm9qY6RX7FIMKguDzgK3aZpRqWzyj6%2BwIhANdfpVknPKobxfGhCsXRsdp8V5Ixx6UMWHGQrJSOowJCKv8DCH8QABoMNjM3NDIzMTgzODA1IgxACg%2BOwqtTVZjAWQwq3ANB7%2FqgKUJlf8pft11p99lVq4ZiCt8%2FHYrekTaSI%2BmQM9KcJ8UrEXLK9abe58C4GLEW30X8OpKqb0B8AC5VCgzW8mBdh%2FOV3Ya%2FMd9e3285OX03EbkY5ja8Hr%2BF2rk9ePNImdp2s0TiNJpmjhM%2FcXROdMUYAKQj%2BnSly2ZDxwXEnxlAXonHPK0mGVc8VQbKbbrtD1ZrdFFybT2OV7zAxWCffgrRE%2BqUgwO7X1H0TZTQg10z6JwM5PK6XJsoflJW4nGUhC9A3uX3XahzYnDvCgu%2B8FfhPTZH%2Bk0Oce4dry217uvTHELDMikBN6lOoQKbt1rphYQfBSF2nG1OPxL3kO2u34ff1pUDZkX5WzJPVBqrRQRjO4ashJPi8gF96Bk3yJAg0iJaxY%2FtDd7e3ehR4cdbz24YIRAfAcaDZ0X8a4FYCjLqog57HwxYaobzpLmleRkzyLdjReAe4jopdsHIUsUR05EJmwnR4nEDZkWNV2KgQ%2Fl%2BZB0vPPcob1TxjSCExBFgZ9mbyQVPzAkdcLh6%2BpOptSugoC0R6rk%2BALGwZQvd6TmS%2Buw6gO1ZvyGiyJH42KR%2FO%2FTCbmLO0ZoehlA63ulbxG4h3H%2Bk9l%2FqNo%2FOJgYuALJf%2BpGjKX0oGg5%2BuTDLrL3OBjqkAUO4HXR9iqet278WhzOSog8niXINXYN3eqprVOuQirEhZcHNX2y0ov9ZvxblrCiWXLuh8bTEe4F9PgI7OaTwCb5qZ%2BNSJmgkv27GJw7QEuYv9LGW137%2B12uqaOyOodb09KtsBrEUmA19N4ALoC87GyGKQxDPeGX0F6vuw6SE%2F%2BdAvrZ3YEph4WCF501XTHvyRqLarDQtsgT8q2A6xLHYjgliD5ii&X-Amz-Signature=c777cb8424798bb997948342f24150f959e6adea70af4a8eb4819c48119bf49e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

