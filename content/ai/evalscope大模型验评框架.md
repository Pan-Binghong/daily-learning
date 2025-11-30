---
title: EvalScope大模型验评框架
date: '2025-03-28T01:13:00.000Z'
lastmod: '2025-04-21T02:58:00.000Z'
draft: false
tags:
- LLMs
- Eval
categories:
- AI
---

> 💡 之前都是使用vllm或者sglang官方提供的benchmark脚本，现在尝试更换为EvalScope框架。记录使用该框架对速度进行基准测试全流程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3VSOMF5%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIAEtF98NBn51d8Gl0EaSN4rnM%2BMng5SyMZMi9obkxvMmAiEAwoK%2FJXxJDM8sIvNomyay9r9b0sKtjgQyHD83ZumwFCMqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAdBgZkTbm8LxS2v3SrcA0rEEmFxUhxjo6iuiVEk6srEmDdyKz56miOW8itoAVHoJ%2F9S%2BJw0Ctd2JQgmiT5cbuLyYirkjYPxAxy3HtVJpRfl%2FhRglWOSxBQq2aImM4Z1QGbZi9e7txiLe1xf74m5gCCudIOE9oKmgE%2FQ3JnDowMTHZnNb8F6lcQWmDYpUO6pTqBhr11XZJw2B2ZZ9wQBpq%2Bj3eyqSM8zHjfEdUcMcppS3kYg7Xvr%2BOKvp7j1uei3B7xJQw%2BdOPCP6QnG8pJ5OIr8zj1O7p4eV60%2FB1eN3HD%2Ft%2FUK%2B5N2%2FVKte6VyL3yxIU7dC%2BrwyvEtTpN4T9noNVaXpaPz9Lb1i%2FoKhoYkGC2HTnq5OOFBu6IQ%2BuTImHowo2d%2FQ00gx4%2BS5JcTDpBzBXnZjJzI0Tro8Vr6fjAYPIx2Q4m2v8HLVbuYQfqLE%2B0uCGNAx70yARix%2BtZHiTV0k1tnnh6cPcQ3FkVQNMU1RnRA5Urm0L6txAXsNeMlnkmG8MiEB7nCadUKJRa%2FEqb8ZCwz24w3yNQroId73Zwph%2F6i5%2FCQGB6kI8Qjw75VF2umg33LV4mLxZcCo7fShZU%2FWBU80mx%2F6W%2B18a5FLLNB4qDpQV1xK07%2B5T1qARvto8HBQAbkIqEnCjr%2BNJSoMMLbrckGOqUBQtGK6r9yFgfHTnSOiL79KZKA061bH0792w4qIbrcDPJEIplBFT35QlHoE%2B%2BQlIIfSViFki3vWkiJNFFQygriaDzbMjUyutFlXlVWelkBUVcF8H8jubwisiSc7x80OfPaJeM0WVTfox5jMjpK4zfJ6i3jd1guBDNdQoimf3G5tDytYr6WuyXpKS95m2gyxlyvasnjQfydAzGld6kmDGgGUxFf4Oni&X-Amz-Signature=3adb500c6eec5b826709077566091706de9141b1ad2a1216521b0f6f856f618b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 1. 安装

官方提供3种安装方式，1.pip/2.source code/3.docker。

## Pip安装

1. 更新pip
1. pip安装
---

## 源码安装 | 推荐

1. 下载代码
1. 编译
---

## Docker安装

https://modelscope.cn/docs/intro/environment-setup#%E6%9C%80%E6%96%B0%E9%95%9C%E5%83%8F

1. 拉取镜像
1. 创建容器
---

# 2. 运行模型推理性能压测

参数详细说明：https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/parameters.html 

推理性能测试有2种策略，第一种为标准的并发压力测试，第二种为单并发下的速度测试。在该框架下，特别说明了如果需要使用速度测试，则url需要设置为/v1/completions。https://evalscope.readthedocs.io/zh-cn/latest/user_guides/stress_test/speed_benchmark.html

## 命令行方式启动

```bash
# eval.sh
CUDA_VISIBLE_DEVICES=0,1,2,3 \
evalscope perf \
--parallel 20 \
--model /data/DeepSeek-R1-Distill-Llama-70B \
--url http://127.0.0.1:8000/v1/chat/completions \
--port 8000 \
--api local_vllm \
--dataset random \
--max-tokens 640 \
--prefix-length 64 \
--min-prompt-length 32 \
--max-prompt-length 64 \
--number 100 \
--tokenizer-path /data/DeepSeek-R1-Distill-Llama-70B \
--stream \

# 为了截图，暂先取消设置该参数
#--debug 
```

<details><summary>测试长截图</summary>

</details>

---

# 3. 可视化

1. 安装wandb依赖包
1. 注册 + 获取密钥
1. 运行命令后追加
1. 结果展示
<details><summary>截图</summary>

</details>

---

# 4. 测评模型能力

1. 首先将模型启动，使用vllm框架进行启动：vllm serve /data/DeepSeek-R1-Distill-Qwen-7B --tensor-parallel-size 2
1. 运行以上命令后，会在当前目录下输出一个output文件夹，其中保存着日志文件。可以将日志路径保存。
1. 终端输入：
1. 访问本地的7860端口：
---

> References



