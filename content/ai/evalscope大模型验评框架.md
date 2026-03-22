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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RIP3W3L6%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBFr2Ee70cENfUiwLi23VoDAHkS2Q8vBp2g077cQPRbwIgBWITgSTHJLzj4AgBBUVq5AFI%2F5GT80ZM4hRBVNcqijsq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDIglySUwv6aM8dP7DyrcA%2FyEk%2FSoYaBUrXmU7KQnxPGd7xiqIi3i3V7qHdq5M0Z4ZE2r3fKUuBAtochP4BEBL7oSzRTc%2FcY8bo79GJeCgwutbBN%2B5uWzsW5afF1lWkHr4OTBYHTsGVStKeeEkW8aQ01rOS3EOflIZBXaakQ6uO0qeCb3w9xZ67bF81ggzTxAkbcp64PqSIRHeiZOVRFvoReWnEtZ0A8jwp5o%2BiDPKKzNIeQjar8Uf7EyWm9xEkYTBTa0WBLidGtX1pPKZNRzEp1y6PazwYyUqm530XRyOSlvd9ra3BFoo7squaqoLymOXcyMkqZIcWp4Eav68PdCVSRTaNEDbMyu2TdeFz6oAKoqzCI50t9dik4uiJdOJ9wvr%2FKnZQ2yDx56D310pO2yA1Qk9CGRrTRxIDnJ6UC2Y5z6wLVBumsOYZwTAKaiPmfQjeBHgOCTj2vUrLsZ4mT%2BaiIm4r5SLuNNlbxCQFJM%2B74e92gxwnRVdoXUvZvrbZOHHoT4gKu3fnALYD8b4dFudQeFe0h5jjO8qhMCT%2FiIOIXYPz5EA81GXVIPPRb8a2K%2FhQCoyxmlzmq%2F8aJVCk3kRVMArFM4i8xFOaqpQrSsIzngrxDmQ86RmbwnftHKlI8PY4yxz%2FgLI176UTY5MKCt%2Fc0GOqUBTZrazh1kzo7U6Jyht0lRVk4bMT3wsWVGuJNpN9WMFBQuzW%2FjhX%2BXfBkSbldmM6ZIUv9a6i6scliVmw%2FT1GwMAl%2FLrmpRBJZizaZzvT8uNMQbdGIBRcTKPLtlvPz7Fj3DO87ypr%2Btx8PzaE0X2Xg9KojLgonlKOOuv5VCPc%2FnNRKhOV9dwaGToO12XniZ3peHoybh4ZYSg3c0G2aCZlAUDZOrGSl%2B&X-Amz-Signature=09c0bfecff6b58d03afd2be6bdafbbe6338e06e51c6ef367745b648b4fa6943e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



