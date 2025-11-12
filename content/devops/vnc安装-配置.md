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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7OS5SVG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCR0RhZ2sugBzc%2FvZR%2B%2FcWTDRmhlIMiw%2FwF8DGqFVl6GQIhAJbdKJSUtLK6wM%2B04l9IP%2BQk6PcrwuZ9F%2FpqdBDrLDgDKv8DCCwQABoMNjM3NDIzMTgzODA1IgxgD2OiCmKIkzYJVvgq3APJURXKolEFPrGU3TAaIwx4jRT%2Bk94tKnuZZ9JYaBzsJQ7oF8OLCx79Er0FpKjVzJ8Hl7ZUzREam2TgrGsIPuUbbph0QKKVMNbyTGADFSE71DSnOIG0v9bPVm5gXl0s8E9OIfg1YLNFzujWUhfLKOH7C%2B8y7ihQ%2FVVl1D7upTBFx6AjapYlZGZ6ydldz6ELuO7nVHFEdiSqfrrW0GtdNRNWv19EyHq8jW%2FuNESFTO8jylTkj0ptCOzswW6S5Q0bk3mLcfxgDSx%2FXW%2Fwhxwjgtb5uRBm7fsySQJezYFIw069l8rH1qgw07UjyiU1HqO24k8dq4oamriqzd9FlRh%2FBhaXUqwgsj6c%2Bx061y2MDSp%2BBfDGvji6C8nA3PmlLBxfHR1%2BQduWZA4AzOE%2BhUTQgu7wP%2BowXxpxG97h2PceDlzpQlRjY0SZab49nWaY3y057anQIU6H2hLLnSPtNCe8CITRMEuXlkGb8ht9UPlfwKufoc3viVbapy%2FdiBJSa3t9woCs4RS8nKZ1LU3lcW7IdO511SMIi1NirB6x5zd%2Bk%2FLPEFYckqsHD0CpWdDVdNwKGw2AxtDRfm0N%2FZ4uEZxFtlP6y58X5sUqirIFqsXaDUg3hpJQ4Uxmdb0V%2F1%2FjmzCr48%2FIBjqkAbVBc0%2FWXX50kgeH5AQ8P9WD7cimreGxv8YEmHZ%2FtMdDu7NaKp3LPUSy5QqRnSHarsPs1w9NmfBfPA0Hoe8finuqZE232CjlMYlwyXOfmiq7Z4oPzb5hK6ULa6wCMU%2BA%2BrdSqQZpU23TTKsoRL2CQ2MpCqrLL3d27vGcJYwI3EwTS2TH7WTqF%2BALCjOB78H4Bi6lWALI%2BcKg%2BznFOytNR4V82ot2&X-Amz-Signature=d70ee7b0d90d4f0dc776a2096171996f4be6c6dcd1f8b0db07365656e8552370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7OS5SVG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCR0RhZ2sugBzc%2FvZR%2B%2FcWTDRmhlIMiw%2FwF8DGqFVl6GQIhAJbdKJSUtLK6wM%2B04l9IP%2BQk6PcrwuZ9F%2FpqdBDrLDgDKv8DCCwQABoMNjM3NDIzMTgzODA1IgxgD2OiCmKIkzYJVvgq3APJURXKolEFPrGU3TAaIwx4jRT%2Bk94tKnuZZ9JYaBzsJQ7oF8OLCx79Er0FpKjVzJ8Hl7ZUzREam2TgrGsIPuUbbph0QKKVMNbyTGADFSE71DSnOIG0v9bPVm5gXl0s8E9OIfg1YLNFzujWUhfLKOH7C%2B8y7ihQ%2FVVl1D7upTBFx6AjapYlZGZ6ydldz6ELuO7nVHFEdiSqfrrW0GtdNRNWv19EyHq8jW%2FuNESFTO8jylTkj0ptCOzswW6S5Q0bk3mLcfxgDSx%2FXW%2Fwhxwjgtb5uRBm7fsySQJezYFIw069l8rH1qgw07UjyiU1HqO24k8dq4oamriqzd9FlRh%2FBhaXUqwgsj6c%2Bx061y2MDSp%2BBfDGvji6C8nA3PmlLBxfHR1%2BQduWZA4AzOE%2BhUTQgu7wP%2BowXxpxG97h2PceDlzpQlRjY0SZab49nWaY3y057anQIU6H2hLLnSPtNCe8CITRMEuXlkGb8ht9UPlfwKufoc3viVbapy%2FdiBJSa3t9woCs4RS8nKZ1LU3lcW7IdO511SMIi1NirB6x5zd%2Bk%2FLPEFYckqsHD0CpWdDVdNwKGw2AxtDRfm0N%2FZ4uEZxFtlP6y58X5sUqirIFqsXaDUg3hpJQ4Uxmdb0V%2F1%2FjmzCr48%2FIBjqkAbVBc0%2FWXX50kgeH5AQ8P9WD7cimreGxv8YEmHZ%2FtMdDu7NaKp3LPUSy5QqRnSHarsPs1w9NmfBfPA0Hoe8finuqZE232CjlMYlwyXOfmiq7Z4oPzb5hK6ULa6wCMU%2BA%2BrdSqQZpU23TTKsoRL2CQ2MpCqrLL3d27vGcJYwI3EwTS2TH7WTqF%2BALCjOB78H4Bi6lWALI%2BcKg%2BznFOytNR4V82ot2&X-Amz-Signature=8282ce374dacc17ee2adf1a2afb4d0435da118a2a2b1598537d08537f8b85ce3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

