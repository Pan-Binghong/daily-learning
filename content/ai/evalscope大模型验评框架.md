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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662X5E5EX5%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDEFu4mn5BO7HpH0YMWiKUiCKdIS9A5f6jO2EgKylIsCAiBcVYP7bp9vZYuUQ8eeMiCDHHvt1upCYsfHSFGm6mRipSqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQlc5JAl%2BdWTRZvovKtwDHrHFWS49DFXWZJzJLBLqEqZYF2qMZBZe7lWtqVRnVKVfBImwlSU36XvpsAOQXRy40ryo9ijVsIAdJSGxckHhHlPUg1fzH5NGFRb2nZ9%2Bq6ZpBdXWEWm9j4MH1JwrfFEkzjR026frxp0Untfvvt%2Bk2Vy%2FatONueof3UqZ43X4puKcM4LY7EFjJ%2FIVzcxTONh5%2BKOyXqsb1ZJkTjPUz%2FCWfhEKH0ashYnDBG5SGv0noWQw%2BqhBjCwWVkJJyQugWWMUlRTS8gmvWtjZrOBpkwZ2cT%2Fyh1lawlCJkd5%2FaJC3nGWdxQrDsHciOU3U8jXU9mJFgYeA7oHx%2FBaqqarzbEquxrGl0AqJbSyjHWAFkzPcyfvkRcLpy53dRAqEMQQTNw3x0ZSOiv%2FMtNYvzmCi8QbrRYi1EzRNP9wHvPYUbWmqgaalFm2ocrN0JfyPZ6K3pMDIbxPjlC%2FhBs1ptFv0norq6hIKaC755%2B8PSXgrDdosY5FGualDo3IwxvJMsNqH3DoLowA2bIETObwxUdwuB81NLkaiwTahEgBILn3ahkYQjDh0lP6C9rFmy28a8H%2FOKGIuUB0f6Thh96Gfj%2F3BndXiFuipcvLwLszZ0XQpgXOqQG%2FzFVx%2FjLwmC7XSiJsw%2BJmpyQY6pgFyIdNwkUAzCG9JCfYMeCik4Tfe9D6QVRy9dWvirnfK8REJBOYXZpBZz8oZNOyWuqU1e%2B0n1ogRY5dn8bPoUJ3v8zsp%2BeLr9AcoywIFJny5X2gfwA4vJRmDPNFOCxO6IyothitNfPJGNbm%2B3AEh%2B8uHRo2yTBkpNVvyO%2FBbsSyGb3c2gdS5ipHtJVyaRHVA0fcRS5z%2Bs0OAbEMEtYT%2FwDTpImoIYKqs&X-Amz-Signature=768941854c3bce574a82ae31d581fbe556b323397274b99a62190df9cf66810d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



