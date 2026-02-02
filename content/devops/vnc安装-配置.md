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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX7GYKCU%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDfxq5ow%2FVmrlq6ZX9LpLyh2PKf3sCzECwl9FQTuUTmnAIgNgXN3znB1wi9mhw7sZc7LMRZLwi7KCBzXDsC8SBC7VEqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6hoyT52dQ0uNZMAircA91WLMLAQWSweCl%2B24%2F1%2BTentJQPpjV3Du0y1fFOgZVrLSDKo1e0ELl1A3rmJPCzEi4dwv71JoFT1reRrowb8xY4xw8FuDHlhhY4aV7WhnkdcCsP73z2CBGeutY%2FG3qm%2F3ygi%2Fd1sPU1fkKRsq09i8bv5d3WmVScGnmAWU3gTTQPzWIOCYVKcR8zplAigPW6a1VAhYuOjBao%2F9NXNzOlQMcihpoXsH%2F6WPmgdzsrOpezMD%2Frs4ixVMn93W6oEAesxJQATb518SVu9trk%2FfRPPhr2e2CH5bwwuSSvPFjKzdAV1woN6wBbi76duCZwhJkvwQHw3ZK%2Bj0i2TjziIkZBAartqGro%2B2musfXh%2FbVHzZNgLDyZvwVaxet4Yh7P5SmvjmPJV4plelstz0hN7P9SwRdsIPRViTViZj98KX0O79whDoyxWFunf4Cgoi%2FoSeeGiN1niIW3LMML9I7XZHtAnJxZxtHgfLKN5mRQXJQoA1ubm5LjpzUck75zEkRLUy4NPo9%2B3dZEwkRIybwhsWHNVSXPh4BCGwDtyFi%2BNWY%2BBK64kvj9X0RGuZKZNg8vsgJP4QLim6Mc08fVOA8yq%2F%2BqoGfwKh%2FcOnbEijvV31o4h4bE7Wg1vCJLYYw2F9XNMIGIgMwGOqUBrEDy%2BN1nFnvlY4kRyvXK8zwLeM9ms9zphcyU4B0iPyKtZ4dHpAWYvC%2FlWEkzRPSrB2kcvpF0VGgZm6cTFNfGUU%2FscvcmFpQCIxkH7XMyFzDV9drzEKrxKTiSwdCkTAKEfvSejQ3TMUOeLchDsx5T6SCatNRbpIownBYrSnn7da7RqTyAZ4dT%2BDvAe3xzgoQFQXffd1L5FhJUKJV9lkskFTu%2Fi67X&X-Amz-Signature=1426c8457f7251bf27331896b0895b04026d33180735d72bc3605b8e213f7e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX7GYKCU%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDfxq5ow%2FVmrlq6ZX9LpLyh2PKf3sCzECwl9FQTuUTmnAIgNgXN3znB1wi9mhw7sZc7LMRZLwi7KCBzXDsC8SBC7VEqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG6hoyT52dQ0uNZMAircA91WLMLAQWSweCl%2B24%2F1%2BTentJQPpjV3Du0y1fFOgZVrLSDKo1e0ELl1A3rmJPCzEi4dwv71JoFT1reRrowb8xY4xw8FuDHlhhY4aV7WhnkdcCsP73z2CBGeutY%2FG3qm%2F3ygi%2Fd1sPU1fkKRsq09i8bv5d3WmVScGnmAWU3gTTQPzWIOCYVKcR8zplAigPW6a1VAhYuOjBao%2F9NXNzOlQMcihpoXsH%2F6WPmgdzsrOpezMD%2Frs4ixVMn93W6oEAesxJQATb518SVu9trk%2FfRPPhr2e2CH5bwwuSSvPFjKzdAV1woN6wBbi76duCZwhJkvwQHw3ZK%2Bj0i2TjziIkZBAartqGro%2B2musfXh%2FbVHzZNgLDyZvwVaxet4Yh7P5SmvjmPJV4plelstz0hN7P9SwRdsIPRViTViZj98KX0O79whDoyxWFunf4Cgoi%2FoSeeGiN1niIW3LMML9I7XZHtAnJxZxtHgfLKN5mRQXJQoA1ubm5LjpzUck75zEkRLUy4NPo9%2B3dZEwkRIybwhsWHNVSXPh4BCGwDtyFi%2BNWY%2BBK64kvj9X0RGuZKZNg8vsgJP4QLim6Mc08fVOA8yq%2F%2BqoGfwKh%2FcOnbEijvV31o4h4bE7Wg1vCJLYYw2F9XNMIGIgMwGOqUBrEDy%2BN1nFnvlY4kRyvXK8zwLeM9ms9zphcyU4B0iPyKtZ4dHpAWYvC%2FlWEkzRPSrB2kcvpF0VGgZm6cTFNfGUU%2FscvcmFpQCIxkH7XMyFzDV9drzEKrxKTiSwdCkTAKEfvSejQ3TMUOeLchDsx5T6SCatNRbpIownBYrSnn7da7RqTyAZ4dT%2BDvAe3xzgoQFQXffd1L5FhJUKJV9lkskFTu%2Fi67X&X-Amz-Signature=f4251672a40d52847c0a259f183e5006b1cee24250f31b8c2aeeec62d836da7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

