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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I2EACGU%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF92bSYI5vcEnm%2F1awkCmOy9Swm3kgkkAAM37tng5RYNAiBgica1H%2BdfAxOH6DTgq0L%2BPcsrLwropnFe84lQa5uSkSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMu88ttSht73YOgHfsKtwDwmgOlyJukgR7qWRQE6PftRODznmvZgTl%2BDAdKnC0bvyoeMOuXtFynYRC2ehKz5FeR4%2FssoTtRcTJkGlpcUdYs%2BIHBakXjwDBzAsmOojne51Cbvhp1CbokGchrn0%2BUmYTYahJnpPoIP9IbPFeRnEnsotjWJXEv7VIuBQ7ebpt0uEUyP0RTPNbmb%2BKVnDjRRsUmwSVkAol0E6PE2JlOVpMHTewYxJyCPvk9dzWjDywSyebcRc86VUxLWufZpZd%2BVJR5BDwtapaeeJhzvBvhkXLM5JOGDaVJbwfHx3vlTlT5830FeQdYdg7CUuqjrMXnHOsAFjNqJ9mphM%2FGEaZ9rnmmGPsqhImg1IHqGsoCMWxdJFFHe%2BRHQvIFblTVvaDYYQKXWBN8%2FFwDkdUjc1KexiAUR3zw9DApJmVZZTLI15MpnqBY5Omm3DE0PGetccRXK0SFlkzabaILCvMoAYiD975Q2oCOpw4Fqg2Brq9gOhojmJ6oMXut3QhkXlUci3zGeeauNPszvAzc1c1VhZWRuPJBlM0YqqVuNPk7jHsApuVDdfrbPihK8m52lBls7dldvJ%2BD6F%2By1SWbd%2FjQnaTdnNjsqBQYNiQufLSj4qXcei0mL16Ry5f2Qq0rg9heXcw%2FbKIygY6pgGQtFi9q1dTgAFZyVX1BKFleQnnzor46aOzawU2p%2F5H2MpHHrlzvqpc86M5f8CViumlGEnJ9oFG74uV%2BV9GRj7Y5cy7enIMEgJky%2BBnaot5UKyjca0WQN4URDcT8sDBV3XZyrQMbdfrIZJ8wbB6T%2B94oIRRYe%2BZCzPbxqmv0i6tbh%2Fk6NUKQDtO1i%2FSJKtjOS9LqKlB%2FWq%2BKV45wp01OE09J73fJlcI&X-Amz-Signature=033f5e611d3949aab26485e34cb49906309152cbc1a2c42557ff2a41fef609a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



