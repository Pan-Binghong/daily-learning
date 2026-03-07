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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW6YQYBI%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCDI8Rk0uvKH60vqTQ%2Fqdv6xXIRpEDLZaYCdSqVQNxM7wIhAOHDjxxjrqrT6v1W9IbTVIijG%2Fwe5xn2uZh%2BEoCq8m0EKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymJbfW0XM3EspdgeQq3APi%2BNhS0wPNzyyvlOKespFSNAS9M8W8xZqDvWAQy7I5hZijnP5WbQ87lCo%2BQZzW%2BOk2n4bK1xlSRAlsXBXnco9TFUzPbT0GsEYyDZoG04ljjOmd9%2BVYmdkr41HkYGiBQJNTNDl1c76Uvr7Bdkj4s6A8jQsO0m%2F6HMsdpNXZesd5HZt%2BIcsXvLYACW8vcojzVIESqOSU6XCUoHd7pUBzYdNxawG9EzirNgfhItQKEsQSYLzo4xfVxn%2Fz9%2Fv1LwJhS5gf4uu675pUsvyMCFpMCMB3ci2bzMRFXdCb1ff0JCYMNtuPqeLtNEJv3aSxUDLOd%2FrAMIJvTGvHA3ksIjpXZ2Ydqkuw8kEIpsYFKBXOqmvE5YtJqD5qoNsxUd8yt3GUvFBtjgbVvsr8usZaOnKhFK9904Z34bJRsZvyy5pSDaFjUdIbiok7WWlNpFSUVgFmuDUqE2kyiS56p7NCwQ6FRY8Z%2Bkx3RK3Pc1At27xTxZ%2BWfmN6IHNWB%2FPwrceH3Y6IWzRWkFYODNNxDqNBHtYoF%2BE4DByr%2FT%2BVeZJ0jCBzDaNO3m1uP%2FG8rPv6JaQWjYIAi5pp9D3OUt1hej9eybtyE3xxsQPZpdchB%2F2ZMDgCSZnus1caRH7amtDV4LV5vzDxlK7NBjqkAcHguoG%2BZTZ75%2F3NncudWfCPqEoZ2%2BShsqT%2F8fggC7fyjjJqMvuzBBYq8bYczEzdKMMARQv38l2Hy%2BZS8xZcCHohiZf1WXRTaDTSRIzq5vdjM5PQPuJ1djgjkZ%2FISL24Wl1A9Kbm4uLOQq31s7XmLmwLWQ8tHoT2PuL5vFEG8lB3G%2F6PwgCSuzFYhPFaB5%2FZXue0bALcJlIGkVS9DMFKhbFkiNU5&X-Amz-Signature=80c18edff7e679f428b33a4d6844fe3c41a5c98fa5256e96c145905fdd938ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW6YQYBI%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCDI8Rk0uvKH60vqTQ%2Fqdv6xXIRpEDLZaYCdSqVQNxM7wIhAOHDjxxjrqrT6v1W9IbTVIijG%2Fwe5xn2uZh%2BEoCq8m0EKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgymJbfW0XM3EspdgeQq3APi%2BNhS0wPNzyyvlOKespFSNAS9M8W8xZqDvWAQy7I5hZijnP5WbQ87lCo%2BQZzW%2BOk2n4bK1xlSRAlsXBXnco9TFUzPbT0GsEYyDZoG04ljjOmd9%2BVYmdkr41HkYGiBQJNTNDl1c76Uvr7Bdkj4s6A8jQsO0m%2F6HMsdpNXZesd5HZt%2BIcsXvLYACW8vcojzVIESqOSU6XCUoHd7pUBzYdNxawG9EzirNgfhItQKEsQSYLzo4xfVxn%2Fz9%2Fv1LwJhS5gf4uu675pUsvyMCFpMCMB3ci2bzMRFXdCb1ff0JCYMNtuPqeLtNEJv3aSxUDLOd%2FrAMIJvTGvHA3ksIjpXZ2Ydqkuw8kEIpsYFKBXOqmvE5YtJqD5qoNsxUd8yt3GUvFBtjgbVvsr8usZaOnKhFK9904Z34bJRsZvyy5pSDaFjUdIbiok7WWlNpFSUVgFmuDUqE2kyiS56p7NCwQ6FRY8Z%2Bkx3RK3Pc1At27xTxZ%2BWfmN6IHNWB%2FPwrceH3Y6IWzRWkFYODNNxDqNBHtYoF%2BE4DByr%2FT%2BVeZJ0jCBzDaNO3m1uP%2FG8rPv6JaQWjYIAi5pp9D3OUt1hej9eybtyE3xxsQPZpdchB%2F2ZMDgCSZnus1caRH7amtDV4LV5vzDxlK7NBjqkAcHguoG%2BZTZ75%2F3NncudWfCPqEoZ2%2BShsqT%2F8fggC7fyjjJqMvuzBBYq8bYczEzdKMMARQv38l2Hy%2BZS8xZcCHohiZf1WXRTaDTSRIzq5vdjM5PQPuJ1djgjkZ%2FISL24Wl1A9Kbm4uLOQq31s7XmLmwLWQ8tHoT2PuL5vFEG8lB3G%2F6PwgCSuzFYhPFaB5%2FZXue0bALcJlIGkVS9DMFKhbFkiNU5&X-Amz-Signature=cf432fd7e0e42e86f8648ca5385f2b93bb0f66fe15a7d7c28662fada0e1feab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

