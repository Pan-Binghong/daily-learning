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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RD65XAEG%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIAeDCzE1GVVDTu3rKWroIChBhqIQfvcvKWAPJF%2Bojeh4AiEAxUUg3zNfekxcPjmk0KqPxElDls%2FqQF%2BB%2F5eFYtEbRy0q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDM6UXSff%2BCzvWT95wircA6qEcRwvZqcotBCqZH6dw1z727p7EyxbObz1qBkLj5FT768k6Pz3kr55qk8kBQ7Thw4L3RMeyfRP7RAA1Ri5BIsjpt23rvPdW6iazpEHOJU%2BA9umRBniq5t2d%2BgApN1DI5k4wJiIJ1qrrAGniu%2BQktwICc1SWl16t3fCjNsZuk%2BmALXMQLj1Syvp90vWFNL7NblvXHTVRchhne2S21FQx%2FPKStSDGRLiQAE%2FuyhEqUGMBGKEZ%2FI8H5TgpQxF%2FCUZo5%2B6ijTHuL%2Bz41p3e6zYVXGhI9asSEt%2BC6sRab7Q6A0RLhckTQhKQWL9B0ZPGtDGaM1h3kJ6tOONgojvta80taQHBHI%2B4mp9qApVMPF8ByhOEW0OKvG%2BtyzMNSEkiwuTG9285GalYkgQUJfFgUQ15G4CwYbhN7QDTZM7ha%2FV0II3zwd0G3YwJai%2FeEoEhQ9QRLu%2By1TbJTILnQGYYRAEZbipHgcssPcGRFGsmH%2F5bW7iNA6NO%2BJWNdgvrewEIk3FwKNRWDmjrjdZAK4Bdf%2Fp2Wjahn7MOE7yarskTomke5fYenV3f6gx0yi56fs7nEswlpjHu2DgNN4dt%2BR6ehqd0is8uFEJEjseVnGAozfj94Xht9JB4YJOVlR3dWAgMNiP%2BM0GOqUB5foSj1%2FHR%2FEy6bX2%2By44VktfiUAFsGVaamzEksDxqXsAQnCfww1lfmLBG%2BjCge6XgG3Uoi%2B3Yd1q5BNO5GympZeCEFrWCQGx93MwjW8k3AyfU2hJ2mBOhbTmcsUdl5FLWt%2Bd07Pet3c%2FasBqkV4unJp0AAN%2BwsgewXhmP6MZGl%2FxCXkBz6Ns7kRB29r5H6Smw%2BBe7tCZb9hb8D5m7awhnNWWtJ9Z&X-Amz-Signature=c07cc18caa5fd9f8d0def8db2a74196d7ed2d6e31c72228582ffa7a239cb09fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

