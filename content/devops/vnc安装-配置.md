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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WJ365UV%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4hCMeh%2BBGILF%2FqMDkpB%2BldenpM2Q13VO457qrBf%2FUewIhAJ7tOl3Y2lt0J9pgWvQd5itwTmNtb7T08bQgz48f2LVmKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4zt%2FduF0RlLBC9pwq3APaFBMoOLOb9wdJH5CqHUZOBSBLux9B4UJpQ1Ue7tnzCjTwSIT1VJvVOyVI%2BsleR0Xnc1H6RGXsm5M88IKQmUpZRZEbqGWZ6PJplsHcZsoLXuA12cI94EhqO4z0G9g4Aeut2MFCa%2FyEUUknPJ0kYlunDGHZmwwEk7Do8hp2lncb5241WxEs6NSuugy43ILlLemroT%2FCjbEsVkA6bGmjFNxDGUa8tfjAAYOuxFGiVr7op7jKxr6njn9ZJUKtix3pE6J6MjBjbiO4JTAsGbr7nZOffnc0KDbKg%2BkjcHEyaAmWP1h2nPSENibcPE0aLX7ivKqgqvjyK7HZrsNJiTJi1kDtX3Vi5q38aZ4SyH6YzJ0dZjJnDgB0Olw5ID3hbOFfyYMn%2BRlFneaxqIilUjzGkwflEmI4SaAPU3z2YDDLc7CndLP%2Bs4%2BwqBJ83x4yEo7ytrsowklqfRL2jr%2B%2FJVaXMU0b0G0mFjUk77bAHDHQn%2BiUx94yyVCN0v6%2F6GnGhA%2FlNRSC6aMomzjUf4ograp1gVkYpCqH1JNxNvq9vAt1g%2FXB0DSCO1hGu%2BgJ1%2B0VOIQBQ%2Bo%2FQ5NjVTHSzlndjlL98p3uYBB9uQmjh2bUVM22V668HXveS7PI6u%2B73eNxNzDepY3OBjqkATmERASUln%2Fg6xgK9EPTJrJS5UH%2FlmCvBhbDpcofEYTYaG8bcUhpAu8KreUWZ6MdHS%2Fth4PZ3GdbBxgYGTuUIXLtudRQeXzmW8pDe%2FNy1xuHoWLueLATt3TArrw6rN962SJUJcSqumZrL4OlNL0cyaOJil1oDR%2Fkn%2BDivqEY8jpumHD88DqdOVYqaAa0u4Lp79b58ZJr9Okegmh%2FkV6mZ1L7hw7Q&X-Amz-Signature=d838efb2868d8f760f859a8546cebde540d7fb59c33383ac0f1611139fced18c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WJ365UV%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4hCMeh%2BBGILF%2FqMDkpB%2BldenpM2Q13VO457qrBf%2FUewIhAJ7tOl3Y2lt0J9pgWvQd5itwTmNtb7T08bQgz48f2LVmKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4zt%2FduF0RlLBC9pwq3APaFBMoOLOb9wdJH5CqHUZOBSBLux9B4UJpQ1Ue7tnzCjTwSIT1VJvVOyVI%2BsleR0Xnc1H6RGXsm5M88IKQmUpZRZEbqGWZ6PJplsHcZsoLXuA12cI94EhqO4z0G9g4Aeut2MFCa%2FyEUUknPJ0kYlunDGHZmwwEk7Do8hp2lncb5241WxEs6NSuugy43ILlLemroT%2FCjbEsVkA6bGmjFNxDGUa8tfjAAYOuxFGiVr7op7jKxr6njn9ZJUKtix3pE6J6MjBjbiO4JTAsGbr7nZOffnc0KDbKg%2BkjcHEyaAmWP1h2nPSENibcPE0aLX7ivKqgqvjyK7HZrsNJiTJi1kDtX3Vi5q38aZ4SyH6YzJ0dZjJnDgB0Olw5ID3hbOFfyYMn%2BRlFneaxqIilUjzGkwflEmI4SaAPU3z2YDDLc7CndLP%2Bs4%2BwqBJ83x4yEo7ytrsowklqfRL2jr%2B%2FJVaXMU0b0G0mFjUk77bAHDHQn%2BiUx94yyVCN0v6%2F6GnGhA%2FlNRSC6aMomzjUf4ograp1gVkYpCqH1JNxNvq9vAt1g%2FXB0DSCO1hGu%2BgJ1%2B0VOIQBQ%2Bo%2FQ5NjVTHSzlndjlL98p3uYBB9uQmjh2bUVM22V668HXveS7PI6u%2B73eNxNzDepY3OBjqkATmERASUln%2Fg6xgK9EPTJrJS5UH%2FlmCvBhbDpcofEYTYaG8bcUhpAu8KreUWZ6MdHS%2Fth4PZ3GdbBxgYGTuUIXLtudRQeXzmW8pDe%2FNy1xuHoWLueLATt3TArrw6rN962SJUJcSqumZrL4OlNL0cyaOJil1oDR%2Fkn%2BDivqEY8jpumHD88DqdOVYqaAa0u4Lp79b58ZJr9Okegmh%2FkV6mZ1L7hw7Q&X-Amz-Signature=9e3c92e79a8afa51834ceff41684c6d40743c1faa36f7aa2f7ba59910ea56830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

