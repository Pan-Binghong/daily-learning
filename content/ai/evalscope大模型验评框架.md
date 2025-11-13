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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSI5NBSN%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIFdDGR0u4dAJU1cuaSMOwdln5GS6jdyshL23H2Imv2HaAiAdtm8rvl7uaQRvLP%2Be%2BxswaFbvTjnkO9P1k%2Flrxt255ir%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMEQNNFRh0vl2FGh7iKtwDpSXqkx%2BZGWZ4SXLYa3PiWwVhRFVoqq%2BoAXuCRe1EetHdU0o8fxwpT1KFEujwmI7EhhNyl40FZZalXlL8RUrmLGCejbFonHimCiUXbAUnPWCnSgmB8JcoTAUtZvnqApel70OvU%2FYkFjfFLCaaNR4NwgPiy9LqCAHN42b7RAQDIjChQvejOiNfAhRdBdiPvpIjVu4rSD%2B6beWPYqa86od07fjF3BAq7C%2FIdCbPRcHxjfpdLK40Oeedy3TGz5oFo9Q3J1oHUFQY3we0G9o%2FQUrQTuwmErbc6aAdUEaifd4SoonIEueaVsKYXi5%2BsouBDdD1akPP9sHgsvByMO8rZ9zw0tnsjyKrFlQJica%2FkiSxG56gGiQ1NCmvN1uUoFGKpHKD3iW%2FaxWLOr1LVHbZEFabQ66Znvq47qZg8NDe4Bk%2BjI4tqwI%2F6ASJUA2yF7K0Bd2FXog5bB2zg0AEYVN%2FSlHaAuseiyuJgoe%2FUQRK96mFitwBJmvYPgamLcDihx1AOLmQNelBZcaX41RZwuvof6LLVlvBmcKr9K2iZ78q0hDztBJTqv9GaON77jdVOiVc4RYF%2BvdJaj7DOSqAJHusCceVdFBxY6Wtjg7QRM5Do3d02uWGH3sNB4%2B7hkJf4YEwofDUyAY6pgFscJkJDCXgZN5aKMvXJeO2VOMpkrGUKzaJP4O8UZBFBDFEQp7qpVivnnuS1KfoSUAMzZtpXZDhYxaBGSPeot10CiIfPeM3pm199NtHE45Qx18mBmjXtjcNnRj0x0xf%2Bcjt83Yk3imFZtRI9wFa1HFEa4EhXt89lV6Lw9ZgnCFwidhS3etZcY2EWkR%2F6tQUOvyQlrd%2B08INmUdJ3DSt%2FWPsdAGuf68%2B&X-Amz-Signature=aa6692c2a3cab27ad7b7a32710feb266220ba0f3f92fe1b1f21c0ed0a7ee55bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



