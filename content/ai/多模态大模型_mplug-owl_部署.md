---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625KTZ6EW%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHVGL%2BVSIbEamJpSHCMtF5OClWMjeQ69P3hwZ4ygUs7FAiAtvN7of6f0hbR7ZXkjBMzwePai758DIbCiMjAs2e515Sr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMCzWCZBZ3%2FPTJ2K2nKtwD0x7%2Fs1Kyz7awu8zCNQKjGOJmMh5%2B1hpNGe2cHX0B%2BhajpskAUPfbP6diKgG1h2x3sToGwkUekMK8nusfZn%2B6LiEZ8hqRSXzRWbYJ4dKDssbtjGtj48fzMklTSPZdMztnmhj4riYsSbCJ0e5BtiCIG0AKhhTfV55YA6ylCF6836hFWiEPueblwxtPUVCGsGtwkyVH5UTqqm2Nm0mfarjY5Mbsh2YLZ1eXmSVFdkL32BkthF7S%2BSMqtDzzBkyO%2ByJxE5fa1Gk3U2qBLALNbzLdBjHj6%2BB09mrgl4ZeE%2FtL7BNr4zME7AH5J%2F7a1s%2FQ7TBm0hih4aGUx%2FX8HJOB%2F6CQEuskAoKiVSxhv0nudCM6xWfcm45Czu2xwR4HO66L6%2BSdf0pm%2FgJV6OwPqmIz925h0Fq%2F7CQ%2BHzhVn2AQ5I9HJfA2W0rJX3McfED5qg93QLGpQ%2FMC%2BIXEo1%2B7xiKWNtUuel6uhWGjmfiQPcsulr1tL9HrfP1LZrEoQNR4Wd6ea94MoHlgeG4C17wDlpfLZ7ZZDiaIXl3JilaBXEWyGjHeaCADLfAH7xxSWTNhbkuUQ%2FBFIS4avceTg7vGeNXxcZMZFcL8v0PQ8IWf7mWAwnVpIYc%2BpZZPAg%2BH8sOC7YMw1eOCzgY6pgGE%2FeTHot7MCKJUlp6kPvLyH9HlKSJMTq4zcWxxk7iNkJFbUCEnm2zT1hwaE6zRBKQEIxp1rAIDWyhjcMEEkxmr0evMZVywPGlkMkShTHwf7WbsE6PUM6wqpN2YDgGqcjCbTQtedWMMbv2S8%2B2BWwY4Lm07%2BffViiiiets0toVQPTFGDSK%2BrM3PzZ8z%2F3N2hi9fJGwFwNWNFSDkfLe3IpLPlw3fEcUD&X-Amz-Signature=9a4a586f12e8e1b20b948951803deeaf59452d8a3a5a0a33f3ec83669afb7e6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625KTZ6EW%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHVGL%2BVSIbEamJpSHCMtF5OClWMjeQ69P3hwZ4ygUs7FAiAtvN7of6f0hbR7ZXkjBMzwePai758DIbCiMjAs2e515Sr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMCzWCZBZ3%2FPTJ2K2nKtwD0x7%2Fs1Kyz7awu8zCNQKjGOJmMh5%2B1hpNGe2cHX0B%2BhajpskAUPfbP6diKgG1h2x3sToGwkUekMK8nusfZn%2B6LiEZ8hqRSXzRWbYJ4dKDssbtjGtj48fzMklTSPZdMztnmhj4riYsSbCJ0e5BtiCIG0AKhhTfV55YA6ylCF6836hFWiEPueblwxtPUVCGsGtwkyVH5UTqqm2Nm0mfarjY5Mbsh2YLZ1eXmSVFdkL32BkthF7S%2BSMqtDzzBkyO%2ByJxE5fa1Gk3U2qBLALNbzLdBjHj6%2BB09mrgl4ZeE%2FtL7BNr4zME7AH5J%2F7a1s%2FQ7TBm0hih4aGUx%2FX8HJOB%2F6CQEuskAoKiVSxhv0nudCM6xWfcm45Czu2xwR4HO66L6%2BSdf0pm%2FgJV6OwPqmIz925h0Fq%2F7CQ%2BHzhVn2AQ5I9HJfA2W0rJX3McfED5qg93QLGpQ%2FMC%2BIXEo1%2B7xiKWNtUuel6uhWGjmfiQPcsulr1tL9HrfP1LZrEoQNR4Wd6ea94MoHlgeG4C17wDlpfLZ7ZZDiaIXl3JilaBXEWyGjHeaCADLfAH7xxSWTNhbkuUQ%2FBFIS4avceTg7vGeNXxcZMZFcL8v0PQ8IWf7mWAwnVpIYc%2BpZZPAg%2BH8sOC7YMw1eOCzgY6pgGE%2FeTHot7MCKJUlp6kPvLyH9HlKSJMTq4zcWxxk7iNkJFbUCEnm2zT1hwaE6zRBKQEIxp1rAIDWyhjcMEEkxmr0evMZVywPGlkMkShTHwf7WbsE6PUM6wqpN2YDgGqcjCbTQtedWMMbv2S8%2B2BWwY4Lm07%2BffViiiiets0toVQPTFGDSK%2BrM3PzZ8z%2F3N2hi9fJGwFwNWNFSDkfLe3IpLPlw3fEcUD&X-Amz-Signature=34c49107c337b3e4d6603e00eebb313a089c7160fa41b271fa81145aa08d8c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

