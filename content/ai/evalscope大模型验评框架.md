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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAJYGUEE%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQCBVgQcCaVBL4Nf2NoqvmHqPV7ZxE10Dcv34wMZMFgOtAIgYhAlht1%2Fq%2BB6BJcVTQe1g4ZKF9t%2BbQAhJIaxXYjsNd4qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMmlVcGEd%2B4Xb7haoyrcAw9Cq%2FYm5F4XJFBwx54izugV9qxF%2BMacJcVYHMRE7tUFM%2BAc7d47etwIa7l181VcwdpzA4ILgStVquNlEcTAiBDDsAyEOejuYcSyWKwVP3VXSl1zKF2QXjzuXNjqwcjyofELsjGNNIJ9NAa9A8eptD6rRBF2pGB7LBj11arIcHYzk%2FrCS3iWg7ipwcUeEkHYkTiXsvzROEZyf%2FycqD5yNG96MvzcxQovsiInSnupIHK4K1hqGfrY44xF07DLyVAks4I946%2BDUQvIPUBPgyMaeO3Ob419FiXq%2BQeo1zhm2fuFXph2%2Bx9JwMkthk4KMqoCiv1UWjwLZ09Nie6M1DIafvHM5pgiyzJxGmxAKoFAzWCwG72vZXfh%2FvZQDFx3s%2BdULRxrgd%2Bod7Im9NfoFgvu7gOL2HEORzrWqWJP1FiMOkSPuichBneqB7IL7O4kDVjBxnt0Z3nqQRQiFg6wuFtWCRp84cX7r7hpwlXvO%2BS%2BqvK6NIaoUjzYXAJEWM%2B4E13h1egux848sh6pZksYSUYMio%2B3bRuA2P%2BbHpv6EQDkQcpBjYkmKOjmvlDN5wm5jvO6VWCDTMBCnDAFb34h6Xn6%2B16Mj%2F8CjZM1wcGeT3bJHTHDr%2FzIV58ZPkcq49bDMPGRxs8GOqUB8ZPq2tbHVrS8kQzbK4rboMfEjH%2FocMiM%2BcYxP0OD02ZHprEqYwjukYDFWbZz3vGKQzVGnOtZeacAh5nSKxVr6x75BEcqNHo6tQt1edJxgkU75jZJYRenonIkRI6k1SSf8Ki9RVI9oFuOLLirHx5F2KP03csCS9H07a%2F86eqEy8%2BOidwNDCCbSBYtO7VQOOTdWtqyTIQh1Xx1JrHzmwHrRkYdvvVc&X-Amz-Signature=a4d0ee4236e793e4cef43aad8cecfcee6f3522ce51202fbc3accc6346e3e39a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



