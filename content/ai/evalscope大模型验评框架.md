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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOB66V35%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBhRSvCd5KqHdAzcBaQPYIbtrixWI7VnBpSBUPOEEwtAIgR1dHEt%2BtX8H9HjQllMtDYz4mNGOKcGXE%2B37lfoVB3wQqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKyOOCdFFguO51TKHyrcA0DqXX8hEHlQZzWtitTkp524lXlagxlnZIR7LOqnYmLc%2Fcq%2FsfqsQ8cz%2BqWJaXC%2FKXiSBlh5TijrHeqtaWPp8%2FFBb2Bb2CUiH6upPHuFDR0sLB7sTwsBFOJnqV20QSrg8tx8DPqIy1CgJxssW7%2BdjW3LnfzVh%2F5KuTXKX56W5%2BR30gI0TsH8Vqt3xdkLbu0mT7sVhiyA7fMOCPMHVd8KH%2BqCPo6y%2Fra24G5mfE2u4%2BYBcERliwd0pQdyrN5BlQK8gm6Y3DWBCiVizkOfdwtL4x5WjVNTN4B3GoLRDd%2F7BZnUJ4H%2F4fOlLZGY3nR93Mtom2R48lPnjjcgkjVHFUYlr%2BymPhnNHENUuvuSeEbh8Drym1xarnKWJiwzk5%2BLJb%2Bjh9mRpT%2BGPEoaNU5vyICFy5XSGMEaZXnGbwdQQNczXQNYQYVY9cHvKDRW1cXvCZEac%2BEOk3%2BBwJ%2Fj7CJHddPpAHA%2FUTNSGnUjAjECs9WdFmT%2F9U%2Bsd%2FzNNBTgvl%2BLn3GUSBz83Hjfeob8%2FwFEUfKIRZiyyiEpRMQvwycc5ssIxxlf709nAJuYVP3rKHl0gLuiMlSkpezqqOqvKTo9JF0dIy01XkgoV8C4OV4Z%2BUYizPZmlIu46L%2BOCwXMfY1mMKyQ2M0GOqUBUytPlH5dmbj1jsa6ubV%2BDxbwCSoLdNRCOfr3BDjW0KlIiDkeK4uWYLOUKvKvjvooBBjvzGI12wsJbhNOTzTISR7uRkpsn7HTWTyHHjRP7WUiivkOkaDrxhnTkq%2BReS1mVpd6Y2P6AISal0NI07zGQX61fBW5YHAOq1BnaInXRuF7UAcS%2F2hzRV2vQeernF9ZbYcJlW1yd8zSIwOwXUSbwFDFJDB9&X-Amz-Signature=92c81b33ccaa873a4566c505f77109d3effec68460b9329f9d302a8edf36a9f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



