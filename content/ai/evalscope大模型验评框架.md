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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMDLJATU%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHmk%2BLyZhcnkWdKkbECylGbt3xdkwceBpSn3avFccW1AAiBFAh17wz13FLZTkdZ00Xdu%2FLjnvEy2ZnJqUocp0%2BrzyCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMscoZMNMf0vD2I2xSKtwDkYjXZTgdH%2BxL61Rm0lPw8f8UTbcSzyfHgGamh80zEIz8aOhfBObPsaUHP349%2F6mLibLWNWCJtAY2lemwY%2BKev5KC2SD1Hj4SdCkc1u9HA%2FkscZt9zjKuL63zzwNlNJ4%2FVOla7gIwDSkFCEeYF015cL2eIRUYp5aG4b%2B8mr%2FmnWWz7Ngnd%2BI90DJfVZ8Y8Ukds%2BheOe3WXbFXGUyz%2FgJyVH5Rw1QTXIWj%2BGRaLGoS36w1BoEEsU0dV0rar8qm8LdwNh6ugYEOF2HpXwfBcu9SlGZ%2Fxw49qRDi8CGe%2BkAFJq8YiRAPM4yvtujKj6Ams0cz1NzBY5HqhSpuKfBnkVtLxgYdRVTXoZD6P6iaug9RCiW3Dwm4RwJ38E%2FUVpkv1jkdheZqCFEglv%2B7FOAD%2Frf6%2Bjaeik2AUuQGDdhNK6exvGKBeQ2aznDdNa3G0pLuz8ZGOzmtkg7VN9bk4AI8B5sSI4c5BQ9%2BgEkDB0FehdWcQtAUl2UYb8smU36WlJ6ScGhqfwRAYVxd4KSDyRakRUs0VeCtgQDkiPaduoQmvKLG%2BZOJXqxUmb9D6R50FOyoBZHxH73F%2FU0ItJlBR328Pm2xkcugyV6uami9B5XM2G3%2BJyFnKwyAitIuJnqlALUwtoaAzAY6pgGVZC1pW1KblEJEwbd1UYGPvlx0tJLnaMcnEOoS6fy%2BsQd9EkV4SIKKR6JLZnvx1Sz5qnOW%2B04PV4OoWH2AeZyw2MRK%2Bcwrluei%2FUvef5sbJXjslcmm8X9x9lep7nRGg68NW51ENG3ID%2B4rLrB%2Fl8FEFfeMrsv7VhaCImFP122%2BOLVUb1uFlHZZ2MmnjgyH8JIckMhvaoxamOaMGKUUTIx7sPfNLWs%2F&X-Amz-Signature=f0c2a32c8e2ad639b9edde0f59ae549b4d14916aa1ae0c850fd110d49df70beb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



