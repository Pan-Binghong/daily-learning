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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XML5LR2B%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCxe8yWMcXjU6t3JGSh42fd75%2FKHnUXMRtghm6aQi7fZAIhAJo%2FvWLFGDKW%2BH8b3Q7REd1hxqH%2F%2FVEwBC%2BRIRRCdZlXKv8DCDsQABoMNjM3NDIzMTgzODA1IgwK5os3lcTNJ9RXd1cq3AManX1NgbWC%2BvaS%2FcU3l%2FuoSjIHfKQCHDIOXiEfAIO3i7%2Ba8%2BowmnwA5MZTsF%2BuD0LvjMtG2mSaHlicI7dIj6dXFmRcMqI4hZdkB%2BC%2BuNH7J7oUdhuQNpfPbEOj4dYWJc%2BF1xYCSOJE%2Fgltab%2BB9tFGMPxKMC7EdTY0Uci899BhrBq0EyGpY8sxEvnFBdOGgOQbgg3v7QpplHCgBAhZ3EVL%2Bx60LHCIQSnSn824h5pxZ9UKIC0pV4G6N4eQpHTH1vfb%2F3Lb%2FVNJD0yIARXP3LutpqZ1Q4%2BFd37dZuV4gBrUm%2BR4qSD4v3pegoYMncXJgaqGrhcTy5FDaO9AbCxkbnusMViymhFf10bNi7QJbJwOVMu06rjmCHE4GEtDhJSR5f7E3W3gc4tpewS1h7TA2ZMtIEq8E1yjqcJlatx7HuaPDS%2BjZXO8R94UnfnekAyHjtM7nS1wkT%2BR6OMeFY%2FQk2S8C1zPgXqiQEpE8Bx11fDczM9L0C5lfyX7wdnlnXZ5NFm8w6r%2BzPUfIbw5HrGxPStNqO7RNY%2FBYRY4qm%2F2Z%2B0upF4ZheQLjqLbWV5D9htVU2uKbyP6Kb5VFJfw5JbVnLLqSqB7sM%2B5C4UDS3f3eQVTVKF7fy9oG7tc6Yfx6DDS08PJBjqkAeH4HdU9pTssY17TZeG32Dm4vC%2BkjGbkdCpu4t6K51dJdKtuAXgVN%2Ff8U5T4TICDpSRjKo%2B6DXjw1QmJ9I%2FFp34aJ6AKIWtN2isVESZ0VUAjTvO12AOhtQttV01%2FIg5QzsUbmle1A5ffTMF8dWltLdOnngbE1HPMCpobtL%2BjhRrWDqtseNrbrzgP3hh7O77jZ8Lt0n2y8THa3vOkxh33phTUasWQ&X-Amz-Signature=52d9965004050d30e4b9923f63b6ecbb7d07a7af652c10337a4966dd7bc8a233&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XML5LR2B%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCxe8yWMcXjU6t3JGSh42fd75%2FKHnUXMRtghm6aQi7fZAIhAJo%2FvWLFGDKW%2BH8b3Q7REd1hxqH%2F%2FVEwBC%2BRIRRCdZlXKv8DCDsQABoMNjM3NDIzMTgzODA1IgwK5os3lcTNJ9RXd1cq3AManX1NgbWC%2BvaS%2FcU3l%2FuoSjIHfKQCHDIOXiEfAIO3i7%2Ba8%2BowmnwA5MZTsF%2BuD0LvjMtG2mSaHlicI7dIj6dXFmRcMqI4hZdkB%2BC%2BuNH7J7oUdhuQNpfPbEOj4dYWJc%2BF1xYCSOJE%2Fgltab%2BB9tFGMPxKMC7EdTY0Uci899BhrBq0EyGpY8sxEvnFBdOGgOQbgg3v7QpplHCgBAhZ3EVL%2Bx60LHCIQSnSn824h5pxZ9UKIC0pV4G6N4eQpHTH1vfb%2F3Lb%2FVNJD0yIARXP3LutpqZ1Q4%2BFd37dZuV4gBrUm%2BR4qSD4v3pegoYMncXJgaqGrhcTy5FDaO9AbCxkbnusMViymhFf10bNi7QJbJwOVMu06rjmCHE4GEtDhJSR5f7E3W3gc4tpewS1h7TA2ZMtIEq8E1yjqcJlatx7HuaPDS%2BjZXO8R94UnfnekAyHjtM7nS1wkT%2BR6OMeFY%2FQk2S8C1zPgXqiQEpE8Bx11fDczM9L0C5lfyX7wdnlnXZ5NFm8w6r%2BzPUfIbw5HrGxPStNqO7RNY%2FBYRY4qm%2F2Z%2B0upF4ZheQLjqLbWV5D9htVU2uKbyP6Kb5VFJfw5JbVnLLqSqB7sM%2B5C4UDS3f3eQVTVKF7fy9oG7tc6Yfx6DDS08PJBjqkAeH4HdU9pTssY17TZeG32Dm4vC%2BkjGbkdCpu4t6K51dJdKtuAXgVN%2Ff8U5T4TICDpSRjKo%2B6DXjw1QmJ9I%2FFp34aJ6AKIWtN2isVESZ0VUAjTvO12AOhtQttV01%2FIg5QzsUbmle1A5ffTMF8dWltLdOnngbE1HPMCpobtL%2BjhRrWDqtseNrbrzgP3hh7O77jZ8Lt0n2y8THa3vOkxh33phTUasWQ&X-Amz-Signature=83b57a49ba693a92331827471849f0a297201b9a38ae23f7a60675abe7070724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

