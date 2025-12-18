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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZZ3YL67%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbgTSUPeKlb%2Fd6hw2G04pCA9ObwyPLUC%2FwMfz4eTD8iwIhAK3E0SfPvvClIb5XYG6rlDycFHA9wEVR4ZWUoVgdSEXaKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjDt47QeIl%2BCZOUGsq3AMy1iFNasnl4L3M6WzvhgjAyw22XyS2VibqN8U2Mdz7BykQuok%2FHXeTfJBa6Uw9AxxpDHWun1WhizPZAYuvpPwBcsl8l8cREOU8RVUnfCWDyPgeiWnfaHYm5MEn9Aznm0eg3X7cqxrP2dOpWjrKDytTRvdU7PsgnaKqICGeGUGeMpZInD%2Fx9WwkwR6YUXt6bU5IcsIQB4MiqiqAw1630oa1%2F%2Fh9%2B7VMCwCaUP2cRxGEaJEQjtLxuPD8N9lyc3l98wZLscAHgLvJnp94vrestjpgBWhB4RPFtUbIQFDlD4SW7gB1qWaeSpftxGMCRPYwPxEmsUPSRJKR1LtgYu63rFERf1RJiLjkUpv5zABbLPWY80bYTeY0YMhiAaSm1VAuQF37J9%2F33BHkII7FehG3W34k4r6knuX6Uhs24uq4JNumkWs0r4RXTjNeWVBwan066atXjzCSNmINwuAvDLSJip3PLAP7QNsCAwyVz3xpvRHaaKDZ8lwkh01lsvLRADNm5bvm9zZn574oZdxu6dcnG7ynn9HG%2FR7SePHXaB9CksrL%2B0NE3FEXYQCIAjLeX%2FnOd728gh%2FEFpu2MRlG0%2FLCAB1NVjH5bscS9WuqYJqPQ9WQtiSXZQDR2HUv%2BU7lQTCfyY3KBjqkARbjteROOtSiDs%2FzEI8jqJ3qrTrA5jisDFrYt14ZdojQle9tFLgzag4C8zHbPKdghseTPZ7Z7jtSwighu3E7NkTCjuSIhiJSulBwvsv5YN0y%2Fl7ep2phhSCHDViPLMbyzns0agP6g4am2Qr93VyCfUw3HhqiTBjx4AiBIYcybVvcw7ulWE7ifHxkx7RfoTA6QNvqsjLZmmALgT1QonVI2hby0%2F5F&X-Amz-Signature=92fa53dbe37d1660442f0a916c4f9720ea9da8f9b4f017bbe5178e2aa6e48884&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

