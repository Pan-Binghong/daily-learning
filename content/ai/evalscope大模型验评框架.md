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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOPZLB6X%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIAxejJxXGEIAkHwKZaw6WhDASaHHc0iRCUibIvG5TT4QAiAdLhdndbqwofuHmr%2FdAXlIxIHy8ZFxL%2BdrJGIv02ON4yqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZXTIu%2FUNqKM%2B%2FymZKtwDsDU4wnOAl84xF4F0pfkT7iNxOoJoUxeazXheCzWYmvIp2oLPg8OnH0nsjKHLgKoomIlJmDUYWNevaEbIiIxcC17gZMR0pX1g3uRlC%2F4TdnVn2PsMVaWdTQfrtOg6PtxlVMOloqQ7agqAXRMFU%2FcqfG4MYNxmvAzvjzFTeY3U3To4wRWzZCMl5d0GTbVXV4Rsq6d2njX9lz1aun1dSwYOVMwBHzah6JMNbkesLdYexKjAeYFgoH2Hpnfq5ccT6jl0b6F2ruMV7olPnq1Gt5tHPSwhZpuAiP5inujUulDNBljuS36PxVVsyArHlfymozLFHdiVs%2Bp3SsmkKnS1TbEkHTTo5Y%2Bb81f2TJScinHKPxaLhISpMfnVsSNH8uqYJs3MVbHcOBmS6as4Biij0jEPuf7qu%2BVFArjON1Q5eWW4dE0hrJ7zt3Aur22%2B9qMnHwdaBe8Y%2F4sS%2B%2BY3839R5QYtYzI434somJe4EuANzmdS%2BrUR8o3mRVqK3CsNru5jVGTsARMT0R1YSWAIXWvryfP2S8HMVJI4I0CiG%2F7xzQdcqmjVOrDyfmIOdjPnYOTIS160Oblnv955oawYgCsEQx2YzDufPoE95lYNq1K4PqmL7iXGZZ%2F%2BRT6lKI5nGQIwu4rXzgY6pgFbUNOtjE7CrE09RezhyUs8Sgc67FN6I33cmDxPVw0sx%2BTyZBnKWRgreiwjcMkVTCNAjgfCnuOCSSNPcESdrwmlxDsX%2F%2FRAIYfBZhPYpCo%2BI7zbQmkQanl50ZF939%2Fq9rZ%2BQn00lQRu%2B1TKGSV90KAad0vd18qFuPPBvSxDoEN7VeSOszBg1YV%2Btfbe1FrXviWONGMDuUAi5zHigkEBN3oCTqr4NItk&X-Amz-Signature=efa0a630754bf225959e4819f662f3660e403823515edb991e64db6dac849a15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



