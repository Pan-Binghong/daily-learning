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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIJU6LX7%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIBHLduzJdPj0mUME4BkCK388oTyddzoO3KUY8qEmh5F0AiBkUqwd06R1ZgnSvDfj4mm0BS%2By%2FICvKHv3%2FpkWzPbOViqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzGdAHiS0FNOsus%2BNKtwD9Hn5%2Bb300z4J1iwdCPogMjvdkEl0T8o1hQXvKuCTMhsVTdAPcz0iNZQd%2FRwwNKeC%2BDQ3K87VnePxQyW1%2Ff4LZqFM4Am03fC9So6JlhLNjjM24FJjUoYMbinGq%2BvLuzYjJXhJZWqts0lJS87kNVcnYAMRnHnqc99SWQaKrhQ8ENXYCMJ%2BS6f6qYrV4yRLPQpPT4qi3ONWT1c%2BkwJsjsZiX3FveTUkwmXPvkSpaIKYA5xt3WM69EeEhBSMylVdJvwLlD7K%2BRMVa2sDLo9sbw5Ws%2FLTNNu8sMhVurJKoW%2B5svzgrFH6q4UIeH%2FRhEJc2sZuP2lXnpw7ZDnhOcPxn5nIH49HkM4TzXSXAYfbqBdmHDvEWoSuVsFnW%2BQBb8OosrDGAKK2Zjr4WG%2B%2F8dyqXWn73NDV2T3FY60sCmCuG6MomrwtZaKZDAYYekPcXpznA7BM%2F0esX%2B5G67xY7aWRWEhYcB1KkDaJoqEJl6gy7XlM2YdE%2BhWyvLgImXlGBSYJhpDQvaC72KoqmkQ4c%2FYt3T8bxLBq2yQw%2FGtUdTI%2Fr8tx%2Frbu0Sg7ZSXkfOXS%2BY1gty49cfYwA7oUj%2FiP8AVrzYoOivupSNthUSaev6PfXPZzFZ5PUvysJflGerGAPzEw2pLGzwY6pgEQIPQxYA1GC%2FSYExhH2U0sL%2BZcZ8AZ6cTswv2oRnJgQjs1gU8d%2BP45lmda8AOPnXX51V0PaKXzlnyyf1o%2F2SO6JHBzMHSuV10%2F9F8IF3WHB%2BuSUvjBwbDt9TvmLCDZwoaNlAAxDmLsl4ckLULqGVMfCSJf%2F%2BL5Dw8Q2shBL2tpSGFr4CjJ3LyUT5kk5ewuE%2BL98hiU58Kij4HDDjjq0EcUvX07CMnO&X-Amz-Signature=abbae5b9733c038c8c3927422990d85425b0533494a65f2e28dafecc3204d819&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIJU6LX7%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIBHLduzJdPj0mUME4BkCK388oTyddzoO3KUY8qEmh5F0AiBkUqwd06R1ZgnSvDfj4mm0BS%2By%2FICvKHv3%2FpkWzPbOViqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzGdAHiS0FNOsus%2BNKtwD9Hn5%2Bb300z4J1iwdCPogMjvdkEl0T8o1hQXvKuCTMhsVTdAPcz0iNZQd%2FRwwNKeC%2BDQ3K87VnePxQyW1%2Ff4LZqFM4Am03fC9So6JlhLNjjM24FJjUoYMbinGq%2BvLuzYjJXhJZWqts0lJS87kNVcnYAMRnHnqc99SWQaKrhQ8ENXYCMJ%2BS6f6qYrV4yRLPQpPT4qi3ONWT1c%2BkwJsjsZiX3FveTUkwmXPvkSpaIKYA5xt3WM69EeEhBSMylVdJvwLlD7K%2BRMVa2sDLo9sbw5Ws%2FLTNNu8sMhVurJKoW%2B5svzgrFH6q4UIeH%2FRhEJc2sZuP2lXnpw7ZDnhOcPxn5nIH49HkM4TzXSXAYfbqBdmHDvEWoSuVsFnW%2BQBb8OosrDGAKK2Zjr4WG%2B%2F8dyqXWn73NDV2T3FY60sCmCuG6MomrwtZaKZDAYYekPcXpznA7BM%2F0esX%2B5G67xY7aWRWEhYcB1KkDaJoqEJl6gy7XlM2YdE%2BhWyvLgImXlGBSYJhpDQvaC72KoqmkQ4c%2FYt3T8bxLBq2yQw%2FGtUdTI%2Fr8tx%2Frbu0Sg7ZSXkfOXS%2BY1gty49cfYwA7oUj%2FiP8AVrzYoOivupSNthUSaev6PfXPZzFZ5PUvysJflGerGAPzEw2pLGzwY6pgEQIPQxYA1GC%2FSYExhH2U0sL%2BZcZ8AZ6cTswv2oRnJgQjs1gU8d%2BP45lmda8AOPnXX51V0PaKXzlnyyf1o%2F2SO6JHBzMHSuV10%2F9F8IF3WHB%2BuSUvjBwbDt9TvmLCDZwoaNlAAxDmLsl4ckLULqGVMfCSJf%2F%2BL5Dw8Q2shBL2tpSGFr4CjJ3LyUT5kk5ewuE%2BL98hiU58Kij4HDDjjq0EcUvX07CMnO&X-Amz-Signature=2366350607829be2ad941613133dd196d68e3f1767664cc75e1277cbbd8b8da4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

