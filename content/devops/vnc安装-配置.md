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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMKY335I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHF6BkhnEB6LN0CNT6KlviP%2FYepqHFf9FTb82H2FeaLUAiABZFuk9A5qJYUfDOuVs%2BL7CAiqyiEDP4JBlMlrbW1w8iqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVnz0dPrCtx2kcuVPKtwDWD8P43RzmQdpcx5pAHhy8GhQA6ScUX%2B%2FYPZmK4HbIiXroCt0f3YWnzTG55uPDRFScTncfj8PNmHKaaRNxJ4XwepRi4fBFoJnjEmDtQ7OhPqBkaMNFetPGt%2Fe6Jf6CJBUrsWH%2F7TqlueLVR4oAcubcIt4Eii4XZLUeFgX09Tcqcv4fknMrqBwodbj4Gl7JvJkBSBj4%2Fljam7vYv7lYe4kHdjgJuf9q8JakvKnG%2BT42zKozemHKPD9PWIOOPV44JiSU%2B74KGhcc3m4LhiJBRxewDpF8iorFb%2FmbtgiQVmqSa15AvfqUUmI0C8EltGZNFQGmniTz5l5nwi%2FMo5Bj6zx%2F4I%2BVYSdZlhcU8m2MeOjigeCdC5zpw79nQV9L4iGp5LJHJVGGffTCqluBF3Yh7opEE8vT5Hzu982PTqjMT4KOdkOI0jbGqFuiTPeOgXIjdQeaROSjANnhPxNpI4KdCZ%2Fa1n5m2oPXOwNGomlnfBIDbr5hrlqwO2U8Ajr9acWTNKKvEekCgdm3bMCX5rFXaE5echvA%2FZXxcyZNSielOJOQM9idz0Pr%2BGSaoJ0tWRl7TR33GM856wfZcUlux5YCYvxykrAPR6FMJ17PTIZBB0SDjUNmaANh65CvpChNTww7PGvyAY6pgH5WEUK3wOdKVbrOXFmb9OJITH97fCWkTEzX65Tqylyhp1lAb4zRjsqiZpBgacKVYBUeEt8onUxg9vcozDri%2FqOtl57Nb6OYpOcD32nNy5az7p3LCyNqWqdyK1yCgSSwJ4ABAbbC5LVsaJKypgJRy9nAbX51Y9ihXoEM5UdbX5Eh0qKru%2BUwa1HMz9CZz2YL0RncFwHqdfIHOS47DvXQhAH87zyf793&X-Amz-Signature=1f131607e85d1dba97561b30bf1616c40ca75a0f15cbfd16bdd2d75d81549bc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMKY335I%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHF6BkhnEB6LN0CNT6KlviP%2FYepqHFf9FTb82H2FeaLUAiABZFuk9A5qJYUfDOuVs%2BL7CAiqyiEDP4JBlMlrbW1w8iqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVnz0dPrCtx2kcuVPKtwDWD8P43RzmQdpcx5pAHhy8GhQA6ScUX%2B%2FYPZmK4HbIiXroCt0f3YWnzTG55uPDRFScTncfj8PNmHKaaRNxJ4XwepRi4fBFoJnjEmDtQ7OhPqBkaMNFetPGt%2Fe6Jf6CJBUrsWH%2F7TqlueLVR4oAcubcIt4Eii4XZLUeFgX09Tcqcv4fknMrqBwodbj4Gl7JvJkBSBj4%2Fljam7vYv7lYe4kHdjgJuf9q8JakvKnG%2BT42zKozemHKPD9PWIOOPV44JiSU%2B74KGhcc3m4LhiJBRxewDpF8iorFb%2FmbtgiQVmqSa15AvfqUUmI0C8EltGZNFQGmniTz5l5nwi%2FMo5Bj6zx%2F4I%2BVYSdZlhcU8m2MeOjigeCdC5zpw79nQV9L4iGp5LJHJVGGffTCqluBF3Yh7opEE8vT5Hzu982PTqjMT4KOdkOI0jbGqFuiTPeOgXIjdQeaROSjANnhPxNpI4KdCZ%2Fa1n5m2oPXOwNGomlnfBIDbr5hrlqwO2U8Ajr9acWTNKKvEekCgdm3bMCX5rFXaE5echvA%2FZXxcyZNSielOJOQM9idz0Pr%2BGSaoJ0tWRl7TR33GM856wfZcUlux5YCYvxykrAPR6FMJ17PTIZBB0SDjUNmaANh65CvpChNTww7PGvyAY6pgH5WEUK3wOdKVbrOXFmb9OJITH97fCWkTEzX65Tqylyhp1lAb4zRjsqiZpBgacKVYBUeEt8onUxg9vcozDri%2FqOtl57Nb6OYpOcD32nNy5az7p3LCyNqWqdyK1yCgSSwJ4ABAbbC5LVsaJKypgJRy9nAbX51Y9ihXoEM5UdbX5Eh0qKru%2BUwa1HMz9CZz2YL0RncFwHqdfIHOS47DvXQhAH87zyf793&X-Amz-Signature=147f340ee73794acadbaf10addc984cf29afa4dd7db6de7651d924538b6627f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

