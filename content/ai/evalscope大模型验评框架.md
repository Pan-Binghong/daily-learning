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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/29bda199-ba22-458e-b9f7-79b94cd6c8c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJ643BMA%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030029Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAHfB56LYH3MYrF3yDENeu%2BSMfDujtZYUp5U2t6zdDubAiAvDLgECVoagXtD%2BR0NJPpCdTK17O3Fx0lezGQptWTEkCr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMBOEZGN5cm5CPMKBlKtwD4iet8XMCG7iN6x%2BwMGSEZTST0GZVGTQQBgcOGUALnk4nD75VenCmAr0thXx4rBojaeaPu04e0ilDulY%2FshWPvqxS%2FAKBPFliAzghVdMKLE84e3CQKcPkXnbhEWjP%2FV2bvoEmdT6%2BQGzH4onNucHZZ9YDV5J9%2BY5VwLgYJhnMaSKnQTdRfYV5rpu3N5qhvqHd6ysksdyTI2mEHiHOZDsaMM4NBVTEmMQdUMFcUqVJ0elH4AnaLNyyx0vaG9F0xe67CNe753vGW6lkPLAeV%2BDMdTp8Jw%2FyDxao%2Fm6P4ydsdiwP7GyOxXN1Z89WR3KL21XW2hyBWZ%2BSQx3xypH6Zv568vttGRlAtcwpB6ytxs3NIlY12qg1VOnh3YkpTkte4NC9J%2Bb4PuZxRT8uGjLCLkKwwR6Z4XNbK7CT2QzSBZL1nRnmDB8QSQVDcA6USyCt20mkm7PrDoGd3qyXl%2Fw2vys3i1HnGgUkZTi9Prhw2j8AOYBNtevGMV91X4VrHJwG04STg5SgYdeI2klA7vTaGo1k3MR3uLlUfuEczs3B0JFj4%2F5GORn4bEoRmrvS4MPScbpPYm6q3zB1Rv%2BLyxAzn%2FWrBEqyAD9077nM8YKNePnvpMLT7L1Gb4d%2BWiIKO1ow%2BJqhywY6pgFPcR8qcpWh59a62JvardNqtFi0Lr7uXTHncBL3sUEq4d2jief2UilUTeHi37ygt6x%2FjXaQI5iEWBKKvEon5ou7IVatoWJzubTRXRhOUecZzWF0hjbySTt5yhh9NcUtX3dAY81Nl0VPZ7herbGXgWtEFJuN2%2Fkso2yqLy3SZTC4VPA%2BfWilicw7T7RA2%2BsLFRr5BgXlrwvh4LhnOqK1FIhr5gLm0lIo&X-Amz-Signature=e70322e1a0da3190170932c06e86fc8677f5949ef16bf5fe2b2b5162143f96e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



