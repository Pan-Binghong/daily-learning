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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667X2EZ6FB%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7%2Fg6S7qaZnhQDbZKxO1NPEEe4QHvwVqFLZS%2FKAXXK5AiA76Gcwp0Rpsnotf9TGAfweCgLB1o2fN25Vp3U5fNW3Vyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMI6iLsYjifCI0ZL10KtwDIjHcZPcNfDZFOz7GKJFc1%2FzTUn8ZfASx28roL0zAeuXtW2scuw9YwvvARXL17apgYlT%2B630ZKnP32BD4PB4fpzjrrBxHOlug%2B5j9aIvFTmH5pKLC51ypRbC75gxrEXnc4DtfSG%2BvDq7lTUnPicY9kYL8aJYufGzHlmt4yIbMyRA30dXwNag%2BYnzRW0yBMBceKVp0%2Fbxp%2BLJ7BPOAAguPU%2BjZeoa%2B9%2FHQQHREgodkspT8cBJTfUGU1k12o0KIQejIIGz1QUfFhqEgOt2dxoyaaN111VQk8%2B3%2BrPW%2FdRvcVNwnMRAuhlEI9K5DOOH1wZRtuqq0LijfUV3r2XP47H%2BTrRWQR9KzVaZMaij%2B5WAgdE62D6E4gXDqXKFOSr2GArbvChZUS%2F6llYJgjsFUSxohZSv8%2F60jGWsbeRoNuGkLI1B%2FJTISztddY82Ats6WQH6H%2FLxn8wRYe75IH96hjBJfC2Z2Z7Z3BmhJ1r3MaEeux%2Bpiu3UIcmlJ9aSCODNp3bHcakFijBgm03DCSYVs7zzmML8iMDvlWJ2W2LOoRiZVRBWwObpv4rGw4rKhB4k7xFca4vD5DKCxSH1vNLPKo9pzZ8cEET5RIjZJHi8jion%2BZExiVnIsr2jlQpbZwIAwgKurzwY6pgGtZy4vYthVUwfbgE9iz4XS96HWNLB4UGWhnZeeUiMNjzllrDuTy9EyvT74mZDhlj4KBwR36kLJP%2BA8xqShJ2dwPJmQDsMUbWTbT8a%2FXrDBWhzoMvSSJjvUu%2BZATgIrV54OaVu86uhYuFxMLSKMw%2Frrt2%2BA9TY1ip%2FLvfMZCSCqh3BXPicXR5DlIBY7i6WfSKlWaiN9E2GjF1S%2FzBs4t%2FoEZgnu9L1h&X-Amz-Signature=911d2d6462713084cea4b37711abb5113aa84ed9774292e758fe2da7e148cb19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



