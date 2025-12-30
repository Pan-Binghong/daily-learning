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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3NWEEW2%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDiMKPmFv2gtfSm%2FNp7Pyva1lg2w0alkxllEAMIJo%2B3PAiEAit491q3V4uTO12hblg%2BL%2FfOXunv9weVXdGFQRLlBl%2BIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAMeTdhU8Ba%2F2anzGCrcAwA5ObcTnB8j3wYnr%2FNjWMEeliIWQ8cdz%2BG456vS3%2Bzec%2FG59XPn2jr%2BI25yN2%2BtvE6DLCTxJxNhOWcC9yysYW2RQrmyq0sslV7sQWNt7ZtApsljhTR2HhCqB5%2BXN2ltsAGcGBLFFj%2Bgceru5%2Brmg%2Fol8vktiW06HitQsQexJDyUyf8WC%2FucD4rrqX4hHBnDyH9vbwAgHRYeptzxwjpVt8FuqmFj9oY4o3Vf0PBSLJ94SHGM2pVUZX%2Buj0z9ylyTbxvprKvlMz2s2A2XBFJQmnw9kiWBDjvdisJ2PklfGA9P0TUDQHp%2BAFfKAF%2F9HMKAGIaoE1Ixv8%2FfMnbJQMrktn3srDHbENgHdcyuFBzzeZ86fehtkh45HYkZPonbC3iYRJseLJTAigCQ6V2jIsId%2B8nNZCF51mc5jIPWEMG6bGPX4EYxwr6A6iL1ih411WEQZbiIcv1%2F9DJoYEKnKraNYO4mREVALFSXUYzzDqqFmXvrHBBcNkAvFjKiCr0kHKdS2XKbRRu9DqD%2BkV4gnfOswEzj7VKHghjepIckNxvDnWu6G%2FEds3KpiFYuYFka27qUDMS5%2BWW8wJIVqBPAKf8RLfIjGDgxyiJHoc0fwkMCSPRNpVqMzhJY8I73niUcMJPTzMoGOqUBfVfgv9QiwHjBFVUYmJZfp5sRGT7qe2TYdycQvusZrpJq9mJuUf0W7oRDM9oYbWWyuC8RZUQBgpbwgKgy4sEsvbWoKati3TwSLtYC%2FcCbAEr6OUv9Hjg%2F1SwPloQFkk5Sy3uqlH1I%2Fvq6lUKXXtf0VW6QH724lJzC9p50biHimDaGHfVS5vFG5dJVVCCC%2BPruSJGYgd2Ml81qwHx88LExv9GgoXi9&X-Amz-Signature=718b4f7e609ab242db868c93ee413eec27bf4edb79e0d05d6338e6e86549e7d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

