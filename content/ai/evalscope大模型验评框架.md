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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3OC6LPQ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2U%2BeC1EaWczM1uPfgf9d27%2BBnC6dlS%2BV1Wm%2FNN8mITAiAjPupoCXxhbN4eyAhyVHa0cdUm%2BCvq%2FMTrT%2FGXv5UHniqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBIZT7kh4Cu7vqqfaKtwDbDdESkdiOpE%2FFVszWVUZGfed%2FyVXGfOLzrNxTieXDE7wU05cxb%2FllMsUkQPgzScLPUAcc%2BJfrJVu3Parc9cXMacRVXfOOLjap4P0U2fON%2Beht3Zx8x42BpQIJBxb2U%2FQho1jCgXTww9fI5uv4AhjO1XxgJf7SQiE6%2FVqbgzuBwNIfEN3%2BzX%2FNoNRWUG2epBRkTNXBGe22w%2FsFW9efOpwgTDRRBaXyh33hCkETpfv%2BaarKRpN2kZD3a%2FVaAJOjSCc3nEsao9neX1T7MyzAC6kYhAQySVu97H%2BBtP3pKHlmZi%2FG0%2BX8sKfdnGvrUXCY2pcUoN3qY%2BkujCLjdpwIt7UQU6jF0vuA1C8QrklE44Xr8yh7mkdPNdys6OnMdqcbnfw%2BQMtvasxdX8attT1n8YlHgSs02BOaWdwoLmz898ymwusqdGGhuxQ%2Fu2mwSpukaOZd127XajoxRghNBAc3f0IMxONO3ny8mLlm7Hk75UBzF85w0skXD7vFfE4RCQ1RfDUCtEb24%2FMnJaCnJyM%2B0RU3qC2H6P20XNeYbTEDArH%2B74lxvKvrka61Oam0hTHuR9w4cJd5YCj5xEjoLavscaQINasgMKlzEuwh6eTqenGzepMmzvkWnhtPji0biAwtsyeyQY6pgF0MD3LFy5n9FAZY8d3rjt%2BSoXFJmq%2BVlfHVC0i1Pgw8wV2WiVbPfdfnCZrN1a2xheWhBXNhpAz%2FjyDwpqdfltGWQ2afCZ1PxPRmESFCoS6DGsW2etc6E%2BenHr5bvHFOc40uqjndWKMWDqY2ciGtuq9d2rdmEbeA1c3WIUK6783EqiAYgWyhzfMxFXkdrqkyVXYXVZkfXUX65E7skIBJAfFBJuaZ2L9&X-Amz-Signature=bb6b5a36eda7f2d9891dda1d21881c419d512fdfa14d72de1c378bd41fdd818c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



