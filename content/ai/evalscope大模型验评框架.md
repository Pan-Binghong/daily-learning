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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QORO33CK%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIBFS%2BBY97IShvrjCizVuqv496wcfYKCvUfRR%2Fp7SLjAIAiABZRmsoMKtbUJeZTdousbv3FImQetjT2WOK%2FLjpAmrBir%2FAwgwEAAaDDYzNzQyMzE4MzgwNSIMPKrlcwI4ElsdqrE%2BKtwDuNvpoVU8QFbC%2BuXZW6QBvIH8CUGV%2BEczoCrqxBqXmCewCc8OtT2PBg6pDllTdpmTKY40cvJkWdcNRK3Op4PIVrFyjJs1bSSKZ3E9SNqVmxzAcPYR5WrHZ6iudOZJ6WvWpiwj%2FPHjt7ErStsp9QXZggz%2FEyneYpI8jubunOIx6D78a8MrghsC%2Fg1H34f7mWfXi%2B3IEBMYAVygkuHJDTbx6DF1GRBdiv%2BGyCTCGDCcoXMgHtRjVbCau%2B4mv%2BDWcHJNp46vylANlkocN66WVGmY78A4xwocBb6zM9kKgpbCTOaLcdIX1j4oOPzSr45LTwnOPrTef2Hk9lHKlkgt8870cW3KsoO1hWb7n2%2B32Z57byMXertt42Rrm3dUrLN8Xg9q9069RBEj%2F9o4xrtjpdA5Eo0ds%2F1Iw%2BckV48lHBMik6%2FyRiqG4uc6KNB8Fj%2FR0omcPNGmY9gx8TO1VyoiJDQP2AlZNQe1SKa%2BeiGAd%2BHW%2Bc8OfZvzqZmaC%2FtKjl7%2BceKdR1z8R2FdrpvwmmqPhYCkF0P0vUiXMa7Ev7aWuQonf8VFOP9KsslXws%2FYD41AfkrPCVXZYymncrdJ4qYtNmPwCxv8g1oKSLY%2Fj%2BNKboHnTeIgij1X%2BmaLwxWIAzkwybHaywY6pgGO%2FW7o%2BBglCwcmFn1piIwe6NKvxuk1kor0w0USwO6UXEllZMkGnbfgZF1aPuEznDnCD93B1OmR4nINqARJLwte2%2FQ8MdIhYwDOmmRpPmhfBYxU6qLGJW0mbcG0qW3ZjAyFe73AvLuBe58kO%2FE52J8H9uM8WTE51OiZxlRy7%2Fz88Su0tD8S%2FRIp9GULLY76Be%2FTKftfg4RFX8aV5FAquieWoo89LUxD&X-Amz-Signature=62d78f638d785d56798ad72ff73e0265d8f75dbb883d0ca305fa999cb56f54a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



