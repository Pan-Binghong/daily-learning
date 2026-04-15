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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MKX22ZL%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB6AdylKqHR%2F0LaT17xr8p7TjwF2R%2B2KcQFFkZbWC%2BXRAiBhCmdbDWLTS5IXrI%2FwNXKWhTmB5KquiQkOzUiVadxqQiqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTGht66Kn5NSGL7whKtwDhLVSWmKsEQfmXejzy3ZLRg9GED%2BXQ0OgDV1n5pqkKjWy4M1HZH47IgGQfoBchi1MO4uxjoWFjfZCPOzdhVG6sOIjFDbodA0XbjJgN7UKyvDe%2BibgVA6qyrATe3AcGcgMT9utNdM7o%2F5f0LFQjL5Wgp%2B8OUNIMpapji0XO%2FdCI3G1VDbRuPGMmtlN3ZdhDUBfRJ59NewdOCMz0HZOgs6XbKYMbOA7puCiXd0uAVknLosOBnxrv9DqnOs6YRvjo0x6y6y1lQXkll1eaf5cE9PnmWW6GHxgK8Wf8hDIF%2FgC7ubxptSvgJwrT1gaUBeN9yFL4u4LaQ07E6cxrmvtYV2nJ3xVVCf07EE%2BbkRkrV%2BKm3DhnKglelPalieJ7nXg5SP3rK%2F0O3C40trcLLL%2B74aWKH5onvn2K%2Bb7MrzXdSO5%2F5Qx7k5m4stT3HZrm%2Biu773JL%2BPHOLGdX1se5alIERUBNOAEG6MHSQTu0kNSq5%2FgGMwy7rg697Po967Q32%2BsDCYJef4WuIhRadjQNzopjSU%2FvjTU5cS0owQIbGAVyCn6y01t1evP9g3jhInKXe1GTL2fCi8ey1aX3TS2k5gevgrj0L%2FGJR%2FPiQxfTbi9nhefRc31j4w7GsdgXrqaf6sw5JP8zgY6pgE9RHjDYFPbdB6DSsATsJhRYBvll71n84522s6Gd%2BfA%2FVxrvLR3rzyKfTG%2Fmou0vLhVwkOn0L7K5k2QO4q28OUgK%2FN4Ad5m802n9GFThRQXX31c7luEHYMwYg0l9QPzmgM%2B2qBCbSnnjmqriwA%2B6jty4jumQsQZOqaCvmXvlkVgUAyd87nfPnWieV00NF%2BgtDSx9KZTz1p4P3TyEJED0tawkyBWvchd&X-Amz-Signature=00190766449a6de501f48798543256dc9c3f8c1425b91e5d7ebc5ae9a528acaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



