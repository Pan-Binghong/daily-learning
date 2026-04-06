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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2XT3UOT%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMOM6Fhstxfr7wG0Z%2BdOIzSh8Tll6RKnhlBFf2S2mTVAiEAviOSJvz3U9lLMzK5y6gBnkrgHGz%2FAH82hkLVUUQrqhwqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDExUdTrCIpIX3ykRAyrcA13t2rZbN41BKvBZzzfKnFFfefPZg4fgg%2Fr%2FMJiM8XpyfcoduTCt4svjtNgriLZwZzf9%2FVdp%2BdrGUejmKNGOEzw3untD8Q%2B3WkHHj4%2FmrfqjI%2F82WD8sAGjP52ULzfqCWwPu58C2oz3NjC2dOj3gI7pZ3%2B7YjZtK%2BjheFll8RW6psx%2FfUoMtyor05OD9jkhB%2FQksP%2FhxvmdNOuLzaaIp5Y3FUYV8CiMm6dx5SeMWuLn%2FXhp0vd1xq2%2FTHRQL4cqStY02T5TnIbWM%2FtCA%2BhKC00SrkZiCDtme2tQHJDpWJEuxRIdTG9xmKv7cM9VDWODnnxE3caItUrThyBaDadQesjFwMDP6FJHkHYeCrQBtfs%2BiH6yGxIW4hWH%2B%2BW%2B%2BSKqYuKiXhUyQHmhVYajmyysLJ9aUDwdX9z1HKP63QUF3LG82AjAOCQsPuV5EG7vlTWvx8BdpNFajztoAdt7ZGeWDV%2B2hmhRpUFGuyFtchebl0eDSzgDlloDu2vFxQjjkLt%2BT0cXjaTgsxYMmoHytUXF313Wceg%2ByOkVEiOzsamsYVgDM2eQM65Xoar5AViL1CTYnP9KkWmWfAdVUkD3tY4cbzTsfLvsJLEfxk59YkfExg%2FYdpgF09aq90AbCEN7TMNSxzM4GOqUBp2si%2FrDrH%2FG0m61XTfTYQ7cvc3V71%2FE%2B35Z9nUV5DNomNUPxw5zkCWlzsmVR1DXcrDV%2FgzjeCldV2axF%2F1i7NcidI3iVtbpJsprczDHFbDYrN9GaEqu2tGzmLM40LF2NefksDpxirR0JJArd0fjlTQgrLI4LlUiGtLcYOgHTF4R3OvH9XMikM4l7Y11Xp6sB2Zd2A%2Fx67YPus%2FFJYvhy9fZqLbgp&X-Amz-Signature=8de5c04eea10b1e25dbc5aed27f0a7aa96aef2af3120882277440b44f6970a39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



