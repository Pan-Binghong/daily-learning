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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFK3BG6E%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGkdgBi7It4bdg%2Bda6TpuayEc94JS2ai3vX6HsYIvpvEAiB65qs4CvCSR2%2B0UoYV%2FJ4nHh3Jij8PFhjYP7kszd9%2BtyqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMugaoX4%2F%2FaKnzJMgSKtwDRqkvJg26wES6o%2F0n57vPJBN8DY8AlfRfBhWj11hkQEdrRiwCivmtabszGEpToyovETG6O0qf%2Fjq3v%2B2d4nAlSw5GvYny5%2FdTJGdDcngmVxd7ZRFjsOlwWrXn8pD7gsFheRL3qkXz8Cxgkp4nnogyBw929%2FUGt2ATnFRoRBT96edO0rSmAAQ%2FsUot%2BQ4fquHKeZUkG8q5R90SR0tzZPXtpZYdGGjm%2B8G%2BzGaB1wPRw4lZwhOOvu%2Fv7BM8LyFPjcwVB9zoGpVDftOKxNX8wnQARThxateXBE1uJecljDnZdeFrqtqQOBDfKnXTSS3535khxWP%2BSFvuC1EDq6BeHaxYSofjXq53AtcBU52Ip3QtNJb281okFHQxNpLLbSo77RyYKypOFUyefzq9clwExwApSOWEAWVpLqHIDqn%2Bbn1TAVq2ThsswBaa%2FGC7mr3yHZv71G3z5LGww1CRiMchcZbHbGQBX82mi3vKtAd2OU8f15Y1pjZvE2%2BPnqrKEKvnvpE5q98sbskwYW%2FqAsSVTfxr%2Bm31rfRY%2BvVOKILn8qjIiO7abSiJm44SKvSXegx%2FjPmi0QNzA8Rms4SzJHLEpou3%2FagNPLNPByi3YrxERJMG6VnBsCi5Tbbisot4ScIwmvmjyQY6pgGfVPzElCcNiVuoyVFwkuBqeKEdMZFdZNNQOxS9k0SvNa9R2FgQGr%2FHAYJkh5xI02bXKu3FVZi801EFse5hNt0smHfRXSVQGnVS4WpNNsWCkcZOmc1uAeBceCfdidmSlLZcqdXhKQvnGeeCzGFsMV2Z3yuO0q7zuIQHGKKyme6fTC4ZhV72saJJyBG%2FHfGhN11PUD%2BEZTETJ%2F%2Fl4dPQVN2Iw7ZB%2F%2FIm&X-Amz-Signature=093f63fef14e17f8a8e3dd7cad65e14331ee93134e07f1038a2340ba6a9243a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



