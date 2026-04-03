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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZGQO2IF%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGUa2bxBlgmEuSta02ZUDl6HAWSfqd%2FURWgLz2fTVbKoAiBnFMGlGqi43ReYsNEzrPCjKVszXhMb7hGY6gr%2BFr9LBCr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMskV9BHPQULrxpexGKtwD2qxnlS9p5cpEpbjkjk2k%2BvDgxyIoZ1kFMdtPdpSAJCSx1r9cspgXRfuAthfGXdkSFHs0oQseE2Djp2jQwS6IZcBY3GPo8oiWQPtmJzazUrtJ%2FwH7G7jYmaBLvzX3b%2BUDQxpRCAFzKjr%2BJEHFx0fvBXhQm6vT%2FT942iWWHDUYfcnPwoAk42YPFxdwMBcslpXdYDi6WVBeB%2B9%2FhKPFgukAw5wT8l2vaewPAbTIaBBGZwTiZQjy36qA5lI3hS9%2Bo5GdMPpVY1gip0hmLYK%2BRfisU%2BtwVLgo64Mqce17WD%2BDLF3qmVIBGAnsnDjAVDBAZiulehi3VwLhJ8%2BXdo20k3KJ2id%2FUjwUGfwG7kyduEOPFkYA2TVw%2BnL2CJ0x4pLToujYWEZmH7gyxx3JBWQegmiTKvsffXKC2WN8yGF3Z%2F0qXQpga%2FtYUVQ0JA6KMye2mJFWPq5uqitNVgvqWBUQ%2Fqlucy7JPKWAWkWV5d%2FLmzMV%2FB34qrbs8gA8C%2BxOFo%2FnEAQwmjfc9m%2FjPesJT7N%2FtgMqCzc9k4DAGD%2F%2FdHKut04K86OlyL38zAZOkL38zLUT4vDsJfM1tiFiNa5l0abeB18VLhx93ZQ1gLZYqndL5QiPl4YvRf92%2BKKjW9CnkwQwoq29zgY6pgE3TC3bFqJOGQ6rwXV5QC3eISt2nWu7PbcHhNaYyTNUU0zXfviKCXF%2BR%2FQYL0dag94C42f2NPeoVzyn0GiRUrARsWCePTgfjIOOiQa0J7GR0KgZLijwyTqJFfn0SmUZP4xCmNM22UbUjRRpv0clm7pcZ5LAlSMlrdU8b0HxUQfFQvi3FSCb6mqg0PBzQ5Xx0%2FLt4mFYXZ7mxpSOglNlDHUQc4MVfNQ2&X-Amz-Signature=977e1cadd5e93ac1850a5a767c8bee4bcf747a87a9953df72aaf22f71fd930ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



