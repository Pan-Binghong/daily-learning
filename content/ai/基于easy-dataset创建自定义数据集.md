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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQLUYTNN%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuugkIV9mT%2FZ9g4ApTseMXytWh4yLASwLAhl2Tlb4cwQIhAOL3HwHTZ4m71FPZze1ww96mfe7GPJQQJAZMDyZI552WKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxglEFiOPC3VI0AdG0q3AOh9qY8WmWP3AHz%2FiN1kxlOyBC%2FD51tgjY1k6LRibWdEnJY98%2FznEyzBdvm2lkPP5ntNH60%2FjMC1HZlad14SfumtHMi79BEWn%2FZgF1ZYCBhSOIs6gPKC6rTkb1wxwbKRJcf6hhKZpVaU59Y2xz3JyPSx9hULoAgUENQ5F0D9YsubU6rdGzyn7gpqQF5M%2BMXnPBRPDoFDMQl7gr20J92f%2FShAw%2FM8ydLkRS5dQTerZP5cJtDrFVh7Ngd8tcxk4Qb8as31an5CX7jy7gM2RiZzVpfqZQhznKu57pNJVBs0G%2B%2FLvYvdQ2cmw1hMplPgFi2fh8gGGtIN4VLOR7Rqq13zE%2FWwlDACQPd%2Fzr50zUBWZgyNRNK6PM5m0RYpwGe%2Bc8%2FPY7E2SsHgAj06deL2%2FYQ6lQmRnSHiet%2B176%2BYkwpL8JKfb%2F4BSO8YHp6FzX4y%2FcoFB5uCzplIf83xlktkUI32NKnncxrSozXTQsqARz8v%2Bo7zMkjqbo%2BUHVj0tG0PITtBhaABkt6PNGBW3RWTX0oosvjIVa%2FY7TcUUcItQv73NjbXryBWJQ26VcO0T27GP8Sbtm8aKYXFhvL4d3jeQAPrlaCMaD49JLHZcWJeC0Y3ZOGNIVeACA3aQyz8TUCjjDmnMfKBjqkAX6x7%2B8wWLwD3d2TRxNjivNd3vtlg7JAPNXe8jJuChfMseJ1vk1G3RQSG6NEMKPnmMWRw9QxjR6m0qlSKXF5Dpx61%2BLmFE0Yx5g%2FZ3ZGAwRDQD3WQmtVPk8Ia%2BMufaiIehH%2BHL0joTF7dytQvf6c2fWz1eawBGFrTtZJUBSgJZVBp66kzr8DgcTANHp4W7ptXeHZODOtRcOScELpB%2FwKpGTfq8BQ&X-Amz-Signature=c298f408b948947c251a94b1e54a0c7752041ab87246a169a5e8ad6961b578fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

