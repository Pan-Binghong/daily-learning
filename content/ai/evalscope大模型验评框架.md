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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7YUTF2%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF6Ms7jNukrAqNM0hx6m2aF4oynzofRJugRHR4tLGBQqAiBq9KjPA9ewgEFyWAqWsGkD1aYp%2FOWdM0X5JGQ6jfJruSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMWrYuVYzE1Qpg36nwKtwDO3mx1Bp4eN2H1aFQCVbsaTNKVsm2cw6Rb3VsOzvC%2Fu%2BuXK5qHl53dhhUO6JqJV4UZq4NMykzKrxqVMOTseEXjJ5ESiFOu3deaas14kMOofYNU3od5agtEHIybzdhseh%2F5IDJbRSZ3AkDnSUBAovjwJ61NU5Q6HnUuothyiNTLWbT58nDdKdb2%2BSZ3AUYRWvFVDrWuYAGQEOCCvWp3aa356u8t8Ak6RaLbALhKgQlncx27D4im4N3hTfXVJnUIgm4Wuuaa%2BBc5i9Gun6qy6QJs%2Fh%2BRbgBG5tnU7rC8FwXEEP%2B%2BaCN55kqsgdeac7Tq54fatT2kvCLfq43afyS1zDAVaWD6Q%2BvZq02RekWLT%2BGazlbTvvZ2hGrVxRwQI75pX0t1M0Ehkdc6Dyj%2FOYBkYaJoO7WkvsZGkzxBL6%2FzJRS0WSXawRKP6wepgM5PZKrzTMXx1k234Q36Cm54Wg1ri60URtakKxaHJHJe5Fw7uYtFDo0yb35GcFGKTLyXA9qp%2FPQs9lBKw0h3AjbPbzCg8xBny%2FVfaK7NnTWIPBnJGIrTLsyAWLdwSDFV%2BcP7kM7FhIM%2BFBGI3u3zoI9zUmWiwMwYf7Nol0w2XuEMmldpbYCnAeimXRFD3Tnu6y6va8wkI%2F3ygY6pgGzzzJ8MSxeDjhp61gS%2Bjrq4d%2F8mJkGu%2F4oxXw75Hw1%2FbDRkQ2hNtaTN6h%2F4KyGHhgptF9EiYGz%2BIyQMUPHo2BBxbkcTQs66eEPXU3w%2BlhrYR2cv%2B76IAEKVdNs9BFnfGWv9tIodNlU54fmSqslv8dJJz1bLcWkOA7Y90vH8uzohvaVFcUCnMaTfxO4zs8Q5CJ2kvPIKT3LUZQyBmaebstOi4BzLFMj&X-Amz-Signature=e44f495c2237da821a89a967313388379792dcebbc87dda302b95d6df3be56b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



