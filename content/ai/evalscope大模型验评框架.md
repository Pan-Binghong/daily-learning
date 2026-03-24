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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJH4IQNV%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCD1HA5bqFRO4t8EEXNgNwlT8AJ35k7jIF9wVkPe7GyDAIgPThLzlFHIpPRA4WMLlw40dqMN1EeR1c1hn2XVlWp6bsqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF%2BJdeHUq%2BZwxpSAWyrcAzDZrxZFAHWpAFEhCBySzOat0oaQ3uuTbMjfzfD0CHugrPWbGXOOwUc6%2F39kJh5WypaJGM4%2F2kUEhTi1gA7UGhRmtha6c8lcSXK18WdLTW5L2AT4YkJotrYMCjUvYw8DkmCH73ZVy2zBdfKnMq9%2Bh8cZv1LhX1em0GGBAjOcjCQk%2B%2BIUmWW76AKq5vhRZnKc9V4f5y9vcPxzsAcIffpp3GIibpbDE6iCk38bVz3E6XkdjBkm0JfCDZvsntjb1AqZnk46QclIBbmv7hrZsVI%2BwGP2eqnvSv%2FjcsZ2CKJD2gCmIqVCkAv%2BtUXFr8WYGVSBVVDr7SZmLRdDMsZwYKFincOm7RmblZ2Hv%2BxRAqJceV9UA1jPWfuWCbZDXzbDkNUh75wkgV0ZeLXyGxSq7PsPhaPkVpL6NPbtw4CuEH%2FmpGINggxbYbQlRzKYNOP99WXZMmFk9ua0JIQMVdPuXF8ThFXyKU0qw6LElj9j9lPPVDekfKU0dONcG0XbKoOj%2F3CbX%2BKEvN2jIn1Oyh39yQQbAfgAHgSb%2FxZTYMmJR2BSvrw%2BiJr1g41g9%2Bm%2B25qV4nhPKUiVA69sXhCbG8CnxJld8opW44Rg0d5m9uQzr0XxKkIXpNQv6txtcmR28kH9MMjyh84GOqUBZ%2FG8fODaj8%2BMTav22D9gMB7NKmHIetxVOxyORxfa8klGjbY%2BVscJITNCh8pOTYUokM7Cr%2BdJXELfPF47POT8z%2BZr%2FZJ%2FHmUqXudjzfa9sPCn3gkG26TDs3%2F7ZTe9mn%2BiKKkcw2A7X9M%2BLS2haBGNV80s3Kq5uEVKsmtZCgfBdUP%2B8dCy%2FFO8ShrgU2vKqTIdmZ8cpXKNc%2BAaaKUpd0dNF8yR1BgE&X-Amz-Signature=09ffa5642d15058d456afcd6d4e61ec7a97d139f05c4c10eb5908a33b6229f3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



