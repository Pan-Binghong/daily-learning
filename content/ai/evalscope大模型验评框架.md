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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCFKWXVW%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDF%2B8WOnwLi3SSmuinIFN0yZ4ro2HcO017G7hhol2WOJAiEA90tR%2B3WyzZEaBuq4KPta4CJ4NGAw12zjr4MArqKiRzkqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLbV75ZkOb0X43F3BCrcA6bAF2rOUtD%2BRYko5ZV0PWHVjrASVWsIWO%2BzSYcxeJGEvtjl6uRUOrJ5qr1tBErFGbBoWm4A8LhM53IXcQ70G9f1DIVd8xMWs6zhGdL%2Bl7AymC772j9mrDGoF977hXe9FQK3xN9CBIe8xdwbLx%2BxfsFEL347eQacbjQWV9HNhDV0GtIuySlTzBBgZvY6VPePPgBg1Er8d5g%2B9gLshyu0vwuePsRRtR7hx8k6Qa8AhWDdsPW%2FfoEdx9cL3hCmB29xzFpUDjCG5DE8TL6LqtaHBW5CED8qwK0obFo5voY1xU4wmSAOBTIqmjDe4BiTrG3zUG8MN026c8VvhlKOmS2IUgUVZVVgKDfHaPPDICJ6Ep2GO7KrWMOptQqILAkVOXcv6LBj7wzfji%2F%2BSwlIs77IAHbmXa%2BiJelDjymMVvUZ%2BKwVT%2BBS848PLXlfmliOOoCuOckWaHtz5HNDqMCVklf9aI0T2gYmMo5dHolm4rYVjTjY58fWZjG4hXTRTmoMQJSZ6qCUd4lKyxqtt9KWktsX80kvT%2BaX4wusv1vAkSGDDCYRYC4mzLYMN6wKJMDdQjyFuAy72xOv47Xfa9CkC9jY7ylEGFuNgklSLNhcHMgFKIUY6f0vygGM1M23WD9oMKiQ38wGOqUBX6Ev4O9IrhJUqv3XHrb4rN8zIWO1YzFWvjsQTYvB6q4gQ1Hvz6YKvGEpK2ivy45CCGMMTl%2BCtKQd570Rm81uF%2F3P6rj7kLEYZPiOz76BX%2BQentOexaAxNeigwrKDjbmhowZGghWYrle4hCozCryOcZVpUv5USfSYesoDPvACx9rDdjPg7dkne3%2FSxepiOsyI9d%2FeZG2rFEdErYJ2PSWDZXWDDqEy&X-Amz-Signature=ddb362da3ad9a80ad627a685adf79ebd67eba20bcb0898053a7482865f20481a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



