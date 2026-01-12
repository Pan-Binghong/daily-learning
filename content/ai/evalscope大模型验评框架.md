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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLL4ALGE%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDWSRgHeJTYBgveLXziElpwspBBgCx%2BRN9t%2Fri0fttk7gIgX3%2FiO7ipl7QzkHPi72j%2FEKEgitUAUJ5EWMBoLn5ICKYqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLATpCF24w95rlsHSrcA0ubdm2c7j%2Fj1JJG0OicYKaSzDK8GLPOycOvw1vc5WHRj83tmwMQF%2Br%2BrgcYdymoEL3cONAqRIADqvjEX3a4W1Ot571%2BfJ1n7k4%2B0cZLJUnuIpv6UyffcG8rA%2FMhQBWKDuMnqP4PBLd1dDvRfPxf%2BCnM6GXPy4CL4YamysAU8xQrE9OscWNeAt4TxpBgLdKOcZvcAf%2Bn2op3nmUQpLrXbf8dTjMUEJw%2BpD3%2F4%2FS7ZvF4fICJ6m%2F0vuYauVLjojpmF%2Bcbrh1R%2FVg7pAbr1p1LO2azqIf7RTpv2DLN5FLHS0UOTnBvJaEExH5wmWVLNGvKWg5NFPEec%2F6iXHzp4V8JBw931VmqQXstS3uOw%2FrQpE8I78aG0ackhHJGW1subqp4gRip59GmLxQIVttWOUabnZUjmaJrEzJdhzYOTOTgR%2BvNsDXPm05YWhym6ORts6K9RjaPSSP9dKjVS%2BPj7U9mJn8gFp1zkEZZ7LM9d6maDsMqw0AD1JUNhJZ9ZAiOGdc5XVhgwplMGC3JWpfQpGTEvondCO%2BOc1XO8eXOqThvOXI8DDGMb1WHgHRkbit1LCUzQYwQaTkbXZlxOT4IdTp%2B9%2FUzBzrp3S9VDPQqnm2DGtPGp0F3MGkX4Z0NdBbbMOH3kMsGOqUByMkwrlBg4T9Nt9HMm3g0IgT%2Bdu7l7zxzGOnvcACbPfcGMT7p7ZMTKEoX%2FNegwjLEg7lX5l2G33Zy7b%2FDfmNr07wyRO5KlurmhG4HNi6IxiihLvHVnNlrDakj1MejJWDzUoCU%2FNCzbx64ECHE3nDAnicZcEoXSvC9eCtTsFMdaHZhvJFZOl7WeIQq62AGwzK0aw3p%2BMm4pqsaf5POxwKJ0xo7wWhr&X-Amz-Signature=cb6cb3cbc672363ce4383a5b7806726a79bc9a0bd2dc18b4227f4b0f034ab92f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



