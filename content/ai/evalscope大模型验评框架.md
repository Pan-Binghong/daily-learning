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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZVMF463%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFSd4WMCaoW8iiZQm77n4kvsf5SbPPzp9jTE3pqecIUUAiBa%2FybK52wBwbMbGXaq95TZQU3AsAFcuoQmxCpJQWgyFiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzDfYoPiuOiU3zE9CKtwD0ixLCOMuyXULEAV5J93IsUk4qIT%2F93jHnsS3Dx6ilfmDum2wOgvl0KgjWDOEcoYEKrGsap59YlbVsVix7h7faVymK5%2FFfbu57S0JirbMpcZT7ATcF4C0TA4oY%2Bk5DFq6NoljdVNQo7CN7KsGm0fH1THTCzWVgPUBrLloPdvWZECu8ZZYLOx%2BQulmHn5hN5H2gkP%2FaXyWCbi80qtFalGZPMNdrfw614qV7Dqdyh7yLPxTMkUo2R1gP2BPhcyKs5ttn6eaE8uhgPWoySO%2BJHHUWXTYWvJbKWWSbw1XqvLMl%2FRqtHfFtayrps3vOChGopP0MXZ1EpGvZQ0HRm8MnK5DLxl8bDkliY5gl85Fe0QPGZscnYIHv6RxOWw1ex0mnQbGyZu4R%2FoMsBQkusYpJwtL8DVtm49VjfwdXwaINvYKojxyRiaVX%2Bidm10TeiYYlWqqJJ4bg8B96lzREZf5pxVySToLHVhsseFsKNYGUrPBmICqfG823%2F2SFNHUpFTHttPSQvOESR2ZkUMTHmPfIResEz8oBp23pjOfk772ZUIp5w2n5ZSwNoCJTI2cD7PoUOegNuzu86zS9fdmrQsus2wHoG4uhyGopddHUjg3j2fXSodlqJnwsTQNElEqqhAwpJb7ywY6pgEM3H9BuzX%2FsiYvhylLjXOXFi0XEMdH6mA09fIo4wdwy%2BWCJAx0omHVaiP4oStDSzvZyABgLuZ8FbWqSyK%2BNRON7JtMCxGjkvehTEBWWVI2lfkZ%2FAi6CAjmCpf40WfUjBL18TRQReJ0F63nQCtVsg9%2B8%2FRqdCF3E27co%2FxIXgDH1sCOWIh8tJAu64n23MeX3js62jZftIDPSGjLoZoewhGpiLDgUd1Q&X-Amz-Signature=d7135b198aba55d0b541b8f66c5e29f032726edd659fbda637909e79ab340cf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



