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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJO2MJP%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJIMEYCIQDLlYemtsFU1WcGX8o9CWFFQpUihGBTAyIejDYg%2FvMxMAIhAOaj8Fz5QzX5QEJJaBZpGgT3bgl8LpRbXDbnq7kG5kb8KogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWTDqs47dBkf3HRTgq3ANKvk19n5b6a2Qg0W%2FMJ79RuH4OnU%2FfPfbhctzYvlruuMDBAM7zWYMKaI31jtBjJYLvgWU36wgakzLCQqyu6wrEx9KU4%2FFjreQvxvP%2BlK0PmYuJ28ldBa%2BQ9yraWkRtJJFLwaZc%2FHSDrL5v5pXTC9xwLB0MHA%2Fv7UblC9wV9cDsAYExukJQQVBP5cepXGfsu7iJnGc4ZOa%2FjHm%2F9fesSOeRyquxMdhu0XXZbPUHpxrzrBGVBAcmWATrAXeLsLLqVW73CMQJeGAqcGymnjQ9Td8pVNCX8Mp7NJIn%2Fi%2BtTULRTson92S2TaZ2gGREcJGoD7QVAQdhj6MI5f2L2VRK9QAxSBUxuR7kb4Mc05rs8UmsWngotWr5fx6RVhz9uWwtfsV%2B9n5fyBFhbzWscCJJjUUE8oRqdZp6mD%2Bk65yzCgej9NXlj%2B4v0KtIkWQ6842Z8iRsro5yvK8Pg02ibe8ojySGo8jqEn0Yn5IEgCXgrrW%2B79sx103HsiRrfIDBoQxJf1Q%2BHe5It8ullFJ7mgKq%2Bt6UM9%2BlAWSiDUStsjEcnByNZ6ZSKtFvshStbMyhVAXB20jT5qlhFwztkmdhPPTx9VKx7oya8jLvheeT65%2FjzLon6p0Nm58l0UoT8bTJ8DCgz6jNBjqkAfi%2F6q9ZOlmkZjxXdu7Rd6UDSTP12mQvbCO5WCJ7IeytTWyb9I7L0yPd3UFK2WRMUhLhBZBfA%2Bk0F6e0KJ4rJW1h4J0vXbrLTEm1zs49dr%2Fzee6oPgQCkX4sbBLr0gKd%2BCI0o362k3O5rMq0uwPxOi%2Bu7CYxRerIAeB8g%2FSkHGtvBNpaMUGMUu3V2pStZ0bjntVKfvfcRTzOKWGSqp3Hxg4h4w8A&X-Amz-Signature=dd415bf6674453f6c4398bcf2851af5d3b55e4d2afef586996fae6436b3054ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



