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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAOGKI56%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEiF%2BRfbnaZpVEA65L%2F%2BqBNlV6IbVEWpvF3ZLIvl2jugIgN2tB9JaczWxtXmZzzireLmhDHe8CCcINBC8tqinuR70qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKE6b%2FuvFFIU80mf7CrcA7M4BXDW6vgs0eXQJ22ElHgFbHqngl8JPkDqQ1ZcT7oWOu1rZa%2BR52Ts%2F7yajzqRQ1Lg3TXRIvFpT7aWkrYFQJzI2YZZqR9PD1QMY0e%2Bt8jFYVJEpSBzihB3rzpZFK%2Be7Ko9WWsZqyaQvzd6wypzb0LKxridtkstxOn1bKhbT4BPdbQlzxJMAw8AJYUWka9UNJTqhDTBUZsJYBSKRYf6uTNgRs1AcWEPJtR7eagiLhJnrJzbGmpI6lEnBvGnmoBP%2BYiEn7fzQTfebWXiyYq2dn25X7Q6EbBVXXsxWeGet55lusORv%2BQS0v%2Fvl%2F2%2Fm5A3q2WyzZWGsNMp6Ppa7QFQUkO6jbsGA5jFrp28I%2FK%2BebRU11VKJOF0A%2Bm8s%2Fv79d1m0zddyBgh0tuJEEmlq%2B0GzuWzHBUK7NLWc2qZu%2Fzxz7OtpV5saQus%2BxeWM9Uj42iZ2gUfkk6W2%2BKvSH3KsjsIAdSsTBe%2Bbs9D4B2IUDjKLf3EX5t10oP%2B0F77dVhmQpySYQPEtEQ9Jp%2Fj%2B%2FUdxYx5ZTGu0Kdv2h25Z%2FAur%2FDLUuyPc5CZgN0k8k%2B85R3eBQqE5Rd6ZvQWezWCRP0iTebmMpElxVk2Yxy5lW21oT0b%2BP5UVTZwQvow2LxqjpLVMK7JjcoGOqUBmVs6K4n9A%2B4sQohpGCFEplxSSsURKET9CyG3Lo9ys1qcs5gIH7acILhlXQTa9ZTHuWR57Sj8eCso8wLwD3DHG3gdhXEoDk6E4hMYgwh3uM4aNaIj%2BG2tX0GeTlIlP7dY4d2qN3zE6kk8ym8NSGEj2XXtreuNWVHT%2FTp%2FdjpD7vk3hhT9tpDUPaHwOgNE3sZgG9vyhuu46kF3Shd0srIDDgfDG8H5&X-Amz-Signature=cb86e35936039b499a279e6f0b9bd6d469f92d49b2d4627dab1521b371e81054&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAOGKI56%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEiF%2BRfbnaZpVEA65L%2F%2BqBNlV6IbVEWpvF3ZLIvl2jugIgN2tB9JaczWxtXmZzzireLmhDHe8CCcINBC8tqinuR70qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKE6b%2FuvFFIU80mf7CrcA7M4BXDW6vgs0eXQJ22ElHgFbHqngl8JPkDqQ1ZcT7oWOu1rZa%2BR52Ts%2F7yajzqRQ1Lg3TXRIvFpT7aWkrYFQJzI2YZZqR9PD1QMY0e%2Bt8jFYVJEpSBzihB3rzpZFK%2Be7Ko9WWsZqyaQvzd6wypzb0LKxridtkstxOn1bKhbT4BPdbQlzxJMAw8AJYUWka9UNJTqhDTBUZsJYBSKRYf6uTNgRs1AcWEPJtR7eagiLhJnrJzbGmpI6lEnBvGnmoBP%2BYiEn7fzQTfebWXiyYq2dn25X7Q6EbBVXXsxWeGet55lusORv%2BQS0v%2Fvl%2F2%2Fm5A3q2WyzZWGsNMp6Ppa7QFQUkO6jbsGA5jFrp28I%2FK%2BebRU11VKJOF0A%2Bm8s%2Fv79d1m0zddyBgh0tuJEEmlq%2B0GzuWzHBUK7NLWc2qZu%2Fzxz7OtpV5saQus%2BxeWM9Uj42iZ2gUfkk6W2%2BKvSH3KsjsIAdSsTBe%2Bbs9D4B2IUDjKLf3EX5t10oP%2B0F77dVhmQpySYQPEtEQ9Jp%2Fj%2B%2FUdxYx5ZTGu0Kdv2h25Z%2FAur%2FDLUuyPc5CZgN0k8k%2B85R3eBQqE5Rd6ZvQWezWCRP0iTebmMpElxVk2Yxy5lW21oT0b%2BP5UVTZwQvow2LxqjpLVMK7JjcoGOqUBmVs6K4n9A%2B4sQohpGCFEplxSSsURKET9CyG3Lo9ys1qcs5gIH7acILhlXQTa9ZTHuWR57Sj8eCso8wLwD3DHG3gdhXEoDk6E4hMYgwh3uM4aNaIj%2BG2tX0GeTlIlP7dY4d2qN3zE6kk8ym8NSGEj2XXtreuNWVHT%2FTp%2FdjpD7vk3hhT9tpDUPaHwOgNE3sZgG9vyhuu46kF3Shd0srIDDgfDG8H5&X-Amz-Signature=09a9bf9c64a81d6d0edb3b758cb6d3be156c88757615ce0be5fddcf865b010f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

