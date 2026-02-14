---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LS23BEZ%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIEwp1b9Q9YdUckOAKNSdHZVGHD4ct6eVjcWdGUGMBvfXAiA8yTqz778w%2Bpd0r4y6EufhGuxJ3Q79FMNS34niOuw2RyqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMevOKxn3SRNxW53pxKtwDsv%2Fcbp6j%2Byz1qsN11tZZoH2iBWsCvbmLx%2F21w5E01TE86G%2B50BsEYwNImFVo2K%2FtSe%2BuPIrv0XHKPz8UojZlxCxsfCjsnhonCt018GjfTuUZ2KB4Fd2LgbD%2FPuL73Jwpb07A09msZycthCXOR8AcJyZpiNNicDrr7Q2rEeWnzcyC1Z1%2FV5Cvye%2BPTcDoPoK1Zv6NPUsP5URHNYXud%2FxFF0FAy5j0b8wSthh79ssoOJpi%2BETQqxSu30TX59%2BB%2BbY%2B5iia%2FZLyl3qaqG0zqhj9ru%2BBXsx8DpDQcNZLU%2BrGs2JUe7OcD3cOAP%2BUVveycy144Aha4YTe6ir7PJKxUpq42084tAI4gqZ7rnRSJGEJUB8f%2Fl%2B1iej6n21xkooyX2wmRqM2ahrUQPxyf%2FXdy0fkjZa%2BR3Uz8nbeGCEz3p9dTbO5hytjZK4SkkzZrbe5idW9VEk6SqjJZTzX2JEAXblCwfHZq4rbFHS%2FElPOnLdoQzcVuQD87NyMg10Ov7V4n2CimHGA%2FmgpD5ujL9Tu2MpF48WEyTCi3tpZ3hjQzKjjMuNVB1kAzqSjGsf9z5yEqGZ6B%2BVtO%2BRkw0CNpiMydVTnbX7603LetJS4yAJ9Eddl114KUEa4ymKHY4s7l%2FMw4sC%2FzAY6pgHEzw%2FUtGcjs4eWsaqeRmUgIjJPkGI3H2hnW2aIyvmumi3zQlqvfVLRzo3bLX83DT6MvFsT%2Bd5T9xQuPOfpVGBuOKTP8B029bR%2BCrUQvGz7ZUIodLtLJQuHleDj7P2IZqsk%2F4ZtFs0qzhAqu0m5Gqe7SJdeOm6dj%2BGuL%2FrqTaUI6Wj6E%2F1Foyl%2FQQsAbGMmE88RSeFv4lhLoUCxcgzRXcm%2BnQygGFsV&X-Amz-Signature=2865c908c60db5f701dfff52c8cd7f82a1572b653fa2fc4d28f68c4e838f3b05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

