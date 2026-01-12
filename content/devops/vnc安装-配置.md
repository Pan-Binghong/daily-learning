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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCKYAHIB%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBJpcK8ucqbM36%2Fg0QMH5jZ4AW02UXnxHVwBFmPY90llAiBG8IR1%2BSetVoRfen00x%2BeEaTaBbFRnpX1qLsKqKo0%2FDyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbb2p64iOQWy8GPFNKtwDTNbsel8r091mCRep1grph9vP9UxisFKlfk8AUlmJN%2F3PRqi22yxuad4rT4pyX1mIpQQ87jQcImNalzMFCtwjx4LzvRp9MuGtbd8o%2FRibat39dBHNjneyooatRbWzNYky0dBGllPbK1S95vumbLJAAZiTNaLtNOW8jPxibPpjQlZoX1KCMXR%2BTqLg6kUYaUIDVT2YN41D0ygmSPgkfSpY5CWwoR9rnVJzCCe8L0uAQc9QJ7e9TTc6hQXDfys2iHHjk0bJsNsis2Lnhp7PykBE3CV4goRsvzddrbkVm7wgZdMHmeSa6iRqGUd%2FmbOBvONs%2FBfEudx3FekW0Y7pByhNoUWuUNc%2FKIKoPK1yrSMYQCg6y%2FIuiig3rUP%2FsLqwJEZTkSlSxblOsNOUTPjbVZho5Oc%2FPYy1hEaIElNijA%2FcDgtrmS0vgbx9KLic4H8YJy3gOmwYyj7VKFZ1Kk7mGpRP%2F2YFUjQghehP11tlpmiUB5mzd3RIAanisF3jInQUuSkA8VvHHOlySr6np2Sk5hsawh94Xe%2FHeGqmy9jRD3tLd5Qov4Fbt9%2BOcD06wXIuLPlF30WUpfawpspqu%2BJ6sbWVQTyySYJ508gTZ6Ogtyl6UOZWLEOSzcXrHlTu17Mwg%2FiQywY6pgGMo2wjBZG09vY2liGu2errNmjmclxUNhsO%2FhEB89GIwQ17wtRyEjioXorUWaPvDlIm0e2NFHRebj%2FqtVd99tgcGthSUYRoDieLZQ%2B1hEopBPMVWafoDWJuWuTi8YvHbnfLSWKlKSF%2FgM4vQBtgQF2HUnbKcLClLFyDyQk5pys2a9sL%2Bsk%2BBme0QlWEj64lrj6IQKPn3iMfscqhcccegv2pdBjVnEy0&X-Amz-Signature=27fc05ae39df31d99a047fe09ecb311da0e3c50d725b519ad669ca19ab2deb6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCKYAHIB%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBJpcK8ucqbM36%2Fg0QMH5jZ4AW02UXnxHVwBFmPY90llAiBG8IR1%2BSetVoRfen00x%2BeEaTaBbFRnpX1qLsKqKo0%2FDyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbb2p64iOQWy8GPFNKtwDTNbsel8r091mCRep1grph9vP9UxisFKlfk8AUlmJN%2F3PRqi22yxuad4rT4pyX1mIpQQ87jQcImNalzMFCtwjx4LzvRp9MuGtbd8o%2FRibat39dBHNjneyooatRbWzNYky0dBGllPbK1S95vumbLJAAZiTNaLtNOW8jPxibPpjQlZoX1KCMXR%2BTqLg6kUYaUIDVT2YN41D0ygmSPgkfSpY5CWwoR9rnVJzCCe8L0uAQc9QJ7e9TTc6hQXDfys2iHHjk0bJsNsis2Lnhp7PykBE3CV4goRsvzddrbkVm7wgZdMHmeSa6iRqGUd%2FmbOBvONs%2FBfEudx3FekW0Y7pByhNoUWuUNc%2FKIKoPK1yrSMYQCg6y%2FIuiig3rUP%2FsLqwJEZTkSlSxblOsNOUTPjbVZho5Oc%2FPYy1hEaIElNijA%2FcDgtrmS0vgbx9KLic4H8YJy3gOmwYyj7VKFZ1Kk7mGpRP%2F2YFUjQghehP11tlpmiUB5mzd3RIAanisF3jInQUuSkA8VvHHOlySr6np2Sk5hsawh94Xe%2FHeGqmy9jRD3tLd5Qov4Fbt9%2BOcD06wXIuLPlF30WUpfawpspqu%2BJ6sbWVQTyySYJ508gTZ6Ogtyl6UOZWLEOSzcXrHlTu17Mwg%2FiQywY6pgGMo2wjBZG09vY2liGu2errNmjmclxUNhsO%2FhEB89GIwQ17wtRyEjioXorUWaPvDlIm0e2NFHRebj%2FqtVd99tgcGthSUYRoDieLZQ%2B1hEopBPMVWafoDWJuWuTi8YvHbnfLSWKlKSF%2FgM4vQBtgQF2HUnbKcLClLFyDyQk5pys2a9sL%2Bsk%2BBme0QlWEj64lrj6IQKPn3iMfscqhcccegv2pdBjVnEy0&X-Amz-Signature=9c94e3e57fbeca7d3e24925bb1b2d7caaa3be8a14b3d33b81c687b3747b6bdf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

