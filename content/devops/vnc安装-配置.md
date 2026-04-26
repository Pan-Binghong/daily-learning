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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMFXGQJP%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHF2EqSlJwrRn0Mx1RFPX1kq%2FCWh2Nc0%2BLEpcth%2BRfuyAiEAmZ4vrNid3zuf27OveDqn0UyvfW97rGm6ZkqegRuSJI8qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK1WYpk3nT4QHrukByrcAzWR5PW56kikEdNwf5WDG5BCNMlF3yN9qZqltDJJ3kB8IizU2iYl%2F%2FndzrIIO7ZQ8k8hfg1qaSr4CwnSSm2fUxcYIAiwaLnzg7FOTUpdTNgTDCXPbyeqwMdscW4Y1mzxRZGGSeGXBHOx70XTyewXzbw5McFlF48JRHbwqPEhyH2PwlOyv%2Buk1XjfcY0902Clr1mm4HivLHKWzi45Ho98QuUBgBbkpdoH2iG62mtRU6ECRaKqMf%2BziTqBbXjNFGeC4euaTwSWK1F2wirUDGQBK%2FXaEdUWD%2BQUT9lvP%2FDW1K5OxZs3cp3lQdaVeCYJU6MJZdkThUr91PngRIkbJCicM%2FDvGXEG54ToXc8Q1aJOQDeAng0r3%2BhJoSZVLrlI%2BvpAD9hK5jq6UiWuT0GN7muRdMHLyCNA5QsJFkktEB5BaPxDYO5d4W2flbGHUcoj8wYSdv9QbBlUY0%2BFtq9LbdRHOFf9BNG8iGJ6rjHPQloPKqjcNjqciIkoxc%2BVFYrjsENVZtLxt%2Fx4eBN%2FjTujVeBMyFtXdpT2t6s49U%2BO8cOPtcd7z3cHO7vlEMV1DdGJLQ7kuxWVSifKiAtTTXB%2B%2FZccQYcgO5TMLKYvwT1GukmDQOSrsZ5CAhq0for8b1JDMJqPts8GOqUBUKyycFRxLZDc9ILVU1NPQQeLQT%2B6%2Bqhw6iZ%2F7bSJpvyX%2FAsTVb7hgkmMrDFghVTo2flSVlbOUfkVYgOVeknOiL3bJiG5B6FDHLSYytnFtEBjCkt3jBkziW%2B8afokubYC%2BLa7Fdo7gbhETE2lNJRLZVNdPyViP60y0h15u%2FvsCWnwkESAygdQzbinIwf%2FXkA4LSxOoXkSHdws7CM%2Buq2hEUQQR%2BvX&X-Amz-Signature=b10eb2011837ab43cdb87a2fb52b7d9466960d10282bdda262ec340175d3a088&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMFXGQJP%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHF2EqSlJwrRn0Mx1RFPX1kq%2FCWh2Nc0%2BLEpcth%2BRfuyAiEAmZ4vrNid3zuf27OveDqn0UyvfW97rGm6ZkqegRuSJI8qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK1WYpk3nT4QHrukByrcAzWR5PW56kikEdNwf5WDG5BCNMlF3yN9qZqltDJJ3kB8IizU2iYl%2F%2FndzrIIO7ZQ8k8hfg1qaSr4CwnSSm2fUxcYIAiwaLnzg7FOTUpdTNgTDCXPbyeqwMdscW4Y1mzxRZGGSeGXBHOx70XTyewXzbw5McFlF48JRHbwqPEhyH2PwlOyv%2Buk1XjfcY0902Clr1mm4HivLHKWzi45Ho98QuUBgBbkpdoH2iG62mtRU6ECRaKqMf%2BziTqBbXjNFGeC4euaTwSWK1F2wirUDGQBK%2FXaEdUWD%2BQUT9lvP%2FDW1K5OxZs3cp3lQdaVeCYJU6MJZdkThUr91PngRIkbJCicM%2FDvGXEG54ToXc8Q1aJOQDeAng0r3%2BhJoSZVLrlI%2BvpAD9hK5jq6UiWuT0GN7muRdMHLyCNA5QsJFkktEB5BaPxDYO5d4W2flbGHUcoj8wYSdv9QbBlUY0%2BFtq9LbdRHOFf9BNG8iGJ6rjHPQloPKqjcNjqciIkoxc%2BVFYrjsENVZtLxt%2Fx4eBN%2FjTujVeBMyFtXdpT2t6s49U%2BO8cOPtcd7z3cHO7vlEMV1DdGJLQ7kuxWVSifKiAtTTXB%2B%2FZccQYcgO5TMLKYvwT1GukmDQOSrsZ5CAhq0for8b1JDMJqPts8GOqUBUKyycFRxLZDc9ILVU1NPQQeLQT%2B6%2Bqhw6iZ%2F7bSJpvyX%2FAsTVb7hgkmMrDFghVTo2flSVlbOUfkVYgOVeknOiL3bJiG5B6FDHLSYytnFtEBjCkt3jBkziW%2B8afokubYC%2BLa7Fdo7gbhETE2lNJRLZVNdPyViP60y0h15u%2FvsCWnwkESAygdQzbinIwf%2FXkA4LSxOoXkSHdws7CM%2Buq2hEUQQR%2BvX&X-Amz-Signature=443817ad0251ff1f9220d4b8a0e04801d91aa5c57a0f51821c4cd38a980c916d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

