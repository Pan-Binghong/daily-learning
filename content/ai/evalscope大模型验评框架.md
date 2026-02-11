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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIZHPDWF%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDbNGew2bXHfBidiYWrEmOrVCgsucZLrHmA6i5RE1rbJAiEAyCG8ACRaPgxkXMguD2AHkqlVICIpbE43BJSh31GFtawqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKXAY1KDm%2FCstIicTircAwWI8FfETnNqJtJKMMLZB1SnzHY3oL0z8r7i0UZSttoBHwZjUcPewCCAf2%2FsQHPWyT%2BUZvTEu0Qa%2BHtyybXQA9WvjuDL%2FKFWD1zFjSdPBbrw5Ndbz42sOp6Luj1h9HCGCV8XA1UeN7NFhG6uj8sw4m1fUDxfdLIGOOoCnkVn5YbrLLtltYgh6j6dBUh3PjXOUf4IbAXK53YbsTBjFLw5mI8YyNIMSlGMQDKEX6Y6UpNGd72ZwPKJLWBbeqHUKBvEv9GXqDYbeCALPOhMqUf7QX2wzIiMGqiE0mDOuQ6sNntAgH0fmErtao29sxZzqJIp9DTFF34JsPecULXFFepMXzBZagP15sHhfbD4S1KYP%2BTikkDw1GjbxrsJMrL9RXvcO6Vz6OcyuPNtU1uxxYs%2B6jpo0lnp0iPpm7HjqOWrM0LVNjRfbPSfEudffvD7MtAF%2FUGUUHGWCL3NpojRoALuM1quOW1SVcQtw2apTk42v6GpUFXpa79vQPdP7s3XZu3eI%2FVO6Ps0w980k5v%2B1wxVgGEfQ4ApT%2FaKCY8uGlmEVsi%2BBeiDe3w4crbOemLXCieZ%2FII%2BYHYaVZ3dHTUrZPgRWjvarGo9uUaHhaa0Re9vL%2Fj2L%2BfSsR%2B%2FetswSRVUMIPLr8wGOqUB%2FikLwdPB9SD9bhcAXzD1HPcfm1RcZBOpGZc89k1tYko%2FQKHpDgJ3O3qU%2FPS9XfygA%2BHedEAot9xmh1ExFZYzu0KoX1KDCbwVzcw8yWnY0C0LZFNMftcdSvcfSpawDKy4qSMCxRtQXmnmDb2sVY1tZTqPUw35M6F8tJUh8sMr2KAsAWlo5HkOz8ApzFG0UPjoTGtQ116a3RbshPWWV6uinlczNaZv&X-Amz-Signature=f68d60547267588ecee013b285c399434bf139f373e5f14f81ef8efe522fa265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



