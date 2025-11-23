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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QNEOJ4A%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQD8vVOz%2FI0G21OXTiOMnqtsFRv5BLhKW7743TJqkCzHrQIgMFfXTRDOPGWvF4618%2FOIwNkGwrLH9rvhbTEqtIUrjsYq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDJL5jblZtL6Qnw8JSircA4LmfyS7och3ENZ8whTC%2Fy3Wx2UQCzKCCrCYrj6vmMu08nMfTIzQDCWJVEpS40KMR%2FbQzb5M3yJA2p3pgAAJI52Q0kOtdBBwwXmvTDFPACNnTN0JRVG0zGFkRHdO5T7RuI%2FeevPhB%2B%2FDxSEVjp7pIxkCu4pQS95mRJJp7t8kj%2Fq9i5IvPsg%2Fm%2B8XgmCzCGAdqYXLbDbIojlnCthWHuE0V%2FdvpVUljFBL0reOW9ICY%2FZKATWNj%2F6%2B2SfgE31Jl7yZ6gjnpZR2hiwyp4Ke%2FWxg0mBYVqx9uBNGy6n00eFhsvoQ%2FUx05zhhi%2FiDPf7yqYAsyWTopWOrxJEDm9N6weycJ6TphW8f%2F0l9xz%2Fel%2BmMExTKSU3m%2BwPEfSemn10s39pW5gvbRT9Dtwn3UxwbZU0l05zuqhksbn5T8s6%2B43LJnv7JqPD8kJbNLqYw28tTjd6Mnd44oeO3bfyh1G9rlWfGM%2FPfuGArA112OLNU2Pr2utZB1Fmzm1HRaG5NO%2F%2Bh21TL5EDqnqtZvYptz5yhRNaMpBogLvXAWG%2B0vLVGybYorRuOXfXHA7A4ggd7tvGfm%2F9fd7N2qQvQ97sovLlT4%2FJn2%2Bb%2FsBJzz5vuH2lfuNCaqR6aPim2DM1jwDHkfWbDMLuwickGOqUBF%2FAkwXV8VuyxXazD4VzjKMODPOnWobFNoB%2BADcAmek%2BwYPk0Vkphp0EyHl%2BPh6QgZ4tJXfKqZ0CDtwYNerTKkd8Talr6snU72a%2FA2dnweoK%2BHfEmBhmyqRnTYzhPuW04VZeaCbxZAXAw1ykUWE6P3ovTI8j%2BEASNlXo%2FKweDkTw8m0sKjktjLwgKxgedWP2Udp73nRzF%2Fl4qP%2B2lhP38bffAbzQ7&X-Amz-Signature=c1dce5bbc140de5fdfd224e6074c1a5da77ba5716709ef473e18279e1fd9c4b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



