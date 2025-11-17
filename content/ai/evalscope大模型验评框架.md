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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EBMHS6G%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs7v9lpU6s%2F1uSpMmdsi7B14iWF2ZCrToHvNVOetBOuAIhALLQcTE3EYxTjFKCVDuLbYCmZnZ84cVgnFJdSwJWlcpwKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBAADwXZaMKDGGyYIq3ANsO50sO9oAaUCQ4Z8ERoBt31yn8Ce3wDx%2B0TdJsBhHDQCtRconio4MAC2uUa0%2ByvyDU%2BkHsNM1P9KRe1NxsI2j4aeSGp46QGQEMSZbaV0wqXc0D3cy2juk647szyT3VgdSWIBZhJwTrYpZ8E2pyRNsM52mA8wOjgTEbsEzB2ZEDpoC78W9t%2Fs%2FzQ76tcAtU34KYqnwnVuFn3YQtHcaLzzRNh1MfcOlw72v1%2FWMcvEWb55gLt9npAQ0bnBuLDL%2FhWzuMLzOG7oEB%2FTipGJQwvmXVVWd%2BkVVrW8Re11bTvhrmEc8GXF75rU7nr1Y2r0pcP9mn%2Bn%2B3XS%2FjjertraTwaHVYxjICd3A2yKUs18DgZHFFtwD%2FcnD1DFi6Hfa7vDh6g9w0OvcMU89EteSu2952EM5jX9LrFXl8GEAu%2B6YN%2F%2FLStmMhFMFohFHs%2Bxf%2BppqEO%2BqcI%2B9jzKfDz4DaejBhuwFw0H2aaVyUJESk%2Bg8gvQA3%2BSSx%2Fe4KY1XQxcQViQGu1%2BCx4eryZAYkCLEnzxDeOcMCQ%2FFlo2bZn%2FWZCbsVY5pialL%2Bglf1dCxYTnEY34K9f%2BlR6XhQ7VNIZzgmjjN6DY6WGBcWmDBME6omNWoSV2sqvnMgU79Gz0szqPLyDCkhurIBjqkAZwrVLSM6t0svGkvt4A0Dea%2BWniVIfugO%2Bqg6CUKP32VwsPDiweOOAu5IDsFR5V9DIPtJhY7zf8LbPAkmD3EyTahIki8tv6dlQSMmJjvLTjYrnv%2FAhFunblKJZDlzBnuYjfoYr2ESlSI56xZAr6wQA8ioOEavH0sk7bqvyY3s8AJ%2FgXziwX9BcYxcdM%2FaepgnrIkQtOv19brWGX%2B453CDNAHmBbh&X-Amz-Signature=d7d3a7e3d6e08936b7773bfa8da6ac1910221c942de06704bd2a2bb92cb04af7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



