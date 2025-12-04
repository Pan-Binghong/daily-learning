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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K6CMZMF%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIEbhgz9exGap2nAQnXZWBsQhSmHfOvI%2Fp545OFtfdrqkAiB518gvRyfQV3lZTR7sTCunAjszz782M%2F%2BIiBF%2FmSSINCr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMTqnnbNnxLttRXEQ1KtwDYf0C%2Bv%2FDhWWona%2BXBvEJyTsew6BNMW6wMzCaQsTZMkPHovE1eSeHdIair6izmnPPaybr83%2B%2F2Oy75cwroXEcywDgIoYP0NttveTx%2Bve4IXILoREiCXkxQLt%2Br1Giwc2seJCZYF5TAyA5dyRKvOyEo7hIA7MKnQrbXm%2BFV8em%2BNHHVnCNeVlbpb6uke4gEBaawhJPJumMhK%2FA3WzgfPiRRnT6CRphgbtkxGVRfgncp69LfFYK85LiB9Ng09crTCekSdiSSszzYSH8un7qktrVvTb9P%2B7CwM8bpEIx%2FantnjuuVzgox1xfHup7HVyB7%2BOmJlAcz3yWjliOn8DnVO1o0UlJQLFCNjTVwE0hUXU%2FpINV05wUlY0tVjs4%2BHQjMjVeVErXKiNvZuO6oq46kurMLd%2FEDHEfWBdVPej4hQqRXbV5lyXIpaA7GzUx37kG40r7%2FJMcGQmEt%2FS9vYbusvk9B8OZB%2BOc3eep94DZmH%2F71tJj35E8kk6HS0WUWGl3nS2N2MGUoRBqoFlrn3BQcY40LQXixfZjpeNPIIceDoPqvg61SpZ8jA%2BjzYTCYgDYuf5coFwog3FW%2Fe8JA%2FTC9YxtrbhH3hudlUJsCxUsJ%2FQExNGNg9DvwT6PHb5KKQUw99TDyQY6pgH3qD0nrcXiClSWCQYmuwvcf2nMB3zA6zvt9B%2FmdB2hTmrPQweUNy6bbc2Hpzz61AQMUmeBa8pNOxc8kQzA1P6tr2cxI63qICaqZmjF5GxZU1d4gW1Z8bTk%2FzLxLR%2F0XxVv18%2F5%2BlMc2%2Fm4ySqR15a0TKXPwi2LsrafUDcNrFmeI7wcxKjCn4ZH6kMScg4TFxecOrVLlavNz6fglyId%2B9nncHW2bMt1&X-Amz-Signature=849918b916dde5811e9853655a84c3559a519b4a7a25c94e3edbd7a3ed93d935&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



