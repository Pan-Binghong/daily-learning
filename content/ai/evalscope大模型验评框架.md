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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Y76CNXR%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmCr6ayHdOeCgFncihLCyyVdpLuryRQBA5zHWAvtXdPAiBnINiufvvhut0ce6peNvzle0siKkkPQBjuhhMML4QYgCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiBEgFaYgD5hIgz9aKtwDBLhUu%2Fr7DQjnzwB6vPy69Dtts8prNYHeSxHuIIBHHr1IwfU2Amc9LG4DXvJZkhJduHpssFRXZG3P9VfQ9OmHEqDWpas3sHodFDbmUBJPJlAEjs9nxXItCdGFIDGh7ayRManrAcPc%2BeBIrjCzAFmIIkw7kgo4GP9PthCOTvIOEhfCo%2FsuhDIfiewuKnWgQCeWyIYlqyoj12WvV%2FvN6bxXsa3SBcNEWMaorloo65ftEkGei%2F%2BYs1%2FVl7EDWJ76pnSFyZmjkUHRsvgjwcZcMVdDHsRm9s87FqO%2F%2FczHKJXnHlgmcspaZcTpv8wVLFvWPMx1rff7XWuUAA1GZA78LOV1bW3lYnGUWkXJIJvCNAh87ZM%2FstME18JoVNe8Rp%2BM1JWBk5K5Bfhev9Q%2FEmAvibEMIqB4XZXA%2BY2JU%2Fg6o1Fo%2FGc%2Bx%2F3MQn6YItt3I1N8pmB2LCWBLcDuSu%2FFbzDVhG2cORUYtsBrr8dTjakX7g7J4bitlKZ5mWOsvDplj8nj3dve4vCl3%2B2g58nCFWrsfIx7z4pp2UGVDlP6fa5B8kvBVTSDAz8J7xDeiyqX9QKU1qiSCjpPBnFKCWvHmYgt7xowEhsdFf8VrfZmlFVrB9ZrTT0uGBLg9lOdWS3%2BG8ownZelzAY6pgE5Qou1Ho%2FY1AizqXnzAoOPplP1jmsowLJuPDlzaCRxHvPPscX0MYCPWRKWo8cNN98%2FooLHl%2FK9meM31rwo2Q7ARuqpdsMsagOIa%2FYqQ2KBq7uHKQR%2Bh7qGaGBWlO5NHOworzPI9lRisJRSJw7wNs0bzGUBbL45YE1y1lzB796FyZAZZWXUv%2B%2Fe4FKW3hce5ibHieCH7HJFa%2BK7LYIpr1LP2LAMZsDA&X-Amz-Signature=26575d88bf30c2a0b6805afe0f87963909139b370793a1560a5a040672ed12d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



