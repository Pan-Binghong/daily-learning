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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USBNAJDA%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAVvHQ86OmbuAGHfRwuAU0RgluTidxL%2BzZ0tfhuPp0PcAiEA9ksT1dmr7BXAwIvAG9XDhczfOgPfkXOyJV2c9uz7h28qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4lRYryb9aA%2F1H9rircA%2Fjrs8IPF7CbXRzwhvf1IXSATWpkhC%2BUwqv%2FvMPHe1sy2JYjL9AYI9TxmHBZ8JnGHkVc9kta5P%2BM%2FMDuSDGB4qQt7DNh9rlZiglvPVEYGgfwYw9fsbPjSCtGTbytlebZ%2B97c07oUdt3MZDb6A3SvR0NWmXuibWEmz%2BK%2FvlnP0CtSw1eQYbwcwj2rMS7Ae1ARfDb21%2FUvKyd18exWfhWgTf1zSFg7vwAlfQ7FutUJB%2F%2FXDahErQMlBZYHRqFF1Jkahl3R4Z%2BKrmI6aQc2NLdyfMBmzkd4UsdQOi4ntDRRG7MVZdYFGcsfeuXuxjXwD2G6ngTU9PxFC7ZKe7e0dMOkkPhPIc%2BczsFowKHIxWPCeZ0sxNzWt%2B0UFRPcoqYt2Md5n2VYFC3EosnCxcK7cqFxFYCtV%2ByL%2FFEvUm8%2BJ%2BSofrYN2AOt%2BASfCExnxf%2Fzo5LYcH2mfMqmTiv9GB1KRh7zk%2Bwb8S7lcjI7C%2Bw%2Bq1Kur3mW1z4lCUrmXXNYIY6z2KT5Glt22wPR0fuFvZ%2BMMBqKcLzhQrWnhYFCTDSTtVsXKqpvyXUiscKgznt2gxN%2BpCP%2BLtcDlur4txtwUKrzXdVBSRU5VEXm6zjR8%2B5cEkGUlF7e%2FEitil%2FcOWgwW6HZMNaY78gGOqUBQrfG61%2BJyVKsEC680DL1Vus0wG1rPfbgGh5SeY3FvhMjqf%2Bc%2FnTxNp1neNtIak26MSChF%2BLjQLdsCRkATIHGyQpampuZjpcAbKNasjYrfph4IM5Q7IfVAu0IHdZXVQb6HXJvqqUWUpZk6ZOXqiROQejEiEyR7ycmehQiVRVcf8CKo5TsDg%2BszIypsF%2FbrSWqr0ZHliUeE7GT9ZabsTLLK49%2BR1ku&X-Amz-Signature=6f118c77c630ec6a2a071887af8873e1416b58510e4452530f4f98f475f00304&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

