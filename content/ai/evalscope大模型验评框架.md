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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPW6U5Q%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIAJP%2BXmb5%2F30R0%2FxEvFLz21e2L3hztprY2TtkdzrDQM1AiEA5Goca7luDacALT%2BrT3ggi9jg6JMFhDoLnQTmUfjkiTcqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGyZ2Kk8nEDqsoAtmyrcAzutmbrLQ7eMcBIu6waqDPOoPWMaioiSlM3kXyxLE1CBBK3Xs4%2B%2B2dDZrVtHxrxy6dVWR991KWfEsSSLKiXgPToPtEuXDkvSiXSQcLySQiGEOAPiCVJ7t8pXhOqcMPDvQFKYgKDa%2F8p1AY5SHzf2wdsf5vpAAhBUyK5Ey55FTIo3sjGo6uN8BE158YCs8tEDGxRSZzjlwkxtOPV31ZuX5EBjjTtSLmPvsA%2B5aKSFagqSsiDy4rcIL7aE8OBPVvBj358h1SJLZ%2Bo398HqPABkUqnqVWziYHkHbfrtlKs2Pu8MUlFbXfzmuKGcZSY7qNLGNPO4lybHWfb3CdwSza%2BFv82rimPrurY%2Fc7FHuMv8oQjx4S2yqnGMst7OklGvBsxCFtfVu7WLlUHOmlrwG4BYRcIk8byUevE3ug1JnKrkf88VNeOClh%2BTz3W2TMTM%2Fgt%2BqDKBlfEHsvDzcgVonD9npVOxnFCBk6UoYHh5iZsmlvF%2B6dgoW4wxDjYhvj2D4wuJPwSzIbFXepfVzEyBqkM3ptsU8VL7igQQ%2Bwt4V50oM9c5LGn9P%2Bawm0mJRC7soOWQqFQepUovvbGbPcdJ5qNAd8KbB%2BSumvCH5dZQbIQDaBISed7fuo3SQ8hX5IOzMPi3xMgGOqUBIfpaI1804nqOu%2Fn2Lx86o9k8xv21uBR3MkheU0CVRCZfDFLmmdLMJp1aGwEVX9fCMitMx9vArhTA7fV6i9w2mg%2FOikDPE%2BbW8ceOUrfpGl%2Ba2pG%2BAIGsNAc4iXUjS%2BoKM5b9lxbXBjxwpKVY5qWdiAyknfsW4%2Bl4eThdD90TCzBRo5gxQKAmBfmWFXYTOtpAC4lJ0SQ6kV%2FE6%2Bg9MA9i2IpgRoRZ&X-Amz-Signature=d4f3568df9d991d074d2467283c38a826efc2f81ce00cf8335202c557c4b16f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



