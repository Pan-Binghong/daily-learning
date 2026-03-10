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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2HS6DVZ%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCCqm682EffqCQW%2BE6qAsbSCv3O6hkmp0uZGeJeHDOEJQIhAKSfzzF%2FsynnN8u3Uoax%2BPDRzI5zNZyciQI02rLD3E4fKv8DCDwQABoMNjM3NDIzMTgzODA1Igz3E4ziarCnLsiTT28q3AND7YLRHXX1SfQ1ZWBQaIntSn19Q4MqQZbVKr4BgrqWNofsgy8YdmvbrosKHs6I%2FFe78iwLedAbxc2DZj82XGzlC7oKtqjRwYPi6T%2Fizad0Elw60JBpuSLanhKrAtUrBjIJXl1mGzxoaattEuYAGw%2Fgmk4%2BVMcQa5KtvzrjQz07PjTscVxncRuHXmY5Nei42fsPg1yxoy0iE9AZD6UedjDvxK9sa%2B5WU93atkmNB51H1dLdeJgrcJPO2XPeazlYrwrAS6sXy8NT1i75Ky8vrLSIWL5MyauJrezseq3f1so7SNHSxM9M1v6Wexys08T01wvXQguT%2FQGu1HZldd2Kakeef9%2BgNNfH6UzJoPCUyQEatb0y0L%2BskW%2Br4epDItBg5fZvS49l8fNWYAHut1uG46EiNL%2Fvf2ViwsydKvuO3eTO9oJ0f55LjHw7xs9FPLf36fL1rrnw4oSjgm0hy6Xh2tBNpwt4x%2FX5iwJeBGdGANmch%2FRM1D3P36vpGT7uhehldPlLPD8cVDBfPfO2JwdUBiThZs91RDLNJGqPTr8PeLAKni2e5RbzjaohZS9sLzrR1KWM%2FwkNfL4fiFkXivBrX1jTSYRYb9%2BWhAJ7JQENjCGcMvfv6tHPJo6lsgKs0TDLj77NBjqkAZhnzUmXhHHCd7nYqOlAQk9liKtBTAf2pXVyt5%2BO2fq19UKYX5NGBoPaxaXL52Ny70xdiqSE8VKK9f8nNbkNZm4gXmUeb1J0woD%2FfBCND%2BLOwjgni%2BS1xhDFXHXiB9R7ngqm6Vj%2FPUN%2BRm5oGeygT6CFoqPOd0%2B1l7rpJxUMbTEAtOWfHUVNbbCRgX14POLLoZ973QCBtxv2ZpGdPYy0Lle5sQw3&X-Amz-Signature=70404aad8c484677f207d93254d0f608adb8b26ea71b80eaa284080f9a8f57ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

