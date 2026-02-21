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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIREMTCA%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCiCU%2FUHhF75W1V4O1xiOiRVTcdudb6eidJla9gLXMGOQIhAJS6aZ9QZ76uVHlEFSYGWKHNsPWorsjDseKWEPVfD5vUKogECKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdA6EXugzY18rZiLIq3APtF6v%2B2naZxzzAjOdlO3mHY1HPHXypM8EgRHb%2Bno7Jf2uApNAUsJj14UD9Y1G0W%2FfbREwiWCrz%2BPiOeTCVHW782sDP%2BCvx6ioR5vFvvjGva6yfIwLfQTwN2vn22qFhUSlEuBOk1Z3HVDeuyTDA8Yijv%2BldibXDYk2Hq2NCW3YWU2IYzCkk9NonIPtgJTPgG9AnUBEkJK6%2FIRcreZTjOk0BS%2F%2F7QiRi4yoVF4pCXDDD%2FqFmYK2w%2FIN9myx0ps6CUsVgTw6kuHW0YtwCf0HHowjY95DZFXfDIlQhYIXaUOkVPJ%2Bod6Cy%2FIJ2lTbl4r0SkteK5tZ398cYu6yQmjt3tA0DJ1jpH%2FZkwV9bH0lyJ10BQfNsgJ4Tgb93clBpQyDNrzzF2kxiGeSaZ68vios%2BEMT2KDke%2F84W3HELUW8SOEhiqOKtHIrlN4aM9Fo9k0UL%2FdSgFMRR%2BKgMWVdehb5KJwcB4LsjcdEe1GMLq7Mv0F6UjCJPfrflZVuEtDi9q5gUWTJC1NpBU%2F7utus2bh0Rfl0KqYZ2I33G8V4LAEVGioxzvgXorX2ECNlBE2PrQ0eAAMnBqmAKxsB2NdN%2BPT18xseX1jScOXWbf%2BwObUCdrYebXLA7ZC6UiJTW58QGJjCIveTMBjqkAWcAJz7wzS7RQMmsAqDhoPmalxP7hvIFdxLvu9yM0JCWjnXIt9A0GdbffHcQT6vrDA1pboRB%2BjbrJtMIYaYUTKWtXq%2BBgqbD5KsArUtAtXNQ2%2BpWzopMk6B%2Fa021zB%2Fu%2FXUEoxeoKaeeJMrzM4NB0Wm38urw0yujEriSPd05iE9gQZY34TXgn1FqqM9Mecs1%2Fmki9%2BrxM7BtrzGr4EPBF341g%2Bi%2F&X-Amz-Signature=b0fe99b8e6094c0c79ff3e63a766c308d6591db61a4a3ed9a36fa943738d8bd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



