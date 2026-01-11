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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR7B42ZR%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDleNu%2FYgNd9cxMpw%2B361%2BH6OdtXEM00lT7MaWYecJpQAiA8aNQmEJiJVrtfo0%2BQhLX6VhI52bbVTbxZWR1qrRQKuSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwT0UrHwdG30IuDRNKtwD2fm3VnSCQ88Nyxbg2ohC7ydkqfa1Lx8HYTjwDr1b3x%2FALgwGBW2%2FFzznm0cFBehxFAOtDks99XyGXcvb1lN189MDOX7%2FNLlsBf4maQSBnaDpCjvnbPIcKeLuoR%2F3rm3R%2BP7DLLpZjRw8AycfJkwIh9gc1hE6HN9mNIxsCrVr3Jm0o4l9V4AcbCwyQb9Wn06myfD0yOkvGtMLPvnTGdHTelvyNwf12B6GUJPSk31I0avTe7J7K7vkcUbi1UtWn0QO5yyI9%2F0AX8eXrLrupgCP7lpGffLCgMyEeGDQjtYhuwlCzfakmo6kO9HShl4PGwFRU5WTLvMI0fVRy2Zg2r5AGgU0H4QGTWllj10vKhWMiwNlunfN%2B%2Bxv5jhIMadN1%2FT6yquvpT7P%2B2wYomnR5wrA1Esy8jcw2ZeT17EVIUfmwVKPUOURXtly4FKgnLChMQvT181FIxpvlpUqLJFU3v5l9CVKecgLwPaEViG5vEdbmxyR3lJ2bHM7R95gkdr7iohye9fD8ssrkqksCMGrqA9viYGxo%2Boe2mod0SsjbP0Dc1bZFjslSKrWsUycXsZXTjP0HkudzuYaCm7%2F%2FU3eBHu4FzQhd24jkQa0lbRrMljnhcJme2riSn9BuxoWeugw%2FPiLywY6pgGMUHK%2BaZbLm8SAZEEcpZBv1Ay10k190QsNxVuNf4F6JZ3sdQWzTgi7FHnDxs1DAhyYeuXOiRrzNkocz22YmJwZBSbSsgTYPjzt%2BLo6KxaDhJTFvMKtKE%2BTmSEeDCIF9%2F561VI43WyFs7KKdJjbJd7wMnGSG8CI8NfxMZh6XmihYXecoQiwKE6XmHQ3U4tRKbrlyBQuiBR%2FEdAAy7ju%2FRV3Ea9G5z7w&X-Amz-Signature=3483e15bcb49b1580c0ae3c52fac3daf738da01bac565a09242382ae49820f44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZR7B42ZR%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDleNu%2FYgNd9cxMpw%2B361%2BH6OdtXEM00lT7MaWYecJpQAiA8aNQmEJiJVrtfo0%2BQhLX6VhI52bbVTbxZWR1qrRQKuSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwT0UrHwdG30IuDRNKtwD2fm3VnSCQ88Nyxbg2ohC7ydkqfa1Lx8HYTjwDr1b3x%2FALgwGBW2%2FFzznm0cFBehxFAOtDks99XyGXcvb1lN189MDOX7%2FNLlsBf4maQSBnaDpCjvnbPIcKeLuoR%2F3rm3R%2BP7DLLpZjRw8AycfJkwIh9gc1hE6HN9mNIxsCrVr3Jm0o4l9V4AcbCwyQb9Wn06myfD0yOkvGtMLPvnTGdHTelvyNwf12B6GUJPSk31I0avTe7J7K7vkcUbi1UtWn0QO5yyI9%2F0AX8eXrLrupgCP7lpGffLCgMyEeGDQjtYhuwlCzfakmo6kO9HShl4PGwFRU5WTLvMI0fVRy2Zg2r5AGgU0H4QGTWllj10vKhWMiwNlunfN%2B%2Bxv5jhIMadN1%2FT6yquvpT7P%2B2wYomnR5wrA1Esy8jcw2ZeT17EVIUfmwVKPUOURXtly4FKgnLChMQvT181FIxpvlpUqLJFU3v5l9CVKecgLwPaEViG5vEdbmxyR3lJ2bHM7R95gkdr7iohye9fD8ssrkqksCMGrqA9viYGxo%2Boe2mod0SsjbP0Dc1bZFjslSKrWsUycXsZXTjP0HkudzuYaCm7%2F%2FU3eBHu4FzQhd24jkQa0lbRrMljnhcJme2riSn9BuxoWeugw%2FPiLywY6pgGMUHK%2BaZbLm8SAZEEcpZBv1Ay10k190QsNxVuNf4F6JZ3sdQWzTgi7FHnDxs1DAhyYeuXOiRrzNkocz22YmJwZBSbSsgTYPjzt%2BLo6KxaDhJTFvMKtKE%2BTmSEeDCIF9%2F561VI43WyFs7KKdJjbJd7wMnGSG8CI8NfxMZh6XmihYXecoQiwKE6XmHQ3U4tRKbrlyBQuiBR%2FEdAAy7ju%2FRV3Ea9G5z7w&X-Amz-Signature=4d8ac4c677f1f9d904b4782119cf887ac268183a34d7538428169a5b9589decd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

