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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNADRB4E%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCN98fhVNjbrDhnikT%2BQyl7O0BvriovkOKp2U5riU%2FPgQIgbUb02UW5ZagjsO2GGKJsHqE0hGrzM59sdxjoq7hnVLYqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKPSEdSEz%2BMEkMfTTSrcAzNn0i%2F%2BsXQDluIwFSE2xqJP0a7qpJ8%2F7DaTI%2FvkeW80zUFyjDyfPbupNlgktQQYBKUzFiVpbV18rEQohkoGtRZzsHv%2BC5%2Ff6BIaG89QW%2FYc%2B0CG%2BSGNtF6hJcWmFv2L7JdongYErc0q9%2F%2Bbmfe5QLZk3zK6ERb5sJHvjmxNmTcJMxH3V2Tp5DmETi6sFsehk6LgqHrjgJQUCSEyOLzo6XEH2xqusawr01pkDgmqjuevOSSsta6bvKw6wXoRhrgXmx07H0UeFripNPqfeMLcrxjojATi%2BHQvSqYkpg2%2FovRIVWe0%2BVi6I%2Frg7Yi1pIxs9u%2BNhtZ%2Fuvw8Ajr2AXOzPkzW%2F4GieiubXKNwAUsrF8Vb5x3lpxs8e2E0nU1bSyRrunNBPtmDeNEaXsu28gr6asyhVM5UKwsB4G6yNWLU41KOpxfSfzjGY9zh8SntvLMR8TObE9NLQ%2FiwNjhjnd0NE3JhL%2BNg852sTc6TCbD0R%2BZod7HvCKome0RC0Yx%2FzLbIdHIhtZwWsUi%2FvRp1ENxBNOLlMoM5b9FBcn6pjomou0aalCHuBKbGPIxjaqDqiZnU1YHeKseDmCf53AQ5fB4Q7C9RE7L%2B9W1jflVMPJ1Z66JR4Sr1nBIRWxq%2FHfgrMNz90skGOqUBPLytIi792pZunWaCWSiNrZwFAvk%2FGdjLyh6oUALIK1GFsx1I%2FxpTOHKIEl3TQEwkqbxqfG5P8lCxgAwLAjyWdNgU%2BZUoEZFtEHiTOigcUUyf9vcu9h8%2FCPUVsOJCF9HQ4x8%2FBWvcX2pHLrT6ooy56OM5XpvLXTbGncBJvNAwjvkqSkX%2BWMiwwwBFdg9T1tza9cJH4My%2BkA4VfHEwgiK%2B%2BwqezRxN&X-Amz-Signature=c5361ded489b299c22b20f549a42462ef2f47e0fca773166e6dd07ff5e931ed3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



