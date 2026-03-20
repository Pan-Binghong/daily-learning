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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RQ2F4BW%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDncj%2BuhR5R7lTM4uCyxbH9u19QI1ubZikdmy%2FXplIYNwIgUVbIiEafC%2F3u0aMu0Su6U7WDsMD1XcU8eoXV%2BDJ9CcYq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDOwKcVrD%2BW7oZzzs%2FSrcAzJJ%2Fk5lAF34bIqxFxqzOYmb9LugTczSMxoTlRQ5Nru3%2BibRBZL8M2hfxydGx1sHtYCdrQZatYr36qeUqXjyjd%2FiEI8PfMHuB0GbhjceuOfmV7tHzbgs5ZPkQJxCIGyswwodTKok8B0GMgHNsxbVtFckOSED3RMQUOyTayw%2B3zVzGt2U2P72mi41YKt11iG9jeb45t6Vm4Fce9RIzkB0PvfVHZC6lHru22RlNea4DxJyCWdoin%2Bw36unIYf%2B%2FKK6byQdmq8qhX1A2311h%2BdCBJ138bdUKjhOdebiYn51TuZ%2F%2BztGBIfLX%2Ban7MLHJd44%2F30Q7v%2F%2F8P42cgBWQfHswhdDCU32oBxSQQGJRR8%2BKMLJY3UQxmODyPxRhPGq3kIi88OAknMfL5fzix3MfpXGyj7BIiOBE0%2BmOyAOJBghGvjrP40XRnj%2FL6CMuVeey%2FgeSb6r94l2SiAFdrf4%2FaXK4IE4N9WV9kt9jhup594TyUfUAmYO6xzo4A%2B3mdvLMj5md%2BmbG0rjBBXveMIfbspougowM2zUePFdD16BOxqBmNHghBBFx44Lhs1%2B3hhTulsRjDcRsdDOH3bdFTqP8T%2FvWiQHQ%2Bzdj9gYkjbIbls7UhnS818dWWKaHzjmO3FxMLK38s0GOqUBaWgwi5fRMbaPt36MqQFIbuIqyKDZZvuWWTeXaOu6H%2BrTl5FyNDHYAYnvX5qR9RNGE%2F%2Bfh4jucGuyWEwzwMfGQUldN3iDrR2scvUF465V31TJM6AH2Rtv7dr9mtBxkpYTM9qBz0GQjTsRJdmVu4PdlKyiRyqMZZqmWD39c0w9sjmXJE3XmtqLQhUS%2FjhfYMdA0MMAL25T7KUysDOcSVBhy1B2UEAo&X-Amz-Signature=7ea3fae34862a45f81a20947cb516c80eb129ba556779139f3fabe4b735fb477&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



