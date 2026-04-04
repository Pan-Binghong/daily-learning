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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SE77ZOI3%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6z%2FxoH%2FHTZtRnwInghrLSfrZitngs%2ByggLUYJ5wwxoQIgIFccJfjI7KYR%2BM4Y6Za949v5BFtIcKV2ffXgxm%2BLDzwqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFeGyj%2BXGwDIjkf7CrcA0Ik1xGJYrJONRrLl93ALfyQXc4acV34Tj6rrx2c6wqkbInbvTyneBg6rCp%2FZlppBnORxV33MY80Q7jM76PaSXbTRpkhcZAgkJtYpJXndqqAcYauc4tKr50teWgpQ0Vg3YnDyo0N90thP0iA60jK9lUpLiXZqNzOZakgPYE8N%2FI5ggKm7%2BglKAIQeqj%2BIschnFe0YnTrk8ZGaMPyOmbHs8ncKPiTrpYSjOP7HUXH9G5PtW1YHZQPiXPiHRD9MmzB6yzfWYHKyCb0keALCNt%2FzhQ0WGqSzRfhen5r63J7LvOZcAic59ZSBa9i0jaMJTYkdF5rMZRrWxhpzyjiukLBOIfCO6k69VaIO7%2FBx3Ga%2FhsccO9VSg2GX9VQpRnFyYY1KUFP2EBNULEVb53S5MDJ5%2Fd3iEe7lAk5BMBOlO6QYHdLH5qTXpruGhEkBDUUQcOV4ZvyTIh%2BFM9kZeaCps3YB4vsMO7HfblPXRTAAkF317TpvJPYS6tFLi8BLoZwoQp9sWdYuq9qBWBaZRQbz7E2jUGqkAxl0vC6F1uEz98cb520wUy1DUo0c3oEvDsYxmx%2B4fbP1FKE3qgbFHxgun093cavTV4YUFT3Af4mSnaLXNJC%2BE4fa0A2jvPJLZ14MJ3lwc4GOqUBIPeo3X3enbwY7g3pWtlWASSxK7C3vOEObLXCaYgaIhXZzMYDiDR%2BmJPLjJcwZR5JSGVdExE6tleO33uAv6D%2BAYhitryBNO6UUo8TyBVoI%2BnneBuzJzTmL4h%2Bm0itLC6rMjOUve0pW8BijO4f1irTxeBffxWJYZV2abGPTKvVFT2zdl1DTxroJP44Ks85FCmJWI2mB1Y%2B%2BYRT4ByoU6foBykU6pxc&X-Amz-Signature=eda7ee4737bbd610b9472e5c2a27c68ac6ad56758d5067359245850471533cfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



