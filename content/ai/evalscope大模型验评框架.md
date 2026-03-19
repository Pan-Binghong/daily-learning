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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBZCIYI2%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIDafi%2B1baL7fbkffjLtcGVSQNjr9%2BHHbVinI9aH%2FzCb4AiAMMWqvbsx8BRpteuUlAGvpc4%2F%2BBfZ8%2FwASm1iDtNP3NCr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMxZCge4wXVohLKEO5KtwDsHwk8JzQJdRWwLUL5ERgdrNxmYFKtit8GifnfyMj3ghIEkgrvFSJfVxzkx7zxHmtYAzg49KENdCaaOu3%2BVXlxhj6vgz8%2B511%2FqaaJG1wYC4fAOhc7ypJhOE7K9wrw9cP6NAL5Gpj10G2Q8ynqxBUXZWktyl8ubjBVDwVSUNS5bssEK13FrC%2FJzuZP03%2BvJDfGKixJuiZjMy1q6%2FWtY2z5z0sDPckNZH0gZNBJMaS3IqDP7IS9dXItZUGV1DvfNQTsS6mfBj0mRUnXfKzsDPNQi1qevpkZXGO8QxUJ12tqyydQFEtv1sFkhfRcy2QxD2X1XPxyjqHeCKMlWV6eQ0BrNHr4RulvHu2Fk3tObGJyxm2IylPzufEosOVw%2BVnkbAYtnsauxtE8ZatdFJ7%2BkoSC6GhTHyXEFemVvPrBOjoRXbOxJM1o81Ihx6G3xuJDPWQFrfcr9aa82rVJHMHDYS9BNWHZnF5XdV%2FrcGllmGoom7L1ttwKHM4A%2FDAoleEP%2F7%2BEcrJmN6P16JkstO8P%2FOiA6pOBOurECdJVClTxMAIdbBGe5vXrv6aT4Msp%2FgoWP8NrRrhOfwXg%2B3yu3QkAZFTu7cBER3ym2Vi9YJHbrZ4KLeRHWnXEwrXcylOZCAwm8ftzQY6pgF45lnOrI%2BH8mLtPFRjpoFvgJhpHUGAC9QEbq5UI3DcpIcEU0C6exLqaSC7PQ0bMdQmYLJL4uiNjzFb67F34cdf9r2sd21SAnhCGYOOYIbKO%2FbDgK4eA3nzLw4NWr1qtemiD7%2BtGy3y6GSX%2Floqz0Dgxh6IQFcxv2w6%2FsbgxsB0QUH6Gm1CUBMTqwLDu4v%2BhVl5J6BKh%2Fg5jBmi8SAE7DI4udeEXmyy&X-Amz-Signature=d0cbd9168480d6046fc8707354dc1afc4d8a379a0b924148fd03ae332706ad76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



