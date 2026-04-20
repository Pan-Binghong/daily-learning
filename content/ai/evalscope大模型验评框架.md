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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQNFFRD5%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQD6xX8HITqqX31YWZ5q8gB3fBTNFDmg4TBNEGqKo9QtkgIhAIk%2FwjlIW8zXFbU4VVrCFcuoeZ9ikKLFtroosnIt3CnKKv8DCBMQABoMNjM3NDIzMTgzODA1IgxdhiUUiUZEagPAvEYq3AMYiDvZxscaP2aN25LlYthIY1snLFC1ZvQ6dhUbUc3sciwn3KZuawS65b6byfXeG8Ldz1M3IXiNc7n8IhvwVNfgHpDoUKz2P714Fxn3ogGq1%2Fz9ljpg9YoCYErwP9bVqF2c6lw7N2sH4fdFPIn6sCrcW%2Bqw2OM%2FpLD5n5HBCURAFt%2F%2FElL2FegPhFSVTW7AX8sfu4i7LbwjUCk6glS1vTNaT4MMdfQ8WcIX9KGFVPti755W4NbS9Ct%2ByemrTePJBgumW38o9QW0EqFwFx37rxTQn%2Fu6M1M1z7q0qxGq7GR53X6TFdnl4lmDE4LKhB5a5%2FHf0NK%2FT8uGtWvdhCxhGXcYpE6g0JKxcPTAGm%2FKAxCpjV5pzkFOBKjhq%2B1rEVXqojYwJdyZREaR6TPmzKOdpK%2BXS2StwFYFB9gZvierbDHfl61vK%2FYyfUccHRMZXMHbwD%2BrhuoEbux7MfuodOBoxe7o8ra6HMr92FGPIsnCE6nIVqV6McPXgXt%2FT4fpBGQfeGNVMaFhdx9j1YfKlpxloLlknzSq83UM5ETKWimSbpx%2BEQCYmNobKF7l6T01oQaVO7tPuIAbtQtfslruQe9PAheZhoJ7fzItNbzS8wMIF%2Bj5XcRYBmXYq0xdvIAY1zCtlpbPBjqkAQcWK7VmV9P4c4gJC7W2W4fl60yatU0GrNYjI0QvoZgH9b%2BIHY2XEp972Vas35PGuz%2BqB9kyR9U7zjR%2Fv7m66CRFO2ziTuAYTVZGqlPdoc4%2Bjg12G8Y7xAOggx8tOl5AqIN6PXqmTKGcafsUnxXnEuNOspvJC6NFVBH489ObW6py4JcuvKI8fZ%2BjCYQNe6Tse2%2BSpJW2%2B%2FFsGoE7K%2Be6OGr1zwe8&X-Amz-Signature=231d6b2195a79b76455173ce424c631e417ac06a772c8b0226dc72b51d7c5c29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



