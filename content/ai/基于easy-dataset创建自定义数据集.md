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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FDHMRD3%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIQCOLr2EwzK3tM%2FlIt3RB8slJMiA3eIpz1Fj5PU6r1ZXUAIgbryzeNz9ijbrTHMgCsJxnFUSs36giZv%2BOWQW6hfeYqMqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHeYgueGtCp26Q05CCrcAyFXmMGpawsDQSZlrvDQv0rp1BKNhatwgnQFpelaYqT6gdnD9RA76QDlQvLAGgAveOIeBS9GCY5ljYEB8hMbfKi5bQ8FunVyejQEGwvNbuvqbC6Zo9ksuvD0nATKffH%2FAEdocfdpD6Fn3SSYuShajzt1kBudLz7o3B4tcWEhRdP8CuGmNjLEfPVvZIhufT8uF9JmDrvFMPoq6iF5wYqBEyeDThWYeuhefxkyqTi1PiJnpABRlsvdelqKNu0ltcOx%2BA83aL1w%2BpXeFxa31oV4lm6Ivt9M%2ByDgU9k68LCn6SVeIZehnY9nWzK5EkKAErCzm%2BK23aysIjiPgaYXfVS%2FrU64Ng9ynfxV4sgtUOcNzmLohaP4lDyPBd%2B5ORZN%2BI8g2mlFzBV7RnkRn2tpBrx%2F1QHyzCy8XJMqt9U3m83D9QioE61LhvolkRNf8eG5Ke3G7C%2FVW9%2BHI2kihrIMdrJ7OH7Glo2xa6fKnHlivt7WJeStBpO72hJRdpoeXggizz02te1EXPmXc9KO2LUa9YJSY9u5sUA7RLab7b3cPev4sx%2B387rsGT5n2muciHHaPCpSfjg70%2F3AuVWqdhhqorJXK7Uq%2BtN0%2FzXoVfaCvKNf38UYfGHaxAzbZnXQGeOqMJX3sskGOqUB%2B9ztM10FfkvX6%2FPOL%2FaxpqG9TyA40o8qQi4NSXad07r8ne2PSz9sOuvSxnBiz660DhmKstDpberbO3pIvjLgE76gQoC8TOKPIPtC1aV9ZoP3rmZFShM9548Hf7KHyFBkbOdjHndDHWfnjIJLZ2gGQC2zZmu4Q27gMU6UB0EKyu%2FLW9MXbVYYQlCzB2yeSuRrsoIZHn1NCbPsc3mv4RIpqFpBqGOQ&X-Amz-Signature=276d60c349495149e25a5e197167e60407099e5c505489ae1d81eacd0c3b39bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

