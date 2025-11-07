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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNXKK2GX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FmvnMYAUYcRR%2BQiJo8p9REKZe01umWWF4tdn2c8ZOLQIgb65zbw0XmKfEhDSUlc6NUBEW%2FylVwmJ%2BBJdQsM%2BZCY8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK0YtKCBwx4kGAKzHCrcA%2FRRckq7r7blWOkMqSGqSeEkj0neWIWYQwjfF13qgWWrjr8vSqZ5gcRdkJdN5pxKf%2FeTyvAdSdTSV2va4kClpVAdkhdwc%2Fe%2BIbz1WfFIwvIxecKCkL3nU8kTtiqg%2FEXK8%2FkZGbA7Y3XmnCzhDexbkP5jaf%2FqN6W5hm9JNeVIXOj5sJDhVfSOfr8nXHFcL0eJDfUjgFtRBhkKpV4yllvxMde%2FzbLqCJaOw4dgBGtf1lQhPzEuyEmmk2S4ZBNVOt9KOR6U3QAoAdL%2FMcZBN9SvsGH%2BP%2Bkb1f3%2FqVc3R4tUb6vYKcM43U%2FkG5v4Lm%2BzlLQkD7PUPdBTUsHV7yYzLtBa7LlkjZ7Tihp%2Bk3bMLekta5ikUApL0lgryoLf4xeIC%2BiwjhWhN6aHcg5VTN3EC1eZ%2Fx8RzkU%2F15IAidhiWcyNE4hAOrBHujFYkxSwD5vxDpLSLbEqFlOfKI%2Bls3bNY5xuUiDuBhdSP1KVrGpxu4uc2ZtTcfFUFDXvHukAhwnKTir%2BwNDXFaexbRuSmflV7bA3t%2B0DnCCPqoHMkqCVlao7k5iwl423CV8BWNp37ewTRwPw7mQ1LSA2M9CFKt0ONJH3OxQGRsnKXtfQ9iGh2xKSav%2B%2Bg2rV2CwNs3A7BS%2B7MKa2tcgGOqUBB70sWs%2F9OyKfoujeWMbseWpuSafjUU2ypRdGKVBale%2BqO7vz8JMQ3yW4uTTmIkLJbhqf5GoTfMFyd5S44ckAcJw8tZ9GpX%2BLz%2B8oUIja2%2Bx0kZRlhjHzJdqFAF4HdRm5NzGVqS6NlBJAN1I3PzEBUHTBrzODkyMwa4Cj6xZY75tWfPtPO9TtB%2BD79%2BCOZvqUqOV%2BL2VvuxLdFa%2Fz8tn6D%2FAD37wP&X-Amz-Signature=2f5b4436199a8c49c887c8ff22f048a521aaff86b46d1ceafdf5cc045766f2d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNXKK2GX%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FmvnMYAUYcRR%2BQiJo8p9REKZe01umWWF4tdn2c8ZOLQIgb65zbw0XmKfEhDSUlc6NUBEW%2FylVwmJ%2BBJdQsM%2BZCY8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK0YtKCBwx4kGAKzHCrcA%2FRRckq7r7blWOkMqSGqSeEkj0neWIWYQwjfF13qgWWrjr8vSqZ5gcRdkJdN5pxKf%2FeTyvAdSdTSV2va4kClpVAdkhdwc%2Fe%2BIbz1WfFIwvIxecKCkL3nU8kTtiqg%2FEXK8%2FkZGbA7Y3XmnCzhDexbkP5jaf%2FqN6W5hm9JNeVIXOj5sJDhVfSOfr8nXHFcL0eJDfUjgFtRBhkKpV4yllvxMde%2FzbLqCJaOw4dgBGtf1lQhPzEuyEmmk2S4ZBNVOt9KOR6U3QAoAdL%2FMcZBN9SvsGH%2BP%2Bkb1f3%2FqVc3R4tUb6vYKcM43U%2FkG5v4Lm%2BzlLQkD7PUPdBTUsHV7yYzLtBa7LlkjZ7Tihp%2Bk3bMLekta5ikUApL0lgryoLf4xeIC%2BiwjhWhN6aHcg5VTN3EC1eZ%2Fx8RzkU%2F15IAidhiWcyNE4hAOrBHujFYkxSwD5vxDpLSLbEqFlOfKI%2Bls3bNY5xuUiDuBhdSP1KVrGpxu4uc2ZtTcfFUFDXvHukAhwnKTir%2BwNDXFaexbRuSmflV7bA3t%2B0DnCCPqoHMkqCVlao7k5iwl423CV8BWNp37ewTRwPw7mQ1LSA2M9CFKt0ONJH3OxQGRsnKXtfQ9iGh2xKSav%2B%2Bg2rV2CwNs3A7BS%2B7MKa2tcgGOqUBB70sWs%2F9OyKfoujeWMbseWpuSafjUU2ypRdGKVBale%2BqO7vz8JMQ3yW4uTTmIkLJbhqf5GoTfMFyd5S44ckAcJw8tZ9GpX%2BLz%2B8oUIja2%2Bx0kZRlhjHzJdqFAF4HdRm5NzGVqS6NlBJAN1I3PzEBUHTBrzODkyMwa4Cj6xZY75tWfPtPO9TtB%2BD79%2BCOZvqUqOV%2BL2VvuxLdFa%2Fz8tn6D%2FAD37wP&X-Amz-Signature=ec1633fa5d64299173698b56ded3dbec6c44c9c977dc56adbd3f9a587d44169c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

