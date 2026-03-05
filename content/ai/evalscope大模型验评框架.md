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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPEL7UJN%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHFH%2BvSy6fIHBUxh61FWXKGSNTe7GvHdstPjKJ5DUOp8AiBeVll8QXLp%2FYGliAIySIzDkFq%2BLphVAO43dM5AS0mPuyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpdJ7%2Bjg6Qvtz%2FU4yKtwDVOgrpLjgR9M4tthSz%2Fa5%2BtJbs1wSYjgIjOzC%2Ffck0x31em%2FeFTnLpGTxVgDzaXtwzvx%2BitAiyByzXt3Dj6mqpzEwWsubdi3l8jEPEhXbUpZ5bF364bwE7SYP%2BYAqny9WTNfPe1GO2x39ssaP3LaV5pkUFmQvzxgPS1FEcaTwPpFDs8QRNGiuUeFPEFlkDndAtaZW4%2BemJA7xViuunqD8gHfa%2BgTwoF7WkKlgXRHK0P9UX68kUgfWgwhp1SRAg0cng3UufUlWlhIhfNf7R9e24Hq0yqwFObntE8qHhNQQmNm2PfA0iGLCMqYLRaT3J5JirBDoDK85fda7KYqWgPOQ6mSgzVBmYQDn7BRFaLtG2S83SiGQceQ%2FR5Ar4YLkzB%2Bwq7s5yN7pbDM29Smc8aJb49SrmZp6nKLCG4BV8Kojk6OWibyDjaIDQx4Z%2BYdtweYqDj%2FnI3cX5ROwHH%2FisxxR%2FIYnn0jSB3m%2B7CmJXWPMmdxuMz8bvbHyX3ezaD971W44%2BvwbYgw1Q6UtJ8duXpsHb%2BYfmUkQgbg66f9Hh2YgfduA9MIPL6meQw05mgGdWPoq9LisEZyUwf19AJdRAk5cC0CVHm1rEooDwrzA4EPdKyaFFP54toQU%2BVZhw6cwheCjzQY6pgF43zkn0N8gfOQWi3sVR2T%2FcNL7VJ51SiiYQzGy0%2FfuuYjWK8s%2BP77aQjFt5995%2B3eXH44PFJebvELxJD8OzbCh6BA7NYccifayvyNVOMJ9JAfjFHaz6XMTHt71%2B5TzLMiAsKVgtATY%2FU%2FNOU0bGMJzrA7SupchuR6LRkO0RYowlB78vkRy91qnpHV%2FkMgezj1hT%2F%2FCnkyl6LjkosgeuFdn2ULL3sn9&X-Amz-Signature=6c11c795a9734a6f1b8fe05805f695ad15cbdbf66eabe566f343e2e7d2025ca6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



