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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPGOAXSQ%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCaeRHaYO%2Bah6O7ZQb2KsllQzm1uOQqInlnSfFzRcLAwAIhAOuG1E3Xde00GPcu4iaz9TrzyULiIjuMr0cc4GhDP1NHKv8DCDIQABoMNjM3NDIzMTgzODA1IgyInv95JMxp8fwdGVYq3APPwmUhgBzeJqezaXSn%2FqCUdhPRbQTCcr6X%2FC8QsFVETS3NC6G2PTfD504asWlYFPMBsoQ%2BmjbJZHa34nYXmxpj0krbjUbsHvVpOIKUY5FZ1DzPtQwdKhm419vkwVEq2xYBX4gwiAT1n6YUiIfPH9kTR2ZFyFZufJZZ0HuL2By8nyH7nsEQp7oUE%2FjgF0ZryzLw5Ej%2BiMzfbyBl3y68McM%2FbfMshjEmRYGazJiD6WU64m%2FcDzxFuS1Ok4qOIKOqYv8SVuZl1ilXKyDNG14UC3XA2MneEwxMxyClndhbKpkEtcZ42zGEdseJSPPpXhzREoBeb6JX61XRCBXSsIQnwtixMUZg14v%2F37xxXwvi%2BZgY3HwiiC%2F54bPgCMBJWcQ5ggEZlbfu%2FhpFFHatrj9CQ7a5Knd%2BGE2I1KmegrTSyI3xhl%2FHHMtkts%2Bsx5y4BqS3t5Ymfbrj5xG4hgpPOfQ5ABnEDBAT2yrKPWTuGvNtTRergydzMzzVeLeXwC3ZFQQHVtEbhKgBTcr1ph4aBCZtZFoNF4Vi5BlId3jXsq55HTHF4Rsd0ziZGk%2FJMpTe5ZuuPQ%2FuoqfD1xwpZIdAakjFvGrSoLhDBW3MNZ%2Bymn16fOPvRsmxiPmglGRAWgRuATDWsInJBjqkAYt4amLHZ7pOi5L5ivKLX0De7pQQGoKMP9dLt7PVt8LMIUDutRNr1oB3XbNSIPn5aiWFA1cOK8Xa4cmyzWY1oIYL%2BS24KoTDqJJauyIpEhQlZElOV5n6VJVzUS%2Bs6dJR1ogxMp3iO%2Bqz9obtlTdfbluGgY9MmveNmznAweDRbE4TBSqwd7NTod5MXWSyA%2FMtmhdeKJhDqXdWWK0RwLQck73LQYbQ&X-Amz-Signature=0509fa86c10a751ede2cabaaa2e6461ac55f117a0525dd1f0ae23bccf4345fa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPGOAXSQ%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQCaeRHaYO%2Bah6O7ZQb2KsllQzm1uOQqInlnSfFzRcLAwAIhAOuG1E3Xde00GPcu4iaz9TrzyULiIjuMr0cc4GhDP1NHKv8DCDIQABoMNjM3NDIzMTgzODA1IgyInv95JMxp8fwdGVYq3APPwmUhgBzeJqezaXSn%2FqCUdhPRbQTCcr6X%2FC8QsFVETS3NC6G2PTfD504asWlYFPMBsoQ%2BmjbJZHa34nYXmxpj0krbjUbsHvVpOIKUY5FZ1DzPtQwdKhm419vkwVEq2xYBX4gwiAT1n6YUiIfPH9kTR2ZFyFZufJZZ0HuL2By8nyH7nsEQp7oUE%2FjgF0ZryzLw5Ej%2BiMzfbyBl3y68McM%2FbfMshjEmRYGazJiD6WU64m%2FcDzxFuS1Ok4qOIKOqYv8SVuZl1ilXKyDNG14UC3XA2MneEwxMxyClndhbKpkEtcZ42zGEdseJSPPpXhzREoBeb6JX61XRCBXSsIQnwtixMUZg14v%2F37xxXwvi%2BZgY3HwiiC%2F54bPgCMBJWcQ5ggEZlbfu%2FhpFFHatrj9CQ7a5Knd%2BGE2I1KmegrTSyI3xhl%2FHHMtkts%2Bsx5y4BqS3t5Ymfbrj5xG4hgpPOfQ5ABnEDBAT2yrKPWTuGvNtTRergydzMzzVeLeXwC3ZFQQHVtEbhKgBTcr1ph4aBCZtZFoNF4Vi5BlId3jXsq55HTHF4Rsd0ziZGk%2FJMpTe5ZuuPQ%2FuoqfD1xwpZIdAakjFvGrSoLhDBW3MNZ%2Bymn16fOPvRsmxiPmglGRAWgRuATDWsInJBjqkAYt4amLHZ7pOi5L5ivKLX0De7pQQGoKMP9dLt7PVt8LMIUDutRNr1oB3XbNSIPn5aiWFA1cOK8Xa4cmyzWY1oIYL%2BS24KoTDqJJauyIpEhQlZElOV5n6VJVzUS%2Bs6dJR1ogxMp3iO%2Bqz9obtlTdfbluGgY9MmveNmznAweDRbE4TBSqwd7NTod5MXWSyA%2FMtmhdeKJhDqXdWWK0RwLQck73LQYbQ&X-Amz-Signature=687ddc3530fae6918c448dbf2b35354a8cd8b690674ea358a6fae4565a04bbf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

