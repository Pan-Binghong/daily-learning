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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642UJ6A3D%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDOMCNFsQZq3POIbrRYlKbVs63FWhhEZJXKRdUlOJd16AiAlOSFXnOK1bwAyvFX3%2Bt6gWMrpi3njp8nsPrqm3SHERCqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJNJdanLhVAVq1fwRKtwDrqwKXPoqhbY7VRTEYqSCvkFSyMgD1p0XnDUsmGcbAsaO%2FAhbePKv%2FcHfBQjE5LwfUzFCCa4KF%2FHlrNuMwVO6O5HCGxxiPlmN3OsprTW97YGK20cIH0gZpp%2BKxotX4UdqmjviBF2M0b29LiMM8ohoWpH2RFGqLIassP1RGTZIslVXp8xRs3uKJGCRPY6Yt1C749jiwMf5HmbZBJynf7ev5Dg5%2FL5rq5yznhTeqmCLAd4LgimCAhTEbQUengUFSaBYxNFuyDPvHR4GGsvNohqDoHTIWG%2FQdGPirWtPzS2uupkmdXkjn%2FPOT%2FO3bsuA8y7E9AwrIir8Ln0tOeWj5nLgP7RqiGuLEEeF2%2BQJBweW%2BGIbOvbR09MUhJhpfumNU62pab1USdMyxDmgToRmX5Ur0AUt22sBIITtQP33Cso6v8mNQ%2BL%2Bt02KAKEL2kiprP5wkPLrLqrC0l5eEKyWFpZb04frCuPQe%2Blxl1lMl%2BHldCwPt5tWUyfVlYQ7zo8siUGG%2BHDA2I9VywEnWVMQmwU2PfBLx4bw3g9ktysbro3ZOPfckwfJ6wlCHO5okfj8rlH5Yl1a9YDSphVforRc5%2F%2FXEVvsTObjlul1RdXbKdhP109eHS0mSSfetPrkLmAw37fNzQY6pgFuTrZbSQj5gwTwvDrgjO6azCdJCfvBa29x0Ftp6KUWfHQ0sC1IiIQIZEnd0H8lMGYv5RB3pdjo1%2B%2B8dI1L3WISbVzATR0RnwY5WYARdXFAFo4g69L6pieRObTpGJeSFjXGLCfNAiavbvFWAHjbgV3ARGLZxqcTOlzVOFgqugYq%2BedQFaa70PeEO%2FwU85ds3JtQL%2BWPB54yGWLRe6L%2FgAE30Jp4aqxR&X-Amz-Signature=04798aa39901e65e31630adc4779364c21bcb7c938a721f483d282471983f318&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



