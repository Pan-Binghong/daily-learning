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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN5VITE3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgxx6l2V4ylNxegM9HkkKIrNggr2eC8CINzWiIUL2cQAIgd%2FD0tZrPxH%2BXEIr8PjDMUQ08wGgtnyNfjLyoNtNeV44qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCYefShLO5pQM%2F3KHircA1tyfRoRJ1scD5q%2BZsHh%2BLupLbhgLRWjxmnal%2B%2B8KayvtbwcHTuEeDQYF7ZhVfVgScMgYf%2FeY9PXHBnco0TnAJOuhLO9H5yeDBDxK84pGlKlRQd1bYmOjwtnuFGqd3GZAVDWo01ht78jj9ly9Ilt1U7MnoIv%2FIxiHtLuM25zqnOSFTr5swT9cfVszzdsBoFSN5JjH58i7caI2GGk8OyxfiH%2FE5ttg2S6OI4iYxlFueUzMt2C9xJzrzvPLt%2F3%2Bqgct6Hdb%2BbLV9PaIwlXlIfpNOb30CH2Fww8829HppMgNVlyHB4CdBszN3SkXChKrJrAdUZaaI%2BxCOTnKjQjLRtRwsYUA%2BmeNayLfpqs0AY5RmfNprJ9uota70OxN1KwTxhJ5%2B8g0gfFbyxV9c8gq%2B3OVd%2Bpc0CWUY738feQJSdtJ%2B1XMqGDdsswIbiHtai3%2BnEIULPxafQfU7AM%2FNsV3yG%2BTLKETaertye%2FG0dHICxk5%2F5xOor%2BixT1ubA0Uv%2BllgsozD7%2FFvda4bPnxDzZNLUdvHs8k4c3l9CBsyoHWmLD9EATEQjRJHUHfjdbe%2Bt6WgPYNQCQ78gvdzqseo3wC6fmAF5HgBLB0CeEj25%2BVSxEJYPcQfJpdAy3DY0dRVppMPDxr8gGOqUB4geiPO%2BMMka%2F64%2FGVX6ERVqZHBQwR1pIr4bilzbd3uLuSrvrv2AgP6m1FZ5NG1%2FeSG0GdErHWnMPLpUJmP3VR%2F1gKt7waZjOsCnYK1p4id8apJNtJU%2BIiejibeeFacHwJJ5YSEgCUnqH7ajF4t5rsSSI0%2BZk0jUu7XjoLme0DgQGWuzkZ7SB5nuUAd0jKHNmNtd%2FkOSa5W2qQuPwmqTnXe7FObSE&X-Amz-Signature=f04f4606da49d6ba8fa4ef4ebca1dd9a0bb687a66eb897bc7abe6a7816fc8c90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



