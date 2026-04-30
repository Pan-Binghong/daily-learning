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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5X4FJTX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIEyV%2Bzb7LH%2FMmqA8frsndOhMxRCD0XZlGlh%2Ffdf71kxgAiEAqBegoNoSv7T3LrtV9u2lLwASN%2FU8dyz%2FPYSTEZOJ6s4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDPEJc1J4IstZ7Y61VSrcA9li4cDc1MI0BR7dyPdvlAgP2mEp%2BdkYabpV3SK3squhCJi0zlyMO9Q8BkWFGHO7yWw9SBMv3kdHKCQlz3CXGEph9WZJwnnWY6Po9dZG3ghukMnp0JUutMB%2BMlE7%2F212%2BYwQL59GPhGFx9ZHk%2F27N7w8DMsZxcOuNt5dT2oc1vH2Vq3xwQ7tn7rpnhO9xbjDV9VH3s3MjmE%2BwlAPCSeA0x%2BEfXb3kTFVoIbN6cW0WU6NQUMK9XGDfkdnIF%2FpELoZGMEn%2FpQFdpQQcw%2FCjq2dGCz8b5fwxBMDoSkRSoUBS%2B1bu6kvMZwut%2F8CLDWxjhw3GZjeYioqCFh1aUNJ2qyt4lrAHlYJXyJ4HBa2cM%2BYAe0ZAwpXkZZYZvGrKsMurWnkAQnW5QkInG8GjPx3Jc4yTEjRGfk2ckxaEDSkf8w7WJBIdV3W9tlgrMElQm19305y3b6i3%2Fi8WkohNURF3awTjKUEg0bWEVUMOkbQ1xgFpCgn0a781AzBbeaAuA6mtvjJQf9TudlcVJ3k8Dzao7HT2B8cQEvOPA0EIAIpSe5vEqSSNfzAwGz4bLD70q%2B%2B2yhb7tXyTQiuXuJvgHNlwlHqWnsv7%2FwNjLgU9Q4ZhF1mavdDARwxyUz4LyMmQryTMLCdzM8GOqUBEIFzPMzCC89AGMbEx%2BXT%2BprSfgdsjkyo9uH25xcZvuS2hAT4tZvf3Le%2FXRbne47UE%2BCNrBtoRKTFrxuO61BVlBOURmYaOTH68MogJzKHKIxTUXqDjhg0N0VdBXhEJGbY0twrKCGGoxvkKCbmQk4r4g33UJDbP2awsMe5F%2Fao3ZaytBJ6CDH87ubOOsPZK6LzRmwpNYxuFM7uBNIsL86eW5JZT%2FlB&X-Amz-Signature=8c545f60fbccf3a9b2161b680998ee289011e1eadb69b9e9c52608fdbb5230a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



