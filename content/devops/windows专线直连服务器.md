---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655UD5MGQ%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQDZx65kW37b%2Bbp4kDvcpschiiWRUKdmZzJfJoscBY6e2gIhAK6jzCjL5XG0gqapbcNKC3GApHLconMtrE6b4fPCkGd9KogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyB79EUlOa7TbstoJIq3AMtOLmOeIyMo9r32TBub%2Fr5xIdLqz3Dmgif8baJxDRXuEY4uxc5UK35uhpSTG8BmMCCgXBknJe8SeJYV4EsHJDmpeYwKTQirANFAjCdZiSdD4Tmns5OXTRf5rD6CfbMkzm2hZC9k2ywyfQP62IjyYT09jzWH5ebDVZVTNbLEC6jrcVwgxq8odP%2BmxiIlprPbYBaN2Wac6Nygl%2B%2BOYypJtm3k8532QbFYmSY3LSSHyy8nPWjqy7grl4x888Kyh6b9MZJoDANKNIqE8QUGlKPnojrmaMrRstZWjpESwZTG4ycOHIGA6FItXyoAl4QTjNU2niw6VbiryO1mgn85%2F%2FHqUrQtXrUxY8rLecmawzyOFFaHgQafRvCk%2B1SuOSXZ0ga71Rrog13NqDZZbWMmZUMkU%2FcaxMHX4eF8IL2cEkkPmlAIAl2%2FIpmr%2FwFCVKCzy3YdHzUuAbYqVBaHIg3V0oV03gA9iCUdN1sT6lAI%2BorRRJx4AwEoAAX5w1UHf7DdMMv8XG%2FHhF2E%2B5mqo96dAqJRMt847yjloCDf0ob6Hfj5s1OI3DXyOTaecSS8fWNuoLG8fCY4zdv2qhH0zd%2FplIyxH8LXMzkpkZH09twb1Ey6y%2Bp05R6T%2BfeUtuzOi65fTCDvYbPBjqkARyqoE7muYa7ZEKNONlag8lZ%2BsbyetHmE6eGVdC%2FIL%2Bb%2BzbJ%2B7D3o2TKG4cbR5yzYxbs4P6SFZcB3Tnyhnq2lH%2FGFg5lqda9fO%2FLknsufuQj%2F%2B%2FIf5qyNV4JucdcMWPoMw%2BEQYE6a8IcHZYe6nvB2ngHqdGXt1cUCfRTwTGPR6gspAkL8jcMsPGX6rpqZwgcitLlBLLCIGkvrKckx6Ke26YYOnLj&X-Amz-Signature=7f286737a46d9b8155e2d974afad2d3cb786ccfc18f1d6233c747fc5a47c901f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

