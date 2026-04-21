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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AYYQ4GF%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCxRQLta5LhdnEqiGkeyFPxULDlCtfqeStXa7erLMgAEgIhAMYYw2pWWqIHXPAKUTs%2FfqORgA%2FTYgYbU97ImHcM4IjkKv8DCCwQABoMNjM3NDIzMTgzODA1IgxopxsId23lxjydNpEq3AOp01RNxdZ%2B1UvJeGKm9rPd%2B1M7CGYgjOhT2AHQAdFZMw7VIUW4iw9reV0dDDfRmY%2FDI%2Fw3YGUwlvrKB9i6T4VmhRHhCOWugEmIrDjepeQvDEwcq8G%2BHaGA42DA9VC02PNyOyHp6RrE2aphr2gU1TbAupHxLIcXWTZm19c7bkpZ80TpZ%2FEJTwyijWsss9PjphEYcciZObGrnmAFkEWgn3xfpvsMViQGqjHyq7w7pIGePDMoZebXE6OpIT7i5VoO7KX8w%2F8pr33GLSc0TwQv0VbVC%2Fr7x%2B0SN4TLf39Gw2%2FnKdRpe%2FJBqn0CxsgYjp5sQWDkhtVfRUaWqV9fSkvpj9rFefeI3iTUhDdzfWoCoTEniWE0RNrhC%2FXGvz5fjO1Ez%2B6HhtRIDyczwGpJ7b1dyDFPAZ2ByZymrr4qXC4q8KvNjs7E7%2Ffzau3iV4IQJQqOFRiT2Cc6S3MyypEj6XMXxJL%2FQgVoYXSZ8h4nQrW4ngSvUd2WBDtyFPLcrydAC9bdq7XgL0h6Ac2YS8%2BSM9m6tik3BTu5%2FPwgBU7NnYR80KWe%2BM84g5MwFJze2kAf9XgtesUMspHL%2BO0kmNesn1nA7TDvjI084KqAXhtXMfZMvmIO86KM8d2LHwZXAxj%2B3zCS1JvPBjqkAfnBwPHw6jCHVkCzfw4lkk2iF7w0QtaPRXX0v6EI7yHb8i7DZqPvpq3KMK%2BIuM3O4wLEJrorNykjB9IIj%2FCi8rJjYWUwyBFQH0cQkGdXxLPFxUiij0eY9GjMqGSDBEIIfu5b7t01VOhXyCEPncpay0yXhmnk55g9mGgUJvj07%2By9gwmem5tu0QhAplAO9lNrHTzPuqDkoDF1uKKB4GMBtwvHXv9j&X-Amz-Signature=a35d5e0cf2c705c4ee7da055b47878206131eab636111b3bef4d08a9b9f910e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



