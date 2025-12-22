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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7V3CZI6%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQCDaTTIYQi4DogdSaRJ9Z3MAsMZcnfCwef%2FYco0dW%2FlUgIhAJKp3jnhuRsVQyAdAhXY1C%2B5p4U4g2PGKLUKAQJ3UG69KogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzhqZI26NpI97ejdToq3AMMhgB9x9QyFMJSlIVXLn4Ggq3ml6MoYZIiNkNm1GjkjxLsOPNrs4m%2F13BVQ28ojUlApmeTCYt5AIPKhxf13xxuTZKbVj2IQOMxvaMGwSfYAzm8fHSSk%2Fsb11gb6ExwKOdhAY3An9TmnstXB4kyNMTjxm4wsubwDEJyTaIttWxYUnu3%2BkwyLFp3jICNsec01RjfJyUAWxyHGjEEEXoW%2B9UB8ei4CHZOQyYQeMY7YT5o4CstXR4x7rUu5QdDeoBOuMOEx3xASGCPb%2FMRFyF%2BRl1pTIPcaam9gXJGvqUK0ovEWan9723Ko7V9pfbGdP6K%2BZCt2%2BIpYoAJLcXUoEGkaKUiBWlTypaENcx4LAdwDNydan%2F%2BHMVtLwiNZ3B2Dl%2FIA%2Ft19beJoQhWHNnN4wkqZXtQYphdu0eqrtsELJw1cvy0dRrqDl2NM4%2FBo%2BxSNG31Dy%2FqKe7W5UkJy%2F1UauV149SAdyaIlp85ts6G3GPxTc4tYzUHhHRCuHIPSXjNOQ45XX3uartdq9xrvTdHKC08fpoTNN5XkR0zYd%2FZw3Ae5HUxGdb%2F92FNE3nQmJE7b583hXsE%2BTZBv0beOcULOY4Yflvp1FvxOGwqp2qiGRnmZjYkAvPUAslsCRRtECd2ejCg5KLKBjqkAUkvCbPG2TZ1qq5x20UHiTCMwdfNobrzdGE3SRR3lExSJLjjZWB9oRIhe3%2FSB9Mixy6%2FJ9i8z3l00tm2xBwHwTy2tuIDwQ%2Fm26cRz5vsbh5mvPxg7gryKOpOyxCUwEnO4lkzZu1FzonVUThtuTEXyhnGvoVJczW6rfZuo2TjE44B%2FxAVloYIPmgb7G9C9FQrR%2F8c4bRJZdEdNx2OI6VvmQ6s%2FmN0&X-Amz-Signature=2f1827d0a73dc9568b9270041a0157155f65c81879b5c445fa7b145c5b6f91b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

