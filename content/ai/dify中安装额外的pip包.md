---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663HFVMHL%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIB2vw1%2FL9MgovO8ykOMjCdwLyjUStA32DmpjQjcPvpyTAiEAldOxBpa2GitY0EjhT71RC%2BxuVotcFHXa4dKzwUAE5IUq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDGZeXKSIyiq%2BrCfLxircA6w%2Fm%2FJSowKz67jsQUd98K6kF9Gtc8o9RBg5nypHc23IkJ8ZzTBErWGe5jbUwoA2R97V2EeY8KXU0w8%2F887x2AQ7zWdyCeb%2FEDtoSgJZZrrla8kmkYSzV%2BX0GXflJTnABm4M6exU80grOEf4gz3SFh7Cx3DCvw%2FRUH8q%2B5aXk3ueloqwtaREVze9sC22ul1In%2B9JKXDJ%2FYayapj1Gd2ItVQ8JBQIiETlab7Cd1F0b4iDuzE0IlRawBMGMsYpLQljxgTNyYsCNbYakuhSn58JrssFKBLjIE8W%2BxGDRiX82lNSRPEAlwhTnSBddAyuZDz7VGZ%2BZdxEHJRSeoMvtT1ge8FZCmGiX2yzOa9obsOfUFlr7XXuKGjHDhCnLgR3pnJl%2FPl3q5wS6BqaKmHDSMbWzL23bM9pcEHkxbgcM1RQ7bvfbRQLQrMxcq6deLWPryiDh%2B5BfNkYClybrW6K3msYOki436ZjVAaLS2PsZVegaE9xBOL6j2w3fJUZcwZnLDufyBDMQL0pFgkpEDfK6HFOUkBaVslNAp53z9%2BP%2F%2BFGteHsfWG5nW%2F7%2B%2B2zMae1Y2q%2FbqnfxsUhzaAPKFZSBFTGkhw0eVwpNMw3Ar6zi%2FxqVHDkR2v5ewNbRs93z66PMIfVw8kGOqUBk9z6i%2Bkn%2F%2F9kRwApooaOQt4TeyZSO1zaATggjrl1PWdb56mVQX2XyAtqfjxshEu7XTPezzkOfNLG5vpmbFCCABqnQd09D7ZMsF0M7fJa5DR3LEh6XDcoXag0R8c2gq3818mp9%2BoJObXjUxRQOs3Bd%2BLBS62%2F7XuMGuQ5g8USem8%2BZWeceLU%2BLsbN4HQM5cNLUlqkoEtjMr3eskhmPE3KdmVxwhKb&X-Amz-Signature=ac0ae3bb129541cc1e9925558c01bc218cf20ce53cc70dac2cf48e17d6a3cc3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

