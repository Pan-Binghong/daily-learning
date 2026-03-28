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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKUD4LR3%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIGx%2Fn0PxxgUxA1QDpCZi4GRyvUUNDjiprtH5I6GcmnOgAiATdT33p%2Bl65nkjjCYjJh0XUqSsbwqD2vK7ptNngUPVHiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0BJmuRPZoC7%2Fhg6WKtwDEO%2BZZnagu3PGHQ3driI8FItGyczVvqcfIRhYLN99zKra%2FGn3dFnj8MBHPXLe4Uc1RgEjr90anbvUIaEOuMgEeXL%2FqqCmkDc9A8VRsuRY54J%2BG2UHV5w713C72F654nAkNT4iqDcAIKVUXtOa6bqC0Ivt3bOGvArmmM1vSwOiwuErksQ6QEx2%2FRXXKhAszJESZHCwo7xFPo5yJNl1pkF%2FC05mL%2FXkfsaJXs%2F7hRf4Y%2B%2FDHBvgB9a4epqxAdXGs5w%2FsMuaVEEHI6j6Hw9fKvvMA%2Fsewfi54ia9NmSLHuVovHJ1OCa1dnYTKhF%2B1tawj8SY9N15rwohw101TPtX%2F9aRxRT7YK9PKj5T%2B91rjKx45Gu8BrGSxkbdvD9mtd8pRlcVjOmbnslB5AIlBs0zawlLpYIEJ9rBxSjeX8Kb%2FXJoNCjlef%2Br1JnlHDemfy6TMt3CadrpsTWR9kKp0uBGSbpSB5AZSJO36x7DhbxQ1Hh8gTPdp2WsVyY%2B1zwnvuATV52HOfFejbvRPwJ7cqDhbgbmpJ85sTIsvrCZXSKaGd46PoaHYTdYFPjEDbr04t82GBXk5BJdzj1wf9AK9Bjei0avgjrMSbHGc1E6XGHkK7Kl4imnJb1bVNRSXvGcE0kw8PSczgY6pgEiQ6OBVF4dQCUgKHSrrlEPxSZ8MX6wHHcohNu49SgcCQIhSNuGyTUNnSlt5olLhAQ59%2FEXx3oTKduWnaE2PhXTfKJifwR%2BGw7mRWStY2MGXBDgR2qWRKjW88E1WMP%2F13ia1WCYEypd1ljdOq59XFvQonGJxt3wY0SIEHBob%2F1OzChOTDEWWeW8F0jOgbod9XZsvHSGEQAFmRASrLcueRILL%2Fi%2BFjZx&X-Amz-Signature=3dda0febb1728a8f77db9a43d45692e04a2c3576a24045dff690c810f08ef440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



