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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YD6FUOY%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFWxU5WUTmA3eIUwJ8Tmb3WLcySRKKAr%2FgtsMWKmqa%2FZAiEA4AW%2BsgG81cc%2F%2BogZDbsmEOun3ys1qWMu7AEjTzFW5w4qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXju%2BpIcb7GM97EMCrcAzYUgAaenKjU5vCIbJP4YgpebZyW9rupMp%2F7QVyLatssL9UTpKCZ%2ByzmqU%2ByIDJ1CsGKk6jTlSiN3MamKH8jExWLeFEsog%2Bh8hftPBLB8rqcTk3rVk9rJZlL7jf0p0cvEU3fAj88LkA7V%2BPbwNxuAfFPk2eHHMpPGiNC%2F3MFIiO%2B%2FBae8f7PYgo9kphPZCqD0D5oGlpmiS75FkhX9njMBoDl1WS8XQbkLvbevJaiLoTneCYYWWlpmj4L70msuN7CM%2FFlvJguHPknnVwuPrLnOo4oEXl8OqIthMU%2FYa9dfda9u%2BAnTvQIf6A5ygPKavp6BDYEKUb76KyHDfnA%2BIl4cdbY2%2BG4hA3z3%2BdbZ4WaGiqAUZCCYemIxHMXTDAOilnMEo%2BUxCGN4PbCYrFesDqbGUyV6YZWWgCnvMQ2fXIh7gEUjhyWzgUYwPdNVl5QyaTyqwwFsbHlqjgg23xDZUV3NrekplbOrmlwgfP7znWjygsiI8%2Bm%2Fcl4v7u5hAg6%2FbPXRMoYGDiVjG8HLvgmt8ttm5s0gIerF8fFjylnbgTxXxyeWd63xnM20%2F%2BhLCgRfqwPZ4d%2B2yOWKH7uHu8ncx%2BUMZzykw1m3%2Bfeq9ED18%2BP3ToIHaIIl%2FBKN48ODyEbMLGdx84GOqUBbHp2TrQZeEnvcLVsqscEotfbFNw7CbB8jaEg2NQQkJpMgtOaPohDfDwlZatNMJ290t5Zn9d7lQ6hCZ0p6zX7%2B%2BUyQUZcdUvPnmJ94oExU4NfJjHszNq8j7fZsrTvDHio3wYSSZi%2BV11TXiuw3ndaV%2Feje7hTjQ%2BsSbJA%2B9IAixt%2BqixfIclr4FvQTw5BOhwjWjib2dDaJXNuQYw%2FlU%2BKp%2Be4Ukf9&X-Amz-Signature=e6bc81a69e173ffc7b3ede76097c8bb3641882b50c8a8b75ee8c9148ec5703e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

