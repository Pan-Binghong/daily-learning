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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IN6N7VC%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICZoPZC1SKlGpQyrZkcCCIxuFmvBhmhsnz9TPG0Wyu22AiEAtVfuVZt0jpIAefqqLTuNrg25BXbkhHJZzDzOnjhmROMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIEPr39XgIRKTkIVircA4wgtrFX2axSLAbdW7vu1uAzahU302mkxqN5yyHjjHDyd3utV%2FxSRoc1CEJbEeHO1afPXiqVMGfmZz2iLPSZRfRrb%2FHrOSxEhk0P50upYUvj36gJyV%2FECsXlvFlIux24O8bqdDLMC3QO46G2HBt9wzPC75MwOT3jEBanLUukKq%2F0dfBfn%2BDJKuCxoc3Mb65Z1BQ8Djgeh2wIWD2ErX9RoQTS1uDSGsfPevgmmiKHGCcNExWl3wNCBwhLRIQO8Nx7mAwFJJXf9dZv7L6ZQPDI%2BXzGoQN34FhY8vddcihXg2uh0H9eLv49n2vtiyJO66os52zazVx%2FV7Z%2BZyCfi6NgkXlXspeb9cltC1CVFCmL5mLLAABkbRgy9xc2CfaLoeUaZS3opUpPUmrX5T5aW4SUVxcapJ7tKtDM8egIYiGBqerEwOD7Za73rJ2LnmVGX4sVAADUN0DQFAjpDurOVMMcUBEZdWp%2Fq2RLcQXqILebJeL%2FVylFOgFdBdYx4hd0M7JfFIZAfNe2d6%2FZu%2Fsqq5I23qDufIWpUU%2B2UvFZLmd28n0RDIm7uJ1TnkFr1XFg7s9ss9tLWi%2BjDqPysvIwnsb8YAa28M47dU7mLqbk0f1vx10Ji4Hc95fTd9pL5KcjMODEgcsGOqUB6GlkDgShA7V1T2ArA9GyV%2BAFgSAAEBm2Z2Sp9X1fmDDvIWUlShxBhhDu%2FhUstvnIJfpvbsg82jF0Ulnf3gkKZOLZiCQImFgsJWYiDEGlU4RR5%2FpXLtOl5oFNFLnXDdD8b5WFcymQva093UwBEWYV8V1BjQI8ZsGXoSpiGYZPEVw3cSCErG3il4BRDB10FbcT4ki9MKONSPQz5RDVwJZvFf3atv%2Bz&X-Amz-Signature=55688baee08b230749af72ddb2864f9132eb9b92b71e4831f4ab636f930c18da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

