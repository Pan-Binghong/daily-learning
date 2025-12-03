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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NVPPA5N%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCijGpBOHORM7tdWHVsREaIQssqF8UT0kJxHErwWK24GwIhAIXrOdDs7S40myyx7HaU0ijo0PIx4OOCw%2FgcfFn1mXbVKv8DCCIQABoMNjM3NDIzMTgzODA1Igw297Y6WHD7CnvTjF8q3APAvVcV2z3HVjP%2BgapNgVvhc6wlzL%2B2eR3zSWCTw%2FfIBxqJ5vEC9whMUIkFxLugz%2BUPJPPQjan3JefWtVVSBahrZz3SJp67Z82ltcwm6MfKzYcaRbGZJp1i00cG0FwIwc0RhxaOi1%2FKigy0BGmEQTmICI4iJwCCP%2BSdQsPRfomXUXxJ7FpBOVAtICIjpe3LdVDQP01d0ZgkYtl3qtcTuxQIkpXwcHVP3gYdmB1oz%2Bb1e7YdH9n7krrfb5N0DGlLU8N5Qpd7IBf7Q%2BudoIiPbmxz0Q4m2GuBgxlStr0MJ6CItkmn5RBSbRSTXLuUQM6sizx5WAi0GlO%2BRQCO%2Fd2DpfdmlX17zkT6%2BQXqo35R%2BQGnCtWZQyVN8swb8g%2Bot7Ns9He9WpIE7lLx7Pw7%2BOnDB8HsPnChUcBASe%2FkHkBDB0PoW7epTOV7LwLhZEBkUZjNw%2BG9bxB1%2F4x7Sb22BBbc9RtWt0BJ1sAR%2Fs9k3vJfiRT34c8nmR9%2FDoQL6K%2BTxFOY3FXQLhpKRyzi3jrG3zWqxEStcI93yQi8QmQSrFV89yknaRr1uRJ%2FQQPE%2FPvjyx3k3jmFxyuhe71QbvX9V1Nd4migRUQZIfrScPsirdbdHMmPt0xYxjP7sCXaBtDuNjDelL7JBjqkAYX0SjUVAzPWFLeW6bpkneGp%2B5wy42dt73fV4P6NdewwxbuSoRh0vvb1iMv6UW1QfTaDWIbmP%2Fl4SmnHYdQDqd4Ok%2BGnXWh5glW9HW51SplltoytWi0s72x11AsOKeHIvcKJ7AxyQCzHZbsLzJuvjSROWLx8HS6MCSo50%2FmnVe8jwpuyQ9DOi6ftyfI4tyguq2WqVlHujiixe0ih0ZtlBkfF7ZzI&X-Amz-Signature=c01e20b5c9bcd868bf43a52a1e577c988fab8ae3171e87cbb8279fc50b2c6763&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



