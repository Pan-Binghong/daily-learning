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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YK3HS26P%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI0UWr2n0M1iSwkPrWRNcT7%2B0lBlErZ5ujZjD4bQsrHQIgGIwptG6Oo8J0R9fC%2FxPJRD6sav%2Bt6f6v9xvJqPT1tXUqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD7AaoFG15YeJOpORCrcA%2BwVTcJscudkg7qcMPcsEb3vB%2BowYkQ0%2F1tCKzwGyCkN51WF1qx0nn6Xv0zkmSmeVALnPzHmTqhDQ14nyQVLDy8TywJiteaDFOz4eKgFGZG08MmwtcVLkCstgqYc0WM3cQ5SUvAucfIWCAOrJDZ8iGr1nIW63rXAKj3%2Be02DeIhu%2Bvgu%2BYTTgi4qyd2au2nHue9kbWAGpsLyGZuVfqHwdVes3JgD4fbT3zU6TlWXE9gTQrW0TFYjl%2BI%2FSbMWK60tLRDvI2eKw5Yh93lcFvGJKt1TsSDxfLApVj5C8iLHK8PStEIHwn9P6Z%2Bmfli82Q2raiiiE2waBhuetBJCfUhf8y%2BVEOx2i1yJwOojcOq48CWUFauAEcIbtlC1xurHKlEawofrazgfMlZsqLjmp8Z6bMhrpkdAEfX5txHpXyqpcJcinqYFMk4UDl%2FhQcxSzNIq2tCTJQzGUEDrMZl%2FRGw%2Bg%2BFLTozCBALoH8K8Trq9ZXyipnrGFrUHHa23HW7Fmtiq5ZSsy53SjA%2BjA4QTM%2FM6ITmJ4wiPRMuLGnEfWD3MVl1twZDjVL7pkS5%2FH2uSGN0crbK9npPu%2FhItDpzO8m4ruMZJ%2BM5JHZtWhozefjfmdf%2F%2F51rDfM4HAX0L9Z6gMK2FmMoGOqUBK8%2FyMxFejanRxFDAoa%2Bi48kFJ4AUs4flor9YsHTF%2B8afB5E0bVNa6jjos%2FOl0M0jO4yMWWuwysdr4%2F9f0%2BA%2B8PLmBM%2B6J3pjZWcsk%2BPdfCOheaXJe2jUKZv0Aqvu4ZN8ITyNiyuyTSGTS48iw9ulrnHq4%2BDGHAxPcTlLMUI27pByS4yT96BFlnQmq%2FKNCa7JZ7stCO%2FJt%2BpW4hm42ekQmgmPG8dB&X-Amz-Signature=7fb37463b84608ef4d7d7251e2d95dfc2558b31e3d300ed712760b0f74bac41d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



