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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S4GJDVC%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGf7dabNAhIFTpOz%2FdemeogN03KQz5cmUhxWgpuzUhLNAiB4zFEzJVOgsADNK%2FB9ZEG%2FKpfMxedb6vl1Bgag275ydir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIM16CNff2aYPR7DgwoKtwDNgoqHOjF2Eev7QMSpOHh7izv99iTUAPKReA%2BYygNdX6aVLUwqbdTgd5q2x4sLmj70ikQgj3FDsGxRmHlMZsW3cmyJW3qrxKhgX4tg5U0liwsVZTqcCB29Ygh1Rm5NrV9%2BwZ9QC9QrmGIj5vqftwwYbxKPbxz%2B1Zm7bGscMMpbsL5UXymlszO%2FBLs29Nkt6rwwIm1Xdp48co9f9%2BMtxVfl0bZag4SMnN6DjgQwqpRUyvraPlIBV6FLYyevZBT4uhP0qst8LYkVYaCw8Z5zV9Y4fMqK5wwklngcGSenQmjGHDfedKSEFnwglEeN%2ByXb7FydbDZZtLtcWooTTS%2F%2FmqTa46fjopHxeCEN7QevatPaieXCC%2BaQlOmavkoTa%2FmWrTxuY%2Bz75AFtPG2%2BP%2F6Q7J%2F%2BcaBBQ7wA%2FZiDeykugsWGbrAvuIgCGhYk82PFM%2BbrRtruh7lcxKBK%2FKh5qjJ%2Bv4vuXu857V9DMjfoxdZS%2FKvlLQyV14w5cSdpYioPzheZZdmwKC3uNZxJ4i0sKr0hwaF9sl1UE4wY%2B%2BPGwiONmglRrqSQ39l%2FvA0BQ5AynPVq7gLS%2FAOXydZr7jaFlulaq1oMyfWPw5TbXJsuQZy3m4ybGpD%2B%2F%2FFcqFBIXvjUmIwmuvmzgY6pgHjS1Sx%2FFG%2BOOh%2BGZ%2FE89mQZisYy8Ut4UWI8SuIJj88DdJIsQznVVPGOXtGuPSkRvhoOJzOrqNL%2FbMvrXF9v8PCvBxXJvCBFKXaMh0cyPOGhFymJwyrSRgw%2FX%2B1z1YkPn4Vu01LbYEyzi9plqPsGlJ%2B8WbTzkp5BtbRMADvGfjQhKlHQew%2BIDuEqjGkJFxPOyVuG6ZE%2BwiDrfczcymQ989DatLGAfO0&X-Amz-Signature=1e3152c766195f2c2f16a40b94103ea896f615d1b9bd49f16c0c68879cdb70ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



