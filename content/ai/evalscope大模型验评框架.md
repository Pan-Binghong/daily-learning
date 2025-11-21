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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WXCVYOB%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQDYUjtQZlH%2B7lmIz9BYJwRJyazevaAnGRvivozKsC%2FrUgIgGAvsQqs7oxvWVANDFqIwFNoJonob4pFhRK9bYzntxQ0q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDA7cWUWgo7c7WuT4wSrcA0P1s3o7EDiKTOiW2BobtkYcnnstN5Lygvu5z%2B%2BW3u%2F7oI0PELUSswlOnD%2BVz%2BMOGmmuS%2BBT2WjcQfcP9zmxRY7kQdrxNp9gS013Efdoyw0yWbnVSbeF4ibUNnzJFQcz4XA%2BXGB95Vp3fFo0EUu9WnjHH4nyTdZiQt44LPyYc8G3WW2P9k9sJ3ns0lYDapC6No1op0WHfO93tWhBn7d67T0Y3Tlc8zCrwW11%2FNb7tzqLlMA7pcB%2BMYzPGb0%2B6APzJ7MhI9Y61StaJdiz3IEpVVgQ8QXvdBJK7oEP2WCXAluUr8I2PbVUkYJX7cN1JeknX9rKtsbusJdkAWys66pBpC4wZQYZbyLal3%2BlneAu4S3GttNZ5pmpy185kaZg0ckmKwwIzcgAOpTA%2F5OJkVP5eoESkVgdZkD1ARVopWSE8yK1ptBhpvYgcAXsKRCZ60RDPCgidcCpSMlMl0DRGSEmJernsVPRxkLDsec1s1ntVj7EcLK6j0H92vgcdv1BzOG94DLDcojLl7BxWG08Jrh6L37%2Bt9fDaqMnmMBO%2Fy5BIrr60heYTfEUz3x2wDWALbaBI0UgBeRmmXrvHFmjZcgLWQ3BpRUb11vyPyJQAdfQmnLwsdgd18rH%2Fh8f98dCMLef%2F8gGOqUBw6waYTgtmzsJa7JI6Nu%2BlJ8kb4pM2tRZc0%2BUlGbZcrRh97n7Fm7cKfm0vVHGmsGUOP%2F1ABjulpmJzioDVMay7DtTKP9kl22ajkWnQcqhYdYkaQ1eLpRoQ%2BFtZuPctPVi6WjxzA03d%2Fp%2BUlv5R0BJs8Ri07BRuGS%2BfJRqf5cNS86Yb4YlpZWQ9tPaYdcVUqu0HzeHPL8Y3axtNkirkEpcW6n6iq45&X-Amz-Signature=3aca4785f4ce8be9929933464a1bbf7d784321e1014a850f9cc491cbc5eda2d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



