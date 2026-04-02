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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRMSYOZI%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDocDdnFFCE7G%2FBERl9zNAszUgk3jl1g%2BOJLwOjn127sAIhAJgs0qyqkkm3lCC8CnxO1gJXAcUWAQOKWR2tPKbGLNRWKv8DCGQQABoMNjM3NDIzMTgzODA1Igz%2FFPzt4UoiE2rtJTQq3ANTgwJUFgbZsHrWUbwSJdZ75hg2QMmtdLKQilgnfkrWBW18FN%2FdoymqjSdrvwS7v6%2F9e0M5PhoUiGXHR9cGXRBtSizRhzUevdBx%2B4DRQBJ2BU%2FETF%2Bfuz%2FO0kwYi6Aoh0RyPRyO2Ct5tXmCiz27TLmr4yTJ43B%2FFB%2BZoF6ptH0XPaDtcdVr56eIFV48R0wViG4umcbrVevS46IhKRHNTi62A8dvVwji04lrdljNGLxW0zS8k2htf7iC0z1KDQUt9%2FkVogyBX9uWLFa%2BlasfZ8VSmZYl4z%2BkSqrnOdQxiJMO3ion7faPPEvvZTaLIVxUE2Jgz8e5Bv6F%2B6Uq75BsT0bHTrrpC%2FMUOXTjUaPU9RepG%2BuMHWRX3wH8yrWcofKuLs3HoJuHUVUp7FZy1v9rh8dtOVQltq7bvSJ9P7blK9seQs9WHTWYY9mxhslKQuzEmUo7vFINHMoOVeq62YvREDRIB4rNClmbevDnoKvKMTAzznF4OwqZi0L3gmGhyzgbinFtx4KMiHpOte1z0rrgi8xMYCrPLMNc2DlWoLINIAh%2BPtCGVlEeF8sKH7vxZ6dNZlpCJe%2BzaPpsoFgt3pJtclCzlWoGAws7GwboVX5zyvRSihWWufeMLkjHb8ViUzDmrrfOBjqkAZgaRaL60%2FUbz5xUdiDLGex6%2BShv1aRfAXazC5fID9tKrxBLiP2uEJp5ea3FKk9hPTMVJW92T8mU896hCxXDUEb4G%2BPNDH3ifkHwQLNnfVGv1yj91GksC7KrhYy6or3B1gpYt6aTIXozPOWb5YtTXPBQSWe2jO0kOA5AtqmE5hc3lHQbUpRYzAKpii5lOUpUIdzSkiy1Q5sWnjQ8TjeoEpDb6gWF&X-Amz-Signature=38baa3754d9835311f22d22027eafeac8beea7eb4bc4d6b4ab4bd4af98b5ebc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



