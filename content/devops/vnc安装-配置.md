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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674TYUG5F%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX7ROBh4xyqIclcR2uHclzcINYSBz2UBlrl1gU%2BH%2F3pgIgPXdfrjM6iECtl4%2FKOgXulQ5YhElY7TTKOi8w9oW9T7YqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAjKTaWL1jqvp16IwCrcAxOYYHbHy7PkaRWnEH9Th%2BPKKK8kO7JTORiDkFEXtrfnjMwlwAHYoL4fk%2FzJrIAvjz%2B4GD4tD70yYlhBITMzXZRB25WKZdbRjneWxXxq4zBUItIFnzAUbR2LTVTSnxuqN2BG0%2FxYHTS4uM5PPN6jUgGFxcFMcXXZdmAvPSYtcL2qXuXJxRTTSJ2QvCioIEwoFimPnu84RdXaRklS01q%2FW5srE3UNZ8ZlxCrMEZdGW%2BlwCSLvrTnawp2FIgSzF9n8w547K8elUovdTt%2FjukTBsPwcq2BwJwj5TTPoz0poP56Rsq94nthRCHanhyPI2jzZkfSjTvRJqD8Q5lNnDwURYqyHMpSO8lA21TO5SB%2F4oHxX59DTgfk66GR0iiVSlOkoukWpaHw7HUI8kq4j2p5XuMkD%2BCKMzMKzR2zMvhXyQPS1TXwamwkkjbkx5dIuvEJmbIGYcYiyH4V5%2FC4QEy2xDtV9xLletHRXPVbJXbaTfWSQJFNL8Kx6xik1%2BsJwEJRIvGFev%2FQzk43bLEwchNelSRTX%2F2FXmRTd20bKv7HxEgg0PXl9wkWyJDq28VKSBHsf4WQyWjpACDBjf6Cte%2Fb8xIJbw1BYxDMF74ZqVceG%2BD%2FoWPYwnvb1aFzZ8yaDMNS1mM0GOqUBJePRoJs%2FfnAnG5996KcWn4%2FHr6tXXqToyqn%2BbxQsvXbe2IHIuXoOEv7eXXtkC2qG5SNJZBMMh1pZc6CynyenjQT65c9NUlW5lIgWqX6f%2BS4%2BYeE35SjpGmu5ahucgyOA1GKEWqf5LENnyq1NNAJ%2FsZyO8BzW5LNl%2FrJ463u8Nsk%2BLHisjW%2Bz%2FxgCfqDzOVJUuBpUtZAvDTi%2FcPLC4C4quGVdPk8j&X-Amz-Signature=17a4780937dbc911fbdc218475855e210adfb928915c385cd99005b06a89901f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674TYUG5F%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDX7ROBh4xyqIclcR2uHclzcINYSBz2UBlrl1gU%2BH%2F3pgIgPXdfrjM6iECtl4%2FKOgXulQ5YhElY7TTKOi8w9oW9T7YqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAjKTaWL1jqvp16IwCrcAxOYYHbHy7PkaRWnEH9Th%2BPKKK8kO7JTORiDkFEXtrfnjMwlwAHYoL4fk%2FzJrIAvjz%2B4GD4tD70yYlhBITMzXZRB25WKZdbRjneWxXxq4zBUItIFnzAUbR2LTVTSnxuqN2BG0%2FxYHTS4uM5PPN6jUgGFxcFMcXXZdmAvPSYtcL2qXuXJxRTTSJ2QvCioIEwoFimPnu84RdXaRklS01q%2FW5srE3UNZ8ZlxCrMEZdGW%2BlwCSLvrTnawp2FIgSzF9n8w547K8elUovdTt%2FjukTBsPwcq2BwJwj5TTPoz0poP56Rsq94nthRCHanhyPI2jzZkfSjTvRJqD8Q5lNnDwURYqyHMpSO8lA21TO5SB%2F4oHxX59DTgfk66GR0iiVSlOkoukWpaHw7HUI8kq4j2p5XuMkD%2BCKMzMKzR2zMvhXyQPS1TXwamwkkjbkx5dIuvEJmbIGYcYiyH4V5%2FC4QEy2xDtV9xLletHRXPVbJXbaTfWSQJFNL8Kx6xik1%2BsJwEJRIvGFev%2FQzk43bLEwchNelSRTX%2F2FXmRTd20bKv7HxEgg0PXl9wkWyJDq28VKSBHsf4WQyWjpACDBjf6Cte%2Fb8xIJbw1BYxDMF74ZqVceG%2BD%2FoWPYwnvb1aFzZ8yaDMNS1mM0GOqUBJePRoJs%2FfnAnG5996KcWn4%2FHr6tXXqToyqn%2BbxQsvXbe2IHIuXoOEv7eXXtkC2qG5SNJZBMMh1pZc6CynyenjQT65c9NUlW5lIgWqX6f%2BS4%2BYeE35SjpGmu5ahucgyOA1GKEWqf5LENnyq1NNAJ%2FsZyO8BzW5LNl%2FrJ463u8Nsk%2BLHisjW%2Bz%2FxgCfqDzOVJUuBpUtZAvDTi%2FcPLC4C4quGVdPk8j&X-Amz-Signature=903345f12f03307f475431020d648bc82fe3d40c9e25f9422604e42410285bd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

