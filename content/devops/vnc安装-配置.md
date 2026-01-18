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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QFRSFRE%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICPDQogfba15%2B9RrcXmdMfkvwWuUoeUP%2BupVnj3v031yAiEA4P%2B8f0cmszv1%2FpV%2FiXaAEcBXJnWdgjFNr5RWp87krRQq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDATyK28ZiOOd0BdZ2yrcAyg7SAAKFM7dRJgIHbfbMRkbiQUy%2F8ncTaQCnloWuJcuXzLreOP4ehicWHe3EQZVsjeSWx3L643eacz4pxMxtX6PtczKpOANjc3Fe62At8t5efviPKswiZ6VZJfZycY1c%2FX1XvK3%2FIAfVPYy9jc4D3OnPVg7mecqjawySs3dSnH9683CygEVAa7uz54UHt1tiP1dM6kQJbj%2BHJ2SuPtOKhd0RyWJAnyOF49C840KIGJgk3Y6HEi31ctj5pPZe2XsoQa8%2FUpiXk0VwRVjMUuTxzykqfnHXzXICvNhDrR4j94uVnpptA0jo9%2F3rxBmcqXR%2BcJ9Gvx5SkfXVUnNu5rvkj8Dxno%2BgT%2BC67N2WG0zUBmB20UHu7hDGcgFaNT9dsYS3zxVTI0FJS6%2BoBHkvsI8Zq17WotiGEJv9M9ZKgh51VOMuV2O6m09p0c0A5CgwGXKe1cgKL%2BXM3FUe8Tw49HkVH6AwDcVK61F6ci1vpGX5%2BH8aemU%2FPtsS2RcgSX1txOWrUF7QFvqDZE1fau1tQ4Sl0rirWMjHAZWciPmgnt9vbY9BcZrwuxKyHghg7fDO%2Bim6kcEAvGiYNZWOpzwkfO2FJnCfLeHbq0NxkzWipv3%2BxWh13tCuW%2FF4IduwcSbMNKBscsGOqUBWHWsvOesEaZzPCkRf0Nxbq6XjJdSFJ3xMa75tWZ1Wm9yNoYo2pgB4si2PkDzamxcc1LH2pLlLSjsQmknAfpvcToXysqDdutP9ZVYQPD8yVPa8BZb%2BFTsTqX%2FvbrHZiQC%2FbYOp4MtjvzaMBSF89fekuLAjU06w%2FBS0n040k20UIqhdKc9CPMCvDIF5DlSnT1d0n%2FeO2BqwDP6YXnsEoRkyANMyKSC&X-Amz-Signature=f162802d416348d6f65c2fe8eee0926df90fcb3c4ef142c95a3fd0720b5d2cab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QFRSFRE%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICPDQogfba15%2B9RrcXmdMfkvwWuUoeUP%2BupVnj3v031yAiEA4P%2B8f0cmszv1%2FpV%2FiXaAEcBXJnWdgjFNr5RWp87krRQq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDATyK28ZiOOd0BdZ2yrcAyg7SAAKFM7dRJgIHbfbMRkbiQUy%2F8ncTaQCnloWuJcuXzLreOP4ehicWHe3EQZVsjeSWx3L643eacz4pxMxtX6PtczKpOANjc3Fe62At8t5efviPKswiZ6VZJfZycY1c%2FX1XvK3%2FIAfVPYy9jc4D3OnPVg7mecqjawySs3dSnH9683CygEVAa7uz54UHt1tiP1dM6kQJbj%2BHJ2SuPtOKhd0RyWJAnyOF49C840KIGJgk3Y6HEi31ctj5pPZe2XsoQa8%2FUpiXk0VwRVjMUuTxzykqfnHXzXICvNhDrR4j94uVnpptA0jo9%2F3rxBmcqXR%2BcJ9Gvx5SkfXVUnNu5rvkj8Dxno%2BgT%2BC67N2WG0zUBmB20UHu7hDGcgFaNT9dsYS3zxVTI0FJS6%2BoBHkvsI8Zq17WotiGEJv9M9ZKgh51VOMuV2O6m09p0c0A5CgwGXKe1cgKL%2BXM3FUe8Tw49HkVH6AwDcVK61F6ci1vpGX5%2BH8aemU%2FPtsS2RcgSX1txOWrUF7QFvqDZE1fau1tQ4Sl0rirWMjHAZWciPmgnt9vbY9BcZrwuxKyHghg7fDO%2Bim6kcEAvGiYNZWOpzwkfO2FJnCfLeHbq0NxkzWipv3%2BxWh13tCuW%2FF4IduwcSbMNKBscsGOqUBWHWsvOesEaZzPCkRf0Nxbq6XjJdSFJ3xMa75tWZ1Wm9yNoYo2pgB4si2PkDzamxcc1LH2pLlLSjsQmknAfpvcToXysqDdutP9ZVYQPD8yVPa8BZb%2BFTsTqX%2FvbrHZiQC%2FbYOp4MtjvzaMBSF89fekuLAjU06w%2FBS0n040k20UIqhdKc9CPMCvDIF5DlSnT1d0n%2FeO2BqwDP6YXnsEoRkyANMyKSC&X-Amz-Signature=c9b0c595655521865cd49fbd3159b0065e1a52edaec110790086f9f514cad56f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

