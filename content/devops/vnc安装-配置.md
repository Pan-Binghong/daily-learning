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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKSIMRL%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrbjgzVR1DMJm%2FlDKyoGJHjrVIKxkWe9vVHY5EMUgY5QIhAMO5udOUh0yrIXJzZ99OvmOPc%2Beymwp5dG10aMPLN8VvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxyta7DdJrBHLH0QnMq3AP5IKXlujhWHWKWzaFL5h49aog5SGjpnlfj4GkDda4XBxL2xvPBqK3YeEAqqm9xmUmwwRqSSwc27YlR%2FS%2B%2BJE4y3JT4wgU%2B5LwKbJr3m%2BN2Q91nHcIgorn7bkQKeFQDkW4H7opNchy9k2OcJboR97jBwuGgkb0fF6BpPyPG3Ue%2BlKRYfJGvl8CYfCmNvvfc%2FsG2eBUGzjeopEi6Y%2FgqOHDmBUGTfkB272hsJGHudQLtuwF8l%2FDKIHsRIgbW4ENLAadh%2BbQjSdwW8nPwYtteD5eRZdUP2QNSDzCyml1xDo5hrHgWxQ0bBJKXwKUl96kCtDUayyVDZlk1F%2FMJdvQ3a7KSJxg8j18466OwmpUzKTu%2BUVpzRKnG%2FJHSsU2piGKFDk8vs%2FMH4S91pSmx0K2irwGG25ZAJysPkgECdODAZwZoaRYQyfKMKJPhnv%2B%2FRUecgtDVc26ZeQvlMOMy8e%2FvFeTQGgsTt3Y0YACDU9JvXbVNMmzFIrfcZPKcKhOXZyscSQVFTys7TX9dxY5aSCp3A0nlaCLkyhe3f%2FtOIp8tXs7Hny9C3ZWKGhyKDnup69rQ8dCGD%2F9Mt8eIiPvyRM782LpQm2ydR1sawdlWy4Q4cR5dOYr43tpmMOB2x%2FxWOjCJ2MDLBjqkASOo4zz17p0xx32tzRTxQ6vaCNuZ%2BNgkiJ%2BlBe7CIP9qAl0URmgriG6RO14TpzD2anRTO4x2n83d1MIyh%2BYGX0jQM8MLPxGETDYn4al6UGxKzJ0uCj4YDoXK0x3o8XvysMTHab9uZfmWtR%2FtYPqa83qotIAzI0IhawVO8PHs2mOe43EyGlPIGU91a2dhmUZ%2BPuLAz6QwEKFDKk2GJ%2Bthwb8W64j%2F&X-Amz-Signature=553285fc5cd6556b35465b7a75c47633535afe1d467cf612139cf9b83cef4825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJKSIMRL%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrbjgzVR1DMJm%2FlDKyoGJHjrVIKxkWe9vVHY5EMUgY5QIhAMO5udOUh0yrIXJzZ99OvmOPc%2Beymwp5dG10aMPLN8VvKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxyta7DdJrBHLH0QnMq3AP5IKXlujhWHWKWzaFL5h49aog5SGjpnlfj4GkDda4XBxL2xvPBqK3YeEAqqm9xmUmwwRqSSwc27YlR%2FS%2B%2BJE4y3JT4wgU%2B5LwKbJr3m%2BN2Q91nHcIgorn7bkQKeFQDkW4H7opNchy9k2OcJboR97jBwuGgkb0fF6BpPyPG3Ue%2BlKRYfJGvl8CYfCmNvvfc%2FsG2eBUGzjeopEi6Y%2FgqOHDmBUGTfkB272hsJGHudQLtuwF8l%2FDKIHsRIgbW4ENLAadh%2BbQjSdwW8nPwYtteD5eRZdUP2QNSDzCyml1xDo5hrHgWxQ0bBJKXwKUl96kCtDUayyVDZlk1F%2FMJdvQ3a7KSJxg8j18466OwmpUzKTu%2BUVpzRKnG%2FJHSsU2piGKFDk8vs%2FMH4S91pSmx0K2irwGG25ZAJysPkgECdODAZwZoaRYQyfKMKJPhnv%2B%2FRUecgtDVc26ZeQvlMOMy8e%2FvFeTQGgsTt3Y0YACDU9JvXbVNMmzFIrfcZPKcKhOXZyscSQVFTys7TX9dxY5aSCp3A0nlaCLkyhe3f%2FtOIp8tXs7Hny9C3ZWKGhyKDnup69rQ8dCGD%2F9Mt8eIiPvyRM782LpQm2ydR1sawdlWy4Q4cR5dOYr43tpmMOB2x%2FxWOjCJ2MDLBjqkASOo4zz17p0xx32tzRTxQ6vaCNuZ%2BNgkiJ%2BlBe7CIP9qAl0URmgriG6RO14TpzD2anRTO4x2n83d1MIyh%2BYGX0jQM8MLPxGETDYn4al6UGxKzJ0uCj4YDoXK0x3o8XvysMTHab9uZfmWtR%2FtYPqa83qotIAzI0IhawVO8PHs2mOe43EyGlPIGU91a2dhmUZ%2BPuLAz6QwEKFDKk2GJ%2Bthwb8W64j%2F&X-Amz-Signature=5617c428daab8e8f8b30a729757f962297e9a42d938118d1551ab1e95744275c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

