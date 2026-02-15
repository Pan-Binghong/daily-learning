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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RPH4POO%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDeoJWwx0%2FC%2BeuuVf4ILiQf5pznQTZOACjVOIQX60aAegIgQOvVz0%2BfBZYX9sedLEaUyvUext6v8tkmuz0EgfG5D9Mq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDN%2FY3aGSvs%2BWNFaTbSrcA8QV39fspFrg6Gst%2BVuyqu%2FayqVxh4vY1hjjOZhgtsAufMzc5gH%2Fx4KZPf3YDGdkwdIMdZEToaax0qN1ut96SRtI3Ni1d9lSTt9BCOoDIHSwkzD%2Ficz54pb4%2BgOiweACoupEBSTKSnEkOwJLqOZ%2FzzqZ8sqdHMJt69vD5fWU05tPtIx44cH1WwbutHUBpH%2BFIOk6I8e4JMRHn8hejBjjjq0CGWmht6BIB8HTmYBC15UTZztk9T0HXhOlSiLaOSrKRu%2BELRqT2mhkhHdH09vowm3Ys8fHLPyR5R8BLH9QJVSe4ccmttyC9pwdy5gzoKs7HS5HnxFgUkrL5p%2BMWydckVkdjm%2BhXetFhWhALv1rmdoiAuUrFzsMgGiCHwJFRbMKb8zK3Iuixcz1fbfE221VMT7df7uK%2F8lnCPdvGCMyffsI6oMIoql1xoUCnQjw50tShrE6DrhKPpkII6THAxeSoIeHxPZAW9t%2BryT3Kg7MIeSU2MOTTLl5%2FiShtykgmJ7YX7eqp78ZAoIuauiRuX6YSD1OM9XPy3r7zeBcPmClPj106fhNOvfrZBdJdMAizTp%2FUwlaEZZR3J0%2FyDh7ldALq6aQU%2BrS1qLhQf79yiXWfof3c9YKVPtjD64znjDLMJOexMwGOqUBPO8dEVSn%2FMGyNf9bqTlHg1FnTykKklo6xBYAVtdtW812uyE58Cvi%2Bkoim5pI5ur3bDG785VH%2FPE9ZE%2FO0Iv9d2Anl8zc0O541dUyNCa0nwTmvV9ujoHrof9FixZNnJmArHPg9KqY7rAagkuMfj36ha%2Ff3X80VaPGT2xcSUUe5icZ4ukSSlnnM7p09bnYwaSRmumvNIenUMGbTSN4fR8cnnlq9tgv&X-Amz-Signature=4fbf55f5d6494cd4f501447fadf98b97129c523f6dff2cc4192f48b57a213030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RPH4POO%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDeoJWwx0%2FC%2BeuuVf4ILiQf5pznQTZOACjVOIQX60aAegIgQOvVz0%2BfBZYX9sedLEaUyvUext6v8tkmuz0EgfG5D9Mq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDN%2FY3aGSvs%2BWNFaTbSrcA8QV39fspFrg6Gst%2BVuyqu%2FayqVxh4vY1hjjOZhgtsAufMzc5gH%2Fx4KZPf3YDGdkwdIMdZEToaax0qN1ut96SRtI3Ni1d9lSTt9BCOoDIHSwkzD%2Ficz54pb4%2BgOiweACoupEBSTKSnEkOwJLqOZ%2FzzqZ8sqdHMJt69vD5fWU05tPtIx44cH1WwbutHUBpH%2BFIOk6I8e4JMRHn8hejBjjjq0CGWmht6BIB8HTmYBC15UTZztk9T0HXhOlSiLaOSrKRu%2BELRqT2mhkhHdH09vowm3Ys8fHLPyR5R8BLH9QJVSe4ccmttyC9pwdy5gzoKs7HS5HnxFgUkrL5p%2BMWydckVkdjm%2BhXetFhWhALv1rmdoiAuUrFzsMgGiCHwJFRbMKb8zK3Iuixcz1fbfE221VMT7df7uK%2F8lnCPdvGCMyffsI6oMIoql1xoUCnQjw50tShrE6DrhKPpkII6THAxeSoIeHxPZAW9t%2BryT3Kg7MIeSU2MOTTLl5%2FiShtykgmJ7YX7eqp78ZAoIuauiRuX6YSD1OM9XPy3r7zeBcPmClPj106fhNOvfrZBdJdMAizTp%2FUwlaEZZR3J0%2FyDh7ldALq6aQU%2BrS1qLhQf79yiXWfof3c9YKVPtjD64znjDLMJOexMwGOqUBPO8dEVSn%2FMGyNf9bqTlHg1FnTykKklo6xBYAVtdtW812uyE58Cvi%2Bkoim5pI5ur3bDG785VH%2FPE9ZE%2FO0Iv9d2Anl8zc0O541dUyNCa0nwTmvV9ujoHrof9FixZNnJmArHPg9KqY7rAagkuMfj36ha%2Ff3X80VaPGT2xcSUUe5icZ4ukSSlnnM7p09bnYwaSRmumvNIenUMGbTSN4fR8cnnlq9tgv&X-Amz-Signature=22a898489b685dd62ad286b32f820d99895a761fc70a81cc295ba7324b98548f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

