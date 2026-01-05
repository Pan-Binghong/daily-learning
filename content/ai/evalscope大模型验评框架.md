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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U223M3NV%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQDPrky3aSCcIgsWupVsBnuj1PM5J6WWUiEGKSnp%2BEuZRwIgWucixfWDdyNMuEYQ5CBL%2BDL2rWZ5q6ugLxG5f%2FCFxrIq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDMxDKI4qvqRcS2Nx8SrcA8SHXvnWeOaH9qfIwStUcxwul%2BTa7Y0OCD3oSLRSkqcVkVIrgr4LFZ1mcs0QaNZkFHgTGid0Up%2B4vWuNq0dW3XU25ZeHImJLe9xBvebjStca7778RZB8xpIdx%2FLNQDvKu%2FlQrMNlKcaFE9sEYyI0iX9iysNr%2Fh3dXW3ZHmwGbaWa4zCjM78vzjXY2LNOM8S8JBPT9iKaqR1%2FAyEkdxz%2BFJuv5owXvDcYC4oHXU8fqsuZODfZ%2FPVKgPKyab9OoksPGreBZkTe5j%2BN55fI1gFAGnBOxoekHKvdQnrJJO8mvcRbq1Ul9O7Fh8G8VWOuBrVZvy%2BhdifIy%2BQVqkUnG6hdMbzScuQP86aZVwa7nhpxQvyBfGsl9C8D4%2BY%2BNsOEYzEuwpMqlN%2BuXSAsWIWLeYM3ma68S9nYK4BIZ0JWATc5bmxasge0d2RI6elJNzRcgVUXX5Nnx7ahc%2FkqFR6tBv7PZa7Uha0p4OfmdqhkUCtC0LSEXwhrWRo2JyV5aEMt2EG32Oj7wxn%2BzPooVTAk5yLx5yjy%2FQ7cgMSIuBOTwCvfpwgPuvv1wmXgya%2BIMJTpoR7hS6%2FFa1QxIaRvwRuh8F2gOq3uC8mjABWnz1q7gIz9gAwOxAgTanE5UqtvhZDeMInW7MoGOqUBBW1DUKCeomZoj3irGM%2FWzoJhtWH6%2FXdZRfXBooYy0EiiAqksIzfjNO7dfS5ie2WyJaX%2FZc%2B%2FPESiFScgzsw95bA89tFuA68PtGsNAp%2FoSpjchOvJIeT7wf912EkOKZ31zvbEdCE%2FlOXQippCqbbk%2FrukHZidFUSNHWsNLn%2BH9pvw5en47%2Bcbb%2BOe0iluYkpLiD%2BF6j2E%2BLlOLSyFEcwvIrR2YO3S&X-Amz-Signature=43df5e849b5446b9595a3160ec07af4903ff43ccd60951d1c9ef429e8a10e4dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



