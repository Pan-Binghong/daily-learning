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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V4MWNPT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIAZDEe%2BlHeyEx%2Bl80D3aZ8vQANOCjs4LmCDxZW55ZuM4AiAWEtEXSP0kNnCHjeQDPhVu67HAhcTx4TRkScKhaUvJOyr%2FAwgGEAAaDDYzNzQyMzE4MzgwNSIMjf2f5h88mGx%2Bl3XDKtwD6IEJzMx5o46D3ZjoAuiWaEPtBMtXeJ0X6RBHyIfGsk8GWlz7NIo68GucwSVMfAsKL3%2BT9OWjugeA657bc2XOBYIPbjMAXxXEFIljJWq1xfvlGzFlLr5YuabdJm8X4csqnRRhQB2PoYcysgYSK9Zd8gAbTsmRMgvXVEXUEkXsspIWWTxZQkUAf7R09vZHbefbPNvX7pigNEC50%2BtE8d8r3ZgAVOAoiu%2B2NQN%2FfxiwrZa1gA4X2Knm07dQkLOipkJc85BmImlXcOQVgcqKGvnkCvyds6cEuNN8X7CcOxT6lc3YKVcwFFCbWYwh%2BzMLO5Bev0im%2FtwHG6TzOFzVIL9wolZoLsgGGCdknXwGEMywBxVSPeYrzYsOrb05SiOWGk4MgGQjsAYjzVUurNd1YE2z3ukzX2yb4ca1HkksOXomcwl1OAA9dzC2Y5bFUUb2xsYdOXYLo2SC1zZaRM7fgmwS5fRDTS8L6AeU2zIlZ8IY6xuZmGQNY6p4pstdwMt95SlVlkm0xPY9PPGvOpRHYJExZzPEvxgoREsYGZRVimTQg1pQo3QeF0nFgsOtgyZPAjxxBC51890TP6b08imUO%2F6AMRLjdKHBO3OGL0cKOKNqKBujfLEwS1zaPZti%2B7EwgbTLzwY6pgEUic66a2tBxhCCRYUSEdpc5KPpg2CGKDjODIqnFEU5WJMu7Qja0nCG6NgcCESgQKGJhMoGqwf2PQJ1C3K6LPi4mPhwd4LTTPyOsooGtGWryh15%2F1CeiDkeozJdxaurTENrUVoDAsmWdcq3c%2FCqXKRbT17U4tvfW5PTurJM3zHRhD3NiGHfg4Le%2FW1%2FFf5bWu7mfXaCem%2F0DYhKBQ1WlSlO8xDUX1cQ&X-Amz-Signature=1b4adf78e74a6a1672e28a444ff78bfa89af5b81fba65bb35fe432a0c9b2b745&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



