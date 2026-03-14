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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIJEK2UN%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTN0PKBp6re74oDd5On8UfA9HcwudEBKKyk%2Bro2J%2B9swIgGQCvI2vToP%2BaR37x5%2BfluJZPLVO3U5BrBivK3fJy6iUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRJscivASMg0%2Fgf%2FSrcA9O1U96UL4IHkIZWIstdIR31142JC8QzHGUa2VFjcbXcbuV8OsWBiLQIUO1oJpNtjAnzCMpk5%2FRT4UGRfPLQnnQBL5mmItO5jrHL8wPb%2Fv1bm6SNtS6VHzZQPLchQMV7p5%2BXRxBXjngXQ3dhM0%2B3EXVLjhqd5AUQxY%2F0xVj7GlS0ahxfsVkNUP5sc7OOcWIHzt47vK6fU1VJPMzBxCsxdVnhJYSvqWB1EFiAUTJKod7e7%2BOXqtqYCkXvyTdoTOo6qbbYoRD%2BJ3KlLXeGHnehNfYtT9ziuae4jGgKW%2FIjpMk%2FIpqDk7FZISO1HtvQJ59wuGqJ0q3BNoGYA7GKRmEZ%2B9CkuG3tyJcDJCYTcOuAOrLkzMwq21TWe8mrcFHOtwwwES3tSpS1lZDdHoB2W4g8NhXknEVMhKH17IRVLPVSkjDd9f1f26%2BdR%2BI1FsePX7gmt1VVYNoLNk%2FbEwmqlDmo3%2FghvsumMv0nx0DkKoRweft6SZ4L978m6MSVmAbm%2Bl%2FLTTqnoQ9HTwtSZK5JX5%2FXXe8My4CBvWj%2BIqalrZu8M6ghW3K9MfM6bbMp2Lzo4ylSFK%2B%2FWGNWs8PoibVnX37dNncl1H%2BgyUvN8uJNhsNsXYJ%2FvWBKGti9hdRSAuStMPWB080GOqUBn3nEwd5Ih0cvBnOpCzexNijnTq4A1s0geED0A%2FP%2BDaZNqrKwG1GE9zu8krpjFUXr1oKfEF077H02AufHx0eeQMmYqCS14LUlxcAbj57ealBG0%2BACCdavxQ2WU%2FD7c6e5l%2Flt4nJ95EJmmWwrOlwgy%2B4k4VMdKf%2BcoUg%2Be%2BB%2FdlNvXfs8j9nW1w3ycc2sDzZA5kGOJcBPRJbvPMy3Px3ImElDjFPb&X-Amz-Signature=f29fe25310035edfd7a06c6d5bedff4e0465ea89724b045d337ae4da8c24cfd4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

