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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDQXTML7%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCeNixwul6HFiQXJxIyQ9eJuS6KmDQ827BgabrZLXeWMgIhALKdM6qH8ztX5nmb7eBnYyVvlsb%2BZqwd0z%2FppKnzF%2BNmKv8DCCIQABoMNjM3NDIzMTgzODA1IgxCU6Atp2uC6qgGtyEq3ANVRIhYW74TzPN4KpIy9706EdOMVwFaEuFc9s3l36KY1bZMX8uQDGzH27hEdpWDa29nXKo1Wvp7%2Fj2KQEpuYw7UJeHW6csbO%2Fz9e6GrZU1d%2BiS66S%2FA8LpJ%2FI5P0m3XjpYacmwa%2B%2BVs92gLLXzL158DwWmkEA1YHyIoNxZq0ZK1FQLfLMUL4Gixrhdqb%2BEb3wlf6tqHbK89%2Fu3uyCFvw0l2gy32XkHWaR7p9BNY6TRBsq6seCujacDzVIZHFOM9gORew2gzXFlNUvNCDiMUlsGkwlMQzAl7b3JaXkZ6Uo7kgERQVk4wI%2FGm4g4se1AzbsDbpIpl4Prrmsh%2BQPTkd66VyjbxYRiUpB0swUtz8SDOQiZnJK5a3VJ3Shry8c4wFa7xVGew4g5ajfMc6gf1kAiWKXH4v77ELbJLdTYxwEyg%2FaanGmynx70hDaRE89Gy86wm1qY1m5eSYZXU5l4TrY1vrBtHWnCrNSdYHTxDdGLiHzcOn3Gw%2BU6DH7E9jeQvVEJS56iB%2FuXoIE2hQcM0YZ3YNHM8eDgJeSz%2FQ0A0Be4HmMzH3q8MSTdS7CSa1dnoSi27Xzc%2BoaFdIkTMAc1HUiBFDqUyZWmowA%2BxW%2B7V1V9YYVjuYTVvCTyMVzudcjDFlL7JBjqkAYrnynWJPvtyyoiCLsUwomDrZRliGBSSuMAuZu85RptUB46jJQDtKho4XmAeWTTst1iR4YBOQ0JdjharQ3iMU7UVyD71zdy%2FKnuW2494iZC2mHpFu0R%2BqwgqvLzROsure4a1GaBhVGVR%2Fwg1uTk%2BTvCNykRUCSu0v8FOLN4WCa%2Bo2eADBgzov09W1ZpKWMy3lm4CMXEkXMdW%2By7%2BtfsceD6EI04H&X-Amz-Signature=332b873ce6472acd4bb9f25f44dffa2e37b48a127a26c82795f5704a54e20c1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDQXTML7%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCeNixwul6HFiQXJxIyQ9eJuS6KmDQ827BgabrZLXeWMgIhALKdM6qH8ztX5nmb7eBnYyVvlsb%2BZqwd0z%2FppKnzF%2BNmKv8DCCIQABoMNjM3NDIzMTgzODA1IgxCU6Atp2uC6qgGtyEq3ANVRIhYW74TzPN4KpIy9706EdOMVwFaEuFc9s3l36KY1bZMX8uQDGzH27hEdpWDa29nXKo1Wvp7%2Fj2KQEpuYw7UJeHW6csbO%2Fz9e6GrZU1d%2BiS66S%2FA8LpJ%2FI5P0m3XjpYacmwa%2B%2BVs92gLLXzL158DwWmkEA1YHyIoNxZq0ZK1FQLfLMUL4Gixrhdqb%2BEb3wlf6tqHbK89%2Fu3uyCFvw0l2gy32XkHWaR7p9BNY6TRBsq6seCujacDzVIZHFOM9gORew2gzXFlNUvNCDiMUlsGkwlMQzAl7b3JaXkZ6Uo7kgERQVk4wI%2FGm4g4se1AzbsDbpIpl4Prrmsh%2BQPTkd66VyjbxYRiUpB0swUtz8SDOQiZnJK5a3VJ3Shry8c4wFa7xVGew4g5ajfMc6gf1kAiWKXH4v77ELbJLdTYxwEyg%2FaanGmynx70hDaRE89Gy86wm1qY1m5eSYZXU5l4TrY1vrBtHWnCrNSdYHTxDdGLiHzcOn3Gw%2BU6DH7E9jeQvVEJS56iB%2FuXoIE2hQcM0YZ3YNHM8eDgJeSz%2FQ0A0Be4HmMzH3q8MSTdS7CSa1dnoSi27Xzc%2BoaFdIkTMAc1HUiBFDqUyZWmowA%2BxW%2B7V1V9YYVjuYTVvCTyMVzudcjDFlL7JBjqkAYrnynWJPvtyyoiCLsUwomDrZRliGBSSuMAuZu85RptUB46jJQDtKho4XmAeWTTst1iR4YBOQ0JdjharQ3iMU7UVyD71zdy%2FKnuW2494iZC2mHpFu0R%2BqwgqvLzROsure4a1GaBhVGVR%2Fwg1uTk%2BTvCNykRUCSu0v8FOLN4WCa%2Bo2eADBgzov09W1ZpKWMy3lm4CMXEkXMdW%2By7%2BtfsceD6EI04H&X-Amz-Signature=263d5fe8261c5b2a66f7a2c407cd558007ee5bc6d68fde166bc837ad0ddf2d72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

