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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZB6BBXPS%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIAZ%2F%2BwI7UTSNwk%2B37PGWw9D%2FvFrEmZiJKvP29OjnHnwYAiByV%2Fd5Kp1o8N6Lv7jxOrHsMGqXTOlnNNZ84bp4ArT6Rir%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMQpKmJyJBnHkoN8p7KtwDu1T%2Bx4BlRvdqNJj0O9cBAC%2BKac1RaRnLFlNwhLNBow4KBtAmyryDRGX67mZ8OB%2B712WVGjzwtWAxOuQyh6rmE%2BdvlENjce8TSMX%2BJ%2Bhe8TCcq9bsWXJvaJuvnvZTCPA265xXzTroUiGpE0jjdNLnPf%2Bx8NLWeFvfNjKdtHA4r69Mi5F%2B7UF5RopTuKAyJhtvQj41PSdkZtFYkJwZJoBck4E1ApyvkQdE1zEhYEHRBqXjvOlawJZHDHHMZl%2FsUfojkH2SEH8I1ZbGI2rgVOZBQJtKWRYhUeerDPC8%2F5G%2FmXYRVYHwBcj3lA7tvtrQFGHPzlviBoqvQvn7QJZ7CeyOLERsRNJp0bPePcKU0%2F6Bc8Vf7dXzdh575jg9Smz8IR4QZlAHxgak4brZTn3idHHhaAPRBN58873XEgL7mVQB52TVXbuO5asAwXzYrnSF4qAgy3ICRbX6OIBK72CsRKE3qSHiuX2h879B%2BZjU7zVXEPjYRdpSX1GqUrv%2FGE97pPT%2Bw1CDqs45TfyHIr23k4Us6l%2FH5zdHvk%2BD9pqpA66fRKxMOK2BVRhZMwvfjRHbkDyAPn7BM%2Fb7C0b6KbJ5aaXb7s0mLbVZBmvJu7Uw%2F7TgmiH%2FoIsjpdhB7yNP4TAwsL7KyAY6pgE17sbqmj2Fjwpye1RqP2D6KlZsVxxXIEnvmshIiYD%2FiXzNSgocdZQtB3BihJRbVN3X%2F%2BIQMDVpgcIM2pCL3T7HzXQ4eETCRggXri0wTjS3yc%2F7TVT7Z1YkONkEtqx6Didzaop%2F2Q3jtt3K7mojNrKyV7xrMee1OqPgKvYo8B8dq7uKFs%2FY1NrISgRj79q1j6ZpOalIpY0rLDmi4r8pYab6Rkdpx14%2B&X-Amz-Signature=25012a36b8c5dd6f78449cad2e4995019f13a54bb1903dcfd31a882db7c98776&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

