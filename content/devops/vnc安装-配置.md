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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XKFEA4L%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDO7AzOQcCemGLOWTzMxIrtaUlt5FojjmIt8GHw5dgRAAiEA4WIOxNcJfw0SteUs4Z%2BIdi%2FTktok%2B%2FzK7ipDAzm5ic8qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYy%2FJBSAO9ziH%2FYXyrcAx3jz2S5gDztZ%2BSDCCw1%2F4lsNaJI5GdGFwb0MWrg2k2nP8uECXt7ZclXue%2ByCvUQikqaUR%2Bv6O%2Bn5882zeiZ6GuCuiI0Vq7aBMpUX2w3NhD9rqYk%2BXFlze32wab%2FyK5By4Iz33JUOoOAV3TWt4q8Vvv9CiP1QWuI452YVVQA2ARwIZ7BY1zbL6cVZDVXX9xrABHuN7lNG%2BxQVfERVqi8jFAb0ov7lVcGfNo42IO5lNsasIbpuyRXq9aEOJ18aVc3K0N5unFgiinvK6plDGBR9G1Lt13paSaB%2FHAz1Yjy4OcfPZIZ5yAkAv%2F2poERNCzGb5DIrufNXwLqIGFt3GScNxQBMmkDFUaJVtMxCWuthThCdHVFf2Zvdh95AN3C%2FvgGj7PTtT9wkKd6lzpbbQ4yLYdxHr1vM1bMARZNYruCpW6eWjdhhxc6x3Z6AgV1NifWZ6gwLNi0%2B25a7XxKEvK%2Fc2bt2YRFqu1fzYB2AktCQ3YU5npE4AP5wjZgamLHT7mcc%2BoW9kwEN2H%2FiHW9ZjK3iq6XQ1oQ%2FUziR902wDNsC%2BEdnnUrtOuhYzNhXCRIMiROoQxfGLn80q91wS%2FE9vkAZT7Yq3taUsPvuZR9vAkQEFmlOuBmPYgSdvypCrHmMLSL184GOqUBQXBsohW8k9EN0oiKjvDrz5DWJKnAmVpxOFjHhJNLdXVV2Q3cRq7bn0YMWaTFLEFVzUt4wf1kpKAQSJ54VmIjxV9HcJ6w6G2%2BDRb1Vkm8wfLvO5mVdIQBbWPbgFH8yAhQj4h%2FJViGATxQhA0mVJd4dDfEO2uSrXEixDU3hlUdCLzkRpf9UiswTKLf0LdLGnBlK8qwaEQmOTDbxXaqlmMZAzQUyHt1&X-Amz-Signature=697d51abc67293d01b91b596d67df236e5e8eb665b90fbf31661f582610171a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XKFEA4L%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIDO7AzOQcCemGLOWTzMxIrtaUlt5FojjmIt8GHw5dgRAAiEA4WIOxNcJfw0SteUs4Z%2BIdi%2FTktok%2B%2FzK7ipDAzm5ic8qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYy%2FJBSAO9ziH%2FYXyrcAx3jz2S5gDztZ%2BSDCCw1%2F4lsNaJI5GdGFwb0MWrg2k2nP8uECXt7ZclXue%2ByCvUQikqaUR%2Bv6O%2Bn5882zeiZ6GuCuiI0Vq7aBMpUX2w3NhD9rqYk%2BXFlze32wab%2FyK5By4Iz33JUOoOAV3TWt4q8Vvv9CiP1QWuI452YVVQA2ARwIZ7BY1zbL6cVZDVXX9xrABHuN7lNG%2BxQVfERVqi8jFAb0ov7lVcGfNo42IO5lNsasIbpuyRXq9aEOJ18aVc3K0N5unFgiinvK6plDGBR9G1Lt13paSaB%2FHAz1Yjy4OcfPZIZ5yAkAv%2F2poERNCzGb5DIrufNXwLqIGFt3GScNxQBMmkDFUaJVtMxCWuthThCdHVFf2Zvdh95AN3C%2FvgGj7PTtT9wkKd6lzpbbQ4yLYdxHr1vM1bMARZNYruCpW6eWjdhhxc6x3Z6AgV1NifWZ6gwLNi0%2B25a7XxKEvK%2Fc2bt2YRFqu1fzYB2AktCQ3YU5npE4AP5wjZgamLHT7mcc%2BoW9kwEN2H%2FiHW9ZjK3iq6XQ1oQ%2FUziR902wDNsC%2BEdnnUrtOuhYzNhXCRIMiROoQxfGLn80q91wS%2FE9vkAZT7Yq3taUsPvuZR9vAkQEFmlOuBmPYgSdvypCrHmMLSL184GOqUBQXBsohW8k9EN0oiKjvDrz5DWJKnAmVpxOFjHhJNLdXVV2Q3cRq7bn0YMWaTFLEFVzUt4wf1kpKAQSJ54VmIjxV9HcJ6w6G2%2BDRb1Vkm8wfLvO5mVdIQBbWPbgFH8yAhQj4h%2FJViGATxQhA0mVJd4dDfEO2uSrXEixDU3hlUdCLzkRpf9UiswTKLf0LdLGnBlK8qwaEQmOTDbxXaqlmMZAzQUyHt1&X-Amz-Signature=d498a3ff18a9fb091e5ed079bcd924adbf739e7d0cd2e14749167416627cec8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

